import os
import sys
import requests
import json
import argparse

os.environ["TOKENIZERS_PARALLELISM"] = "false"

import torch
import spacy

import pandas as pd
import numpy as np

from transformers import AutoTokenizer
from advisor_model.model.advisor_model import AdvisorModel

from utils.reasoning_module import ReasoningModule
from utils.response_parser import ResponseParser
from utils.reasoning_toolkit import ReasoningToolkit

from tqdm import tqdm
from pprint import pprint
from prettytable import PrettyTable

class CovidEfnd():
    def __init__(self,
                 config):
        
        self.reasoning_module = ReasoningModule(
            config = config
        )
        self.response_parser = ResponseParser()
        self.reasoning_toolkit = ReasoningToolkit()
        # self.evidence_db = EvidenceDB(test_dataset_type = config["test_dataset_type"])
    
        self.evidence_db_ip = config["evidence_db_ip"]
        self.evidence_db_port = config["evidence_db_port"]
    
        self.test_dataset_type = config["test_dataset_type"]
        
        self.nlp_en = spacy.load("en_core_web_lg")
        self.nlp_en.add_pipe("sentencizer")
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
        self.advisor_model = AdvisorModel(
            model_id = config["advisor_model_id"],
            batch_size = 1
        )
        
        self.max_length = config["max_length"]
        self.tokenizer = AutoTokenizer.from_pretrained(config["advisor_model_id"])
        self.advisor_model.to(self.device)
        self.advisor_model.load_state_dict(torch.load(f"{config['advisor_model_dir']}/test_{self.test_dataset_type}/advisor_roberta_model_weights.pt"))
    
    def evidence_retrieval(self, claim, context, queries):
        all_evidences = []
        
        # print("inside evidence retrieval")
        # print(queries)
        # sys.exit()
        
        for query in queries["queries"]:
            evidences = requests.get(
                f'http://{self.evidence_db_ip}:{self.evidence_db_port}/search_with_claim',  
                params = {
                    "query": query["query"],
                    "claim": claim,
                    "context": context,
                }
            )

            evidences = json.loads(evidences.text)
            
            evidence = {
                "query": query["query"],
                "abstract": evidences["evidences"][0]["abstract"],
                "source": evidences["evidences"][0]["source"],
                "url": evidences["evidences"][0]["url"],
            }
            
            all_evidences.append(evidence)
            
        return all_evidences
    
    
    def advisor_model_prediction(
        self, 
        claim,
        commonsense,
        # y_commonsense,
        textual_desc,
        # y_textual_desc,
        database,
        # y_database
    ):
        
        claim_tok = self.tokenizer(
            claim,
            truncation = True,
            max_length = self.max_length,
            padding = "max_length",
            return_tensors = "pt"
        )
        
        cs_tok = self.tokenizer(
            commonsense,
            truncation = True,
            max_length = self.max_length,
            padding = "max_length",
            return_tensors = "pt"
        )
        
        tx_tok = self.tokenizer(
            textual_desc,
            truncation = True,
            max_length = self.max_length,
            padding = "max_length",
            return_tensors = "pt"
        )
        
        db_tok = self.tokenizer(
            database,
            truncation = True,
            max_length = self.max_length,
            padding = "max_length",
            return_tensors = "pt"
        )
        
        claim_ids = claim_tok["input_ids"].to(self.device)
        claim_att = claim_tok["attention_mask"].to(self.device)
        db_evid_ids = db_tok["input_ids"].to(self.device)
        db_evid_att = db_tok["attention_mask"].to(self.device)
        cs_evid_ids = cs_tok["input_ids"].to(self.device)
        cs_evid_att = cs_tok["attention_mask"].to(self.device)
        tx_evid_ids = tx_tok["input_ids"].to(self.device)
        tx_evid_att = tx_tok["attention_mask"].to(self.device)
        
        res = self.advisor_model(claim_ids, claim_att, db_evid_ids, db_evid_att, cs_evid_ids, cs_evid_att, tx_evid_ids, tx_evid_att)
                    
        advisor_pred = res["classify_pred"].detach().cpu().tolist()[0]
        advisor_pred = np.around(np.array(advisor_pred)).astype(int).tolist()
        
        if advisor_pred == 1:
            advised_label = "**real**"
        else:
            advised_label = "**fake**"
        
        # print("ADVISOR PRED LABEL")
        # print(advisor_pred)
        # print(advised_label)
        # sys.exit()
        
        
        return advisor_pred, advised_label
    
    
    
    def runtime_web(self, claim, context, y):
        
        self.advisor_model.eval()
        
        '''
        I. Non Evidence Based Explanable Fake News Detection
        ----------------------------------------------------------------------------------------------------
        '''
        
        non_evidence_explanation = self.reasoning_module.rationale_commonsense_runtime(claim = claim, context = context)
        for non_evid in non_evidence_explanation:
            if "commonsense" in non_evid["source"]:
                commonsense_explanation = non_evid["summary"]
                commonsense_y = non_evid["y_pred"]
            else:
                textual_desc_explanation = non_evid["summary"]
                textual_desc_y = non_evid["y_pred"]
        
        # print(non_evidence_explanation)
        # sys.exit()
        '''
        II. Query Generation
        ----------------------------------------------------------------------------------------------------
        '''
    
        queries = self.reasoning_module.query_generation(claim = claim, context = context)
        
        '''
        III. Evidence Retrieval
        ----------------------------------------------------------------------------------------------------
        '''
        
        choosed_evidence = self.evidence_retrieval(claim = claim, context = context, queries = queries)[0]
        
        '''
        IV. Evidence Based Explanable Fake News Detection
        ----------------------------------------------------------------------------------------------------
        '''
        
        evidence_explanation = self.reasoning_module.evidence_compiler_generation(
            claim = claim,
            context = context,
            query = choosed_evidence["query"],
            evidence_url = choosed_evidence["url"] if choosed_evidence["url"] != '' else choosed_evidence["source"],
            evidence_text = choosed_evidence["abstract"],
        )
        print("-"*50)
        # pprint(evidence_explanation)
        
        # sys.exit()
        
        # pprint(non_evidence_explanation)
        
        advisor_pred, advised_label = self.advisor_model_prediction(
            claim = f"{claim} {context}",
            commonsense = commonsense_explanation,
            textual_desc = textual_desc_explanation,
            database = evidence_explanation["compiled_evidence"]
        )
        
        '''
        IV. Explanation Selection
        ----------------------------------------------------------------------------------------------------
        '''
        
        # pprint(evidence_explanation)
        # pprint(non_evidence_explanation)
        
        
        rationale_guided_evidence = self.reasoning_module.rationale_commonsense_guided_runtime(claim = claim, context = context, advised_label = advised_label)
        
        pprint(rationale_guided_evidence)
        
        for advised_non_evid in rationale_guided_evidence:
            if "commonsense" in advised_non_evid["source"]:
                advised_commonsense_explanation = advised_non_evid["summary"]
                advised_commonsense_y = advised_non_evid["y_pred"]
            else:
                advised_textual_desc_explanation = advised_non_evid["summary"]
                advised_textual_desc_y = advised_non_evid["y_pred"]
        
        
        # print(advised_commonsense_explanation)
        print("-"*50)
        pprint(evidence_explanation["compiled_evidence"])
        print(evidence_explanation["pred_label"])
        print("-"*50)
        pprint(commonsense_explanation)
        print(commonsense_y)
        print("-"*50)
        pprint(textual_desc_explanation)
        print(textual_desc_y)
        print("-"*50)
        # print(advised_textual_desc_explanation)
        
        sys.exit()
        
        explanation = {}
        
        if evidence_explanation["pred_label"].index(1) == advisor_pred:
            explanation["explanation"] = evidence_explanation["compiled_evidence"]
            explanation["pred_label"] = evidence_explanation["pred_label"].index(1) 
            explanation["query"] = choosed_evidence["query"]
            
        elif commonsense_y == advisor_pred:
            return commonsense_explanation, commonsense_y
        elif textual_desc_y == advisor_pred:
            return textual_desc_explanation, textual_desc_y
        else:
            return evidence_explanation
        
        # print(y)
        # print(advised_label)
        # print(commonsense_y.index(1))
        # print(textual_desc_y.index(1))
        
        # print(type(evidence_explanation))
        # print(len(evidence_explanation))
        # print(evidence_explanation.keys())
        # print(evidence_explanation["pred_label"].index(1))
        # print(evidence_explanation["compiled_evidence"])
        # sys.exit()
        
    @torch.no_grad()
    def runtime_database(self,):
        if self.test_dataset_type == "mmcovar":
            ori_file_dir = "datasets/MMCoVaR/MMCoVaR_News_Dataset.csv"
            shuffle_file_dir = "datasets/MMCoVaR/MMCoVaR_News_Dataset_shuffle.csv"
            predefined_advisor_dir = "datasets/fake_reasoning_entailment_guided_data/fake_reasoning_entailment_mmcovar.json"
        elif self.test_dataset_type == "recovery":
            ori_file_dir = "datasets/ReCOVery/dataset/recovery-news-data.csv"
            shuffle_file_dir = "datasets/ReCOVery/dataset/recovery-news-data-shuffle.csv"
            predefined_advisor_dir = "datasets/fake_reasoning_entailment_guided_data/fake_reasoning_entailment_recovery.json"
        elif self.test_dataset_type == "mm_covid":
            ori_file_dir = "datasets/mm_covid19/news_collection.json"
            shuffle_file_dir = "datasets/mm_covid19/news_collection_shuffle.csv"
            predefined_advisor_dir = "datasets/fake_reasoning_entailment_guided_data/fake_reasoning_entailment_mm_covid.json"
        
        datasets = pd.read_csv(shuffle_file_dir)
        runtime_pbar = tqdm(datasets.iterrows(), total = datasets.shape[0])
        
        for i_data, data, in runtime_pbar:
            if self.test_dataset_type != "mm_covid":
                claim = data["title"]
                context = data["body_text"]
                y_lbl = data['reliability']
            else:
                if str(data["claim"]).lower() != "nan":
                    claim = data["claim"]
                elif str(data["statement"]).lower() != "nan":
                    claim = data["statement"]
                
                context = None
                if data['label'] == "real":
                    y_lbl = 1
                else:
                    y_lbl = 0
                    
            self.runtime_web(claim = claim, context = context, y = data["reliability"])

def input_parser():
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--test_dataset_type", type = str)
    
    parser.add_argument("--advisor_model_id", type = str, default="FacebookAI/roberta-large")
    
    parser.add_argument("--llm_model_id", type = str, default="llama3:8b")
    parser.add_argument("--seed", type = int, default=46)
    parser.add_argument("--temperature", type = float, default=0.2)
    parser.add_argument("--repetition_penalty", type = float, default=1.2)
    parser.add_argument("--use_ollama", action="store_true")
    parser.add_argument("--network_ollama", action="store_true")
    parser.add_argument("--ollama_api_address", type = str, default="192.168.2.146")
    
    parser.add_argument("--advisor_model_dir", type = str, default = "pretrained_advisor_model")
    parser.add_argument("--dataset_dir", type = str, default = "datasets")
    parser.add_argument("--result_dir", type = str, default = "datasets/results/")
    
    parser.add_argument("--evidence_db_ip", type = str, default="localhost")
    parser.add_argument("--evidence_db_port", type = str, default="3000")
    
    parser.add_argument("--n_batch", type = int)
    parser.add_argument("--batch_no", type = int)

    args = parser.parse_args()
    
    config = {
        "test_dataset_type": args.test_dataset_type,
        "llm_model_id": args.llm_model_id,
        "seed": args.seed,
        "temperature": args.temperature,
        "repetition_penalty": args.repetition_penalty,
        "use_ollama": args.use_ollama,
        "network_ollama": args.network_ollama,
        "ollama_api_address": args.ollama_api_address,
        "dataset_dir": args.dataset_dir,
        "result_dir": args.result_dir,
        "n_batch": args.n_batch,
        "batch_no": args.batch_no,
        "advisor_model_id": args.advisor_model_id,
        "advisor_model_dir": args.advisor_model_dir,
        "evidence_db_ip": args.evidence_db_ip,
        "evidence_db_port": args.evidence_db_port,
        "max_length": 512,
    }
    
    return config

if __name__ == "__main__": 
    
    config = input_parser()
    
    print("Training Hyperparameters")
    
    table_hyperparameter = PrettyTable()
    table_hyperparameter.field_names = ["parameters", "value"]
    for key, val in config.items():
        table_hyperparameter.add_row([key, val])
        
    print(table_hyperparameter)
    
    llm_runtime = CovidEfnd(
        config = config
    )
    llm_runtime.runtime_database()