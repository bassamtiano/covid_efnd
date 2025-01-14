import re

import torch
import spacy

from sentence_transformers import CrossEncoder, SentenceTransformer
from sentence_transformers import util as stc_util
from utils.entailment import Entailment

class ResponseParser():
    def __init__(self) -> None:
        self.nlp_en = spacy.load("en_core_web_lg")
        self.nlp_en.add_pipe("sentencizer")
        
        self.entailment_function = Entailment()
        self.passage_ranker = CrossEncoder(
            "sentence-transformers/all-mpnet-base-v2",
            max_length = 512,
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu"),
        )
        self.local_search_embedder = SentenceTransformer(
            "sentence-transformers/multi-qa-mpnet-base-dot-v1",
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu"),
        )
    
    def cut_paragraph(self,
                      paragraphs,
                      max_sentences = 10):
        
        text = self.nlp_en(paragraphs)
        text = [sent.text.strip() for sent in text.sents]
        text = text[:max_sentences]
        text = " ".join(text)
        return text
    
    def generalization_parser(self,
                              title,
                              article,
                              responses):
        
        responses = responses.split("\n")
        
        status = ""
        gen_title = ""
        gen_article = ""
        
        for gen_r in responses:
            
            gen_r = gen_r.strip()
            gen_r = re.sub(r"\d+. ", "", gen_r)
            gen_r = re.sub(r" +", " ", gen_r)
            
            if "Title:" in gen_r:
                status = "title"
            elif "Article:" in gen_r:
                status = "article"
                
            if status == "title":
                gen_title += gen_r
            elif status == "article":
                gen_article += gen_r
        
        gen_title = gen_title.replace("Generalized Title:", "").strip()
        gen_article = gen_article.replace("Generalized Article:", "").strip()
        
        gen_article = self.entailment_function.clean_entailment(sentences = gen_article)
        
        score_context_sum = self.passage_ranker.predict((self.cut_paragraph(paragraphs = article), gen_article))
        
        if title == "":
            score_title_gen = self.passage_ranker.predict((self.cut_paragraph(paragraphs = article), gen_title))
        else:    
            score_title_gen = self.passage_ranker.predict((title, gen_title))
        
        return gen_title, gen_article, score_title_gen, score_context_sum
        
    def queries_parser(self, 
                       response, 
                       claim, 
                       context):
        queries = []
        response = response.split("\n")
        
        for c_resp in response:
            if len(c_resp) > 1:
                if c_resp[0].isdigit() or c_resp[1].isdigit():
                    query = re.sub(r"\[\d+\]. ", "", c_resp)
                    query = re.sub(r"\d+. ", "", query)
                    query = re.sub(r"\[", "", query)
                    queries.append(query)
        
        queries_embedding = self.local_search_embedder.encode(queries, convert_to_tensor = True)
        claim_embedding = self.local_search_embedder.encode(f"{claim} {context}", convert_to_tensor = True)
        
        queries_rank = stc_util.semantic_search(claim_embedding, queries_embedding, top_k = 5)
        ranked_queries = []
        for q_rank in queries_rank[0]:
            ranked_queries.append({
                "query" : queries[q_rank["corpus_id"]],
                "query_score" : q_rank["score"],
            })
        
        return ranked_queries
    
    def dirty_evidence_parser(self, c_evid):
        for c in c_evid:
            c = c.strip()
            c =  re.sub(r"^\s+", " ", c)
            c = c.lower()
            if "not fake" in c:
                pred_label = [0, 1, 0]
                break
            elif "fake" in c:
                pred_label = [1, 0, 0]
                break
            elif "not real" in c:
                pred_label = [1, 0, 0]
                break
            elif "real" in c:
                pred_label = [0, 1, 0]
                break
            elif "undecided" in c:
                pred_label = [0, 0, 1]
                break
            else:
                pred_label = [0, 0, 1]
                break
        
        return pred_label
    
    def evidence_compiler_parser(self, c_evid):
        c_evid = c_evid.split("\n")
        pred_label = []
        
        for c in c_evid:
            c = c.strip()
            c =  re.sub(r"^\s+", " ", c)
            if "the claim is" in c.lower() or "the news is" in c.lower() or "the claim appears to be" in c.lower() or "the news appears to be" in c.lower() or "claim to be" in c.lower(): 
                if "not fake" in c.lower():
                    pred_label = [0, 1, 0]
                elif "fake" in c.lower():
                    pred_label = [1, 0, 0]
                elif "**fake**" in c.lower():
                    pred_label = [1, 0, 0]
                elif "not real" in c.lower():
                    pred_label = [1, 0, 0]
                elif "false" in c.lower():
                    pred_label = [1, 0, 0]
                elif "real" in c.lower():
                    pred_label = [0, 1, 0]
                elif "**real**" in c.lower():
                    pred_label = [0, 1, 0]
                elif "true" in c.lower():
                    pred_label = [0, 1, 0]
                elif "undecided" in c.lower():
                    pred_label = [0, 0, 1]
                else:
                    pred_label = [0, 0, 1]
            elif "**real**" in c.lower() and "**fake**" not in c.lower():
                pred_label = [0, 1, 0]
            elif "**fake**" in c.lower() and "**real**" not in c.lower():
                pred_label = [1, 0, 0]
        
        if pred_label == [] and len(pred_label) < 1:
            pred_label = self.dirty_evidence_parser(c_evid = c_evid)
        
        return pred_label