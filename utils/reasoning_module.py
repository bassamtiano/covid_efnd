import sys
import re

import torch

from sentence_transformers import SentenceTransformer
from sentence_transformers import util as stc_util

from models.llm_runtime import LLMRuntime
from utils.response_parser import ResponseParser
# from utils.entailment import Entailment

from utils.prompt.llama3_prompt_template import *
# from utils.prompt.mistral_prompt_template import *

class ReasoningModule(LLMRuntime):
    def __init__(self, config):
        super(ReasoningModule, self).__init__(
            model_id = config['llm_model_id'], 
            seed = config['seed'],
            temperature = config['temperature'],
            repetition_penalty = config['repetition_penalty'],
            use_ollama = config['use_ollama'],
            network_ollama = config['network_ollama'],
            ollama_api_address = config['ollama_api_address']
        )
        self.llm_model_id = config['llm_model_id']
        
        self.response_parser = ResponseParser()
        # self.entail_score = Entailment()
        self.local_search_embedder = SentenceTransformer(
            "sentence-transformers/multi-qa-mpnet-base-dot-v1",
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu"),
        )

    def generalization_generation(self, title, article):
        if str(title) == "nan": title = ""
        if str(article) == "nan": article = ""
        
        article = self.response_parser.cut_paragraph(paragraphs = article)
        
        if "mistral" in self.llm_model_id: 
            generalization_prompt = MISTRAL_GENERALIZATION_PROMPT.format(
                title = title,
                article = article
            )
        elif "llama3" in self.llm_model_id:
            generalization_prompt = LLAMA3_GENERALIZATION_PROMPT.format(
                title = title,
                article = article
            )
        
        generalization_responses = self.generate_response(prompt = generalization_prompt)
        gen_title, gen_article, score_title_gen, score_context_sum = self.response_parser.generalization_parser(
            responses = generalization_responses,
            title = title,
            article = article,
        )
        
        return {"claim": gen_title, "context": gen_article, "claim_score": score_title_gen, "context_score": score_context_sum}

      
    def query_generation(self, claim, context = None):
        
        if context != None:
            generalized = self.generalization_generation(title = claim, article = context)
            
            if "mistral" in self.llm_model_id:
                query_prompt = MISTRAL_CONTEXT_QUERY_GENERATION_PROMPT.format(
                    context = generalized["context"],
                    claim = claim
                )
            elif "llama3" in self.llm_model_id:
                query_prompt = LLAMA3_CONTEXT_QUERY_GENERATION_PROMPT.format(
                    context = generalized["context"],
                    claim = claim
                )
        else:
            if "mistral" in self.llm_model_id:
                pass
            elif "llama3" in self.llm_model_id:
                query_prompt = LLAMA3_QUERY_GENERATION_PROMPT.format(
                    claim = claim
                )
            
        queries = self.generate_response(prompt = query_prompt)
        queries = self.response_parser.queries_parser(response = queries, claim = claim, context = context) 
        
        if len(queries) < 1:
            return {
                'generalized_claim': str(claim),
                'generalized_context': str(context),
                'queries': [
                    {
                        'query': f"{claim}",
                        'query_score': 1.0
                    }
                ]
            }
        
        if context != None:
            return {"queries": queries, "generalized_claim": generalized["claim"], "generalized_context": generalized["context"]}
        else:
            return {"queries": queries, "generalized_claim": "", "generalized_context": ""}
        
    def rationale_commonsense_runtime(self, claim, context = None):
        if context != None:
            if "mistral" in self.llm_model_id: 
                commonsense_prompt = MISTRAL_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT.format(claim = f"{claim} {context}",)
                textual_prompt = MISTRAL_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT.format(claim = f"{claim} {context}",)
            elif "llama3" in self.llm_model_id:
                commonsense_prompt = LLAMA3_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT_TEMP.format(claim = f"{claim} {context}",)
                textual_prompt = LLAMA3_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT_TEMP.format(claim = f"{claim} {context}",)
        else:
            if "mistral" in self.llm_model_id: 
                commonsense_prompt = MISTRAL_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT.format(claim = claim)
                textual_prompt = MISTRAL_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT.format(claim = claim)
            elif "llama3" in self.llm_model_id:
                commonsense_prompt = LLAMA3_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT_TEMP.format(claim = claim)
                textual_prompt = LLAMA3_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT_TEMP.format(claim = claim)

        commonsense = self.generate_response(commonsense_prompt)
        commonsense_pred = self.response_parser.evidence_compiler_parser(c_evid = commonsense)
        textual = self.generate_response(textual_prompt)
        textual_pred = self.response_parser.evidence_compiler_parser(c_evid = textual)
        
        # textual_entailment_scores = self.entail_score.entailment_pair(sentence_1 = textual, sentence_2 = f"{claim} {context}")
        # commonsense_entailment_scores = self.entail_score.entailment_pair(sentence_1 = commonsense, sentence_2 = f"{claim} {context}")
        
        claim_embedding = self.local_search_embedder.encode(f"{claim} {context}", convert_to_tensor = True)
        
        rationales = [
            {
                "summary": commonsense,
                "url": "commonsense",
                "y_pred": commonsense_pred,
                # "entailment": commonsense_entailment_scores["entailment"],
                # "not_entailment": commonsense_entailment_scores["not_entailment"],
                "source": "commonsense",
            },
            {
                "summary": textual,
                "url": "textual description",
                "y_pred": textual_pred,
                # "entailment": textual_entailment_scores["entailment"],
                # "not_entailment": textual_entailment_scores["not_entailment"],
                "source": "textual description",
            },
        ]
        
        
        rationale_only = [rtl["summary"] for rtl in rationales]
        rationale_embedding = self.local_search_embedder.encode(rationale_only, convert_to_tensor = True)
        
        ranked_rationale = []
        ranked_rationale_idx = stc_util.semantic_search(claim_embedding, rationale_embedding, top_k = 20)
        
        for rank_r in ranked_rationale_idx[0]:
            rat = rationales[rank_r["corpus_id"]]
            rat["similarity"] = rank_r["score"]
            ranked_rationale.append(rat)
            
        return ranked_rationale
    
    
    def rationale_commonsense_guided_runtime(self, claim, advised_label, context = None):
        if context != None:
            if "mistral" in self.llm_model_id: 
                commonsense_prompt = MISTRAL_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT.format(claim = f"{claim} {context}", advised_label = advised_label)
                textual_prompt = MISTRAL_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT.format(claim = f"{claim} {context}", advised_label = advised_label)
            elif "llama3" in self.llm_model_id:
                commonsense_prompt = LLAMA3_ZEROSHOT_COMMON_SENSE_ADVISED_DESCRIPTION_PROMPT_TEMP.format(claim = f"{claim} {context}", advised_label = advised_label)
                textual_prompt = LLAMA3_ZEROSHOT_TEXTUAL_ADVISED_DESCRIPTION_PROMPT_TEMP.format(claim = f"{claim} {context}", advised_label = advised_label)
        else:
            if "mistral" in self.llm_model_id: 
                commonsense_prompt = MISTRAL_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT.format(claim = claim, advised_label = advised_label)
                textual_prompt = MISTRAL_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT.format(claim = claim, advised_label = advised_label)
            elif "llama3" in self.llm_model_id:
                commonsense_prompt = LLAMA3_ZEROSHOT_COMMON_SENSE_ADVISED_DESCRIPTION_PROMPT_TEMP.format(claim = claim, advised_label = advised_label)
                textual_prompt = LLAMA3_ZEROSHOT_TEXTUAL_ADVISED_DESCRIPTION_PROMPT_TEMP.format(claim = claim, advised_label = advised_label)

        commonsense = self.generate_response(commonsense_prompt)
        commonsense_pred = self.response_parser.evidence_compiler_parser(c_evid = commonsense)
        textual = self.generate_response(textual_prompt)
        textual_pred = self.response_parser.evidence_compiler_parser(c_evid = textual)
        
        # textual_entailment_scores = self.entail_score.entailment_pair(sentence_1 = textual, sentence_2 = f"{claim} {context}")
        # commonsense_entailment_scores = self.entail_score.entailment_pair(sentence_1 = commonsense, sentence_2 = f"{claim} {context}")
        
        claim_embedding = self.local_search_embedder.encode(f"{claim} {context}", convert_to_tensor = True)
        
        rationales = [
            {
                "summary": commonsense,
                "url": "commonsense",
                "y_pred": commonsense_pred,
                # "entailment": commonsense_entailment_scores["entailment"],
                # "not_entailment": commonsense_entailment_scores["not_entailment"],
                "source": "commonsense",
            },
            {
                "summary": textual,
                "url": "textual description",
                "y_pred": textual_pred,
                # "entailment": textual_entailment_scores["entailment"],
                # "not_entailment": textual_entailment_scores["not_entailment"],
                "source": "textual description",
            },
        ]
        
        
        rationale_only = [rtl["summary"] for rtl in rationales]
        rationale_embedding = self.local_search_embedder.encode(rationale_only, convert_to_tensor = True)
        
        ranked_rationale = []
        ranked_rationale_idx = stc_util.semantic_search(claim_embedding, rationale_embedding, top_k = 20)
        
        for rank_r in ranked_rationale_idx[0]:
            rat = rationales[rank_r["corpus_id"]]
            rat["similarity"] = rank_r["score"]
            ranked_rationale.append(rat)
            
        return ranked_rationale
    
    
    def evidence_compiler_generation(self, claim, context, query, evidence_url, evidence_text):
        if context != None:
            if "mistral" in self.llm_model_id: 
                evid_compiler_prompt = MISTRAL_EVIDENCE_COMPILER.format(
                    claim = claim,
                    context = context,
                    query = query,
                    evidence_url = evidence_url,
                    evidence_text = evidence_text
                )
            elif "llama3" in self.llm_model_id:
                evid_compiler_prompt = LLAMA3_CONTEXT_EVIDENCE_COMPILER.format(
                    claim = claim,
                    context = context,
                    query = query,
                    evidence_url = evidence_url,
                    evidence_text = evidence_text
                )
        else:
            if "mistral" in self.llm_model_id: 
                evid_compiler_prompt = MISTRAL_EVIDENCE_COMPILER.format(
                    claim = claim,
                    context = context,
                    query = query,
                    evidence_url = evidence_url,
                    evidence_text = evidence_text
                )
            elif "llama3" in self.llm_model_id:
                evid_compiler_prompt = LLAMA3_EVIDENCE_COMPILER.format(
                    claim = claim,
                    context = context,
                    query = query,
                    evidence_url = evidence_url,
                    evidence_text = evidence_text
                )
        
        
        compiled_evidence = self.generate_response(prompt = evid_compiler_prompt)
        pred_label = self.response_parser.evidence_compiler_parser(c_evid = compiled_evidence)
        
        return {"compiled_evidence": compiled_evidence, "pred_label": pred_label}
    
    def evidence_correlation_decider(self, claim, query, evidence):
        if "mistral" in self.llm_model_id: 
            pass
        elif "llama3" in self.llm_model_id:
            evidence_gate_prompt = LLAMA3_CORRELATION_GATE_UPDATE_PROMPT.format(
                claim = claim,
                query = query,
                evidence = evidence
            )
        
        evidence_gate_response = self.generate_response(prompt = evidence_gate_prompt)
        evid_gate = evidence_gate_response.split("\n")

        status = None
        reasoning = ""
        for rp in evid_gate:
            if rp[:2] == "3.":
                reasoning = rp.replace("3. Reasoning:", "")
                reasoning = reasoning.strip()
            if rp[:2] == "4.":
                cor_stat = rp.replace("4. Correlated Status:", "")
                cor_stat = cor_stat.strip()
                
                
                if cor_stat.lower() == "not correlated":
                    status = 0
                elif cor_stat.lower() == "correlated":
                    status = 1
        
        return {
            "correlation_reasoning": reasoning, 
            "correlation_status": status
        }
    
    def evidence_reasoning_generation(self, claim, context):
        if "mistral" in self.llm_model_id: 
            pass
        elif "llama3" in self.llm_model_id:
            common_sense_prompt = LLAMA3_ZEROSHOT_COMMON_SENSE_DESCRIPTION_PROMPT_TEMP.format(
                claim = f"{claim} {context}",
            )
            
            textual_prompt = LLAMA3_ZEROSHOT_TEXTUAL_DESCRIPTION_PROMPT_TEMP.format(
                claim = f"{claim} {context}",
            )
            
        common_sense = self.generate_response(common_sense_prompt)
        textual = self.generate_response(textual_prompt)
        return {
            "common_sense": common_sense,
            "textual_description": textual,
        }