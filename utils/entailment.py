import sys
import re
import math

import torch
import torch.nn as nn

import pandas as pd
import spacy

from transformers import AutoModel, AutoTokenizer, AutoModelForSequenceClassification
from sentence_transformers import SentenceTransformer, util


class Entailment():
    def __init__(self,
                 max_length = 512):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.max_length = max_length
        
        self.spacy_nlp = spacy.load("en_core_web_lg")
        self.spacy_nlp.add_pipe("sentencizer")
        
        self.prepare_lm()
        
    def prepare_lm(self):
        # docnli_model_name = "MoritzLaurer/DeBERTa-v3-base-mnli-fever-docnli-ling-2c"
        # docnli_model_name = "microsoft/deberta-large-mnli"
        # docnli_model_name = "microsoft/deberta-v2-xxlarge"
        docnli_model_name = "MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli"
        # docnli_model_name = "google/t5_xxl_true_nli_mixture"
        # docnli_model_name = "FacebookAI/roberta-large-mnli"
        self.model_docnli = AutoModelForSequenceClassification.from_pretrained(docnli_model_name).requires_grad_(False)
        self.model_docnli.to(self.device)
        self.tokenizer_docnli = AutoTokenizer.from_pretrained(docnli_model_name)
        
    def entailment_pair(self, sentence_1, sentence_2):
        
        entail_input = self.tokenizer_docnli(sentence_1, sentence_2, truncation = True, max_length = self.max_length, padding = "max_length", return_tensors = "pt").to(self.device)
        entail_output = self.model_docnli(**entail_input)
        prediction = torch.softmax(entail_output["logits"][0], -1).tolist()
        label_names = ["entailment", "not_entailment"]
        prediction = {name: round(float(pred) * 100, 1) for pred, name in zip(prediction, label_names)}
        return prediction
    
    def clean_entailment(self, sentences):
        entailment_score_matrix = []
        
        sentences = self.spacy_nlp(sentences)
        sentences = [sent.text.strip() for sent in sentences.sents]
        
        for i in range(len(sentences)):
            temp = []
            for j in range(len(sentences)):
                temp.append(f"{i}:{j}")
            entailment_score_matrix.append(temp)
        
        entailed_pair = []
        non_entailed_pair = []
        for i_sum1, sum1 in enumerate(sentences):
            for i_sum2, sum2 in enumerate(sentences):
                prediction = self.entailment_pair(sentence_1 = sum1, sentence_2 = sum2)
                
                prediction["index"] = [i_sum1, i_sum2]
                entailment_score_matrix[i_sum1][i_sum2] = prediction
                
                if i_sum1 != i_sum2:
                    if prediction["entailment"] > prediction["not_entailment"]:
                        entailed_pair.append(prediction["index"])
                    
                    elif prediction["entailment"] < prediction["not_entailment"]:
                        non_entailed_pair.append(prediction["index"])
        
        non_entailed_index = list(set([i for i, j in non_entailed_pair]))
        
        post_entailed_index = []
        entailed_index = []
        for e_pair in entailed_pair:
            if e_pair not in post_entailed_index and [e_pair[1], e_pair[0]] not in post_entailed_index:
                post_entailed_index.append(e_pair)
                entailed_index.append(e_pair[0])
                entailed_index.append(e_pair[1])
        
        non_entailed_index = [ne_p for ne_p in non_entailed_index if ne_p not in entailed_index]
        post_entailed_index = [cl_e[0] for cl_e in post_entailed_index]
        non_entailed_index += post_entailed_index
        non_entailed_index = sorted(non_entailed_index)
        
        non_entailed_sum = []
        for i_nep in non_entailed_index:
            non_entailed_sum.append(sentences[i_nep])
        
        non_entailed_sum = " ".join(non_entailed_sum)
        return non_entailed_sum