import os
import json
import re
import sys

import torch

import pandas as pd

from pprint import pprint

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import JSONLoader
from langchain_community.document_loaders.csv_loader import CSVLoader

from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from sentence_transformers import util as stc_util
from sentence_transformers import SentenceTransformer

from datasets import load_dataset, Dataset


from tqdm import tqdm

class EvidenceRetrieval():
    def __init__(self, 
                 test_dataset_type):
        
        if test_dataset_type == "mm_covid":
            test_dataset_type = "mm-covid19_news"
        self.test_dataset_type = test_dataset_type
    
        self.evidence_database_providers = ["nih", "cdc", "litcovid", "politifact", "mmcovar", "recovery", "mm-covid19_news"]
        self.search_evidence_database_providers = ["nih", "cdc", "litcovid", "politifact", "mmcovar", "recovery", "mm-covid19_news"]
        
        self.search_evidence_database_providers.remove(self.test_dataset_type)
        
        # self.entailment_function = Entailment()
        self.embeddings = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/multi-qa-mpnet-base-dot-v1",
            model_kwargs = {'device':'cuda'}, # Pass the model configuration options
            encode_kwargs = {'normalize_embeddings': False} # Pass the encoding options
        )
        self.local_search_embedder = SentenceTransformer(
            "sentence-transformers/multi-qa-mpnet-base-dot-v1",
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu"),
        )
        # Check if Evidence DB exist, if not then build
        
        self.evidence_dir = "database/{source}_index_langchain.faiss".strip()
        evidence_db_dir = self.evidence_dir.format(source = self.evidence_database_providers[0])
        
        if not os.path.exists(evidence_db_dir):
            print(f"Datbase is not exist, Building the Evidence Database with {self.db_type}")
            self.build_evidence_database(db_type = self.db_type)
        
        self.evidence_db = {}
        
        self.max_search_threshold = 3

    def prepare_database_runtime(self):
        evidence_db = {}
        for db_provider in self.evidence_database_providers:
            evidence_db[db_provider] = FAISS.load_local(self.evidence_dir.format(source = db_provider), self.embeddings, allow_dangerous_deserialization=True)
        return evidence_db
                
    def metadata_func(self, record: dict, metadata: dict) -> dict:
        if record.get("url") is None or record.get("url") == "":
            metadata["url"] = record.get("title_url")
        elif record.get("url") is not None or record.get("url") != "":
            metadata["url"] = record.get("url")
        else:
            metadata["url"] = ""
            
        if record.get("url_source") is not None or record.get("url_source") != "":
            metadata["url"] = record.get("url_source")
            
        if record.get("title") is not None or record.get("title" != ""):
            metadata["title"] = record.get("title")
        else:
            metadata["title"] = ""
        
        if record.get("abstract") is not None or record.get("abstract" != ""):
            metadata["abstract"] = record.get("abstract")
        else:
            metadata["abstract"] = ""
        
        metadata["summary"] = record.get("summary")
        
        if "source" in metadata:
            source = metadata["source"].split("/")
            metadata["source"] = "/".join(source)

        return metadata

    def data_loader(self, source, content_key = "summary"):
        loader = JSONLoader(
            file_path = f"database/{source}_covid_evidence_summary.json",
            jq_schema = '.[]',
            text_content = False,
            json_lines = False,
            content_key = content_key,
            metadata_func = self.metadata_func
        )
        
        data = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        data = text_splitter.split_documents(data)
        return data
        
    def search_db(self, query, source, return_all = False):
        if len(self.evidence_db) < 1 and self.evidence_db == {}:
            print("Initialize Evidence Database Instance")
            self.evidence_db = self.prepare_database_runtime()
        
        docs = self.evidence_db[source].similarity_search(query, k = 10, fetch_k = 20)
        if return_all: return docs    
        return docs[0].page_content, docs[0].metadata["url"]
        
    def create_db(self, source):
        if source == "litcovid":
            data = self.data_loader(source = source, content_key = "abstract")
        else:
            data = self.data_loader(source = source)

        db = FAISS.from_documents(data, self.embeddings)
        db.save_local(self.evidence_dir.format(source = source))
    
    def build_evidence_database(self, db_type = None):
        if db_type == None:    
            for db_provider in self.evidence_database_providers:
                self.create_db(source = db_provider)
        else:
            for db_provider in self.evidence_database_providers:
                self.create_db(source = db_provider)
                    
    def search_evidence(self, query, claim = "", context = ""):
        all_evidence = []
        ranked_evidences = []
        
        for i_evid, evid_src in enumerate(self.search_evidence_database_providers):
            evid, evid_url = self.search_db(query = str(query), source = evid_src)
            all_evidence.append({
                "news_id": i_evid,
                "source": evid_src,
                "abstract": evid,
                "url": evid_url,
            })
        
        query_embedding = self.local_search_embedder.encode(query, convert_to_tensor = True)
        
        evidences_only = [evid["abstract"] for evid in all_evidence]
        evidence_embedding = self.local_search_embedder.encode(evidences_only, convert_to_tensor = True)
        
        ranked_query_evidence_idx = stc_util.semantic_search(query_embedding, evidence_embedding, top_k = 5)
        
        for rank_ev in ranked_query_evidence_idx[0]:
            r_ev = all_evidence[rank_ev["corpus_id"]]
            ranked_evidences.append(r_ev)
        
        
        if claim != "" or context != "":
            ranked_claim_evidences = []
        
            evidences_ranked_only = [evid["abstract"] for evid in ranked_evidences]
            evidence_ranked_embedding = self.local_search_embedder.encode(evidences_ranked_only, convert_to_tensor = True)
        
            claim_embedding = self.local_search_embedder.encode(f"{claim} {context}", convert_to_tensor = True)
            ranked_claim_evidence_idx = stc_util.semantic_search(claim_embedding, evidence_ranked_embedding, top_k = 5)
        
            for rank_ev in ranked_claim_evidence_idx[0]:
                r_ev = ranked_evidences[rank_ev["corpus_id"]]
                ranked_claim_evidences.append(r_ev)
        
            ranked_evidences = ranked_claim_evidences
                
        return ranked_evidences
    
    def search_evidence_by_sources(self, query, sources, claim = "", context = ""):
        all_evidence = []
        ranked_evidences = []
        
        for i_evid, evid_src in enumerate(sources):
            evid, evid_url = self.search_db(query = str(query), source = evid_src)
            all_evidence.append({
                "news_id": i_evid,
                "source": evid_src,
                "abstract": evid,
                "url": evid_url,
            })
            
        query_embedding = self.local_search_embedder.encode(query, convert_to_tensor = True)
        
        evidences_only = [evid["abstract"] for evid in all_evidence]
        evidence_embedding = self.local_search_embedder.encode(evidences_only, convert_to_tensor = True)
        
        ranked_query_evidence_idx = stc_util.semantic_search(query_embedding, evidence_embedding, top_k = 5)
        
        for rank_ev in ranked_query_evidence_idx[0]:
            r_ev = all_evidence[rank_ev["corpus_id"]]
            ranked_evidences.append(r_ev)
        
        if claim != "" or context != "":
            ranked_claim_evidences = []
        
            evidences_ranked_only = [evid["abstract"] for evid in ranked_evidences]
            evidence_ranked_embedding = self.local_search_embedder.encode(evidences_ranked_only, convert_to_tensor = True)
            
            claim_embedding = self.local_search_embedder.encode(f"{claim} {context}", convert_to_tensor = True)
            ranked_claim_evidence_idx = stc_util.semantic_search(claim_embedding, evidence_ranked_embedding, top_k = 5)
        
            for rank_ev in ranked_claim_evidence_idx[0]:
                r_ev = ranked_evidences[rank_ev["corpus_id"]]
                ranked_claim_evidences.append(r_ev)
        
            ranked_evidences = ranked_claim_evidences
                
        return ranked_evidences
    
        
if __name__ == "__main__":
    langchain = EvidenceRetrieval(mode = "build", test_dataset_type = "mmcovar")
    evidence = langchain.search_evidence(query = "blood clot")
    print(evidence)
    