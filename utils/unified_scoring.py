import sys
import torch

from statistics import mean 

import numpy as np

from evaluate import load as evaluate_load

from sklearn.metrics import precision_recall_fscore_support, accuracy_score, roc_auc_score
from sklearn.metrics import classification_report

from transformers import pipeline

class UnifiedScoring():
    def __init__(self):
        self.mauve_scorer = evaluate_load('mauve')
        self.bert_scorer = evaluate_load('bertscore')
        self.chrf_scorer = evaluate_load('chrf')
        
    def factcc_scorer(self, predictions, referemces):
        input_scores = [[[pr, rf]] for pr, rf in zip(predictions, referemces)]
        pipe = pipeline(model = "manueldeprada/FactCC")
        factcc_score = pipe(
            input_scores,
            truncation = True,
            padding='max_length',
            max_length = 512
        )
        factcc_score = mean([fcc["score"] for fcc in factcc_score])
        return factcc_score
    
    def generation_quality_metrics(self, llm_pred, ref):
        test_score = {
            "mauve_score": 0,
            "bert_precision_score": 0,
            "bert_recall_score": 0,
            "bert_f1_score": 0,
            "chr_f_score": 0,
            "factcc_score": 0,
            "similarity_score": 0
        }
        
        test_score["mauve_score"] = self.mauve_scorer.compute(
            predictions = llm_pred,
            references = ref
        ).mauve
        
        bert_scores = self.bert_scorer.compute(
            predictions = llm_pred,
            references = ref,
            lang = "en"    
        )
        
        test_score["bert_precision_score"] = mean(bert_scores["precision"])
        test_score["bert_recall_score"] = mean(bert_scores["recall"])
        test_score["bert_f1_score"] = mean(bert_scores["f1"])
        
        test_score["chr_f_score"] = self.chrf_scorer.compute(
            predictions = llm_pred,
            references = ref
        )["score"]
        
        factcc_scores = self.factcc_scorer(
            predictions = llm_pred,
            referemces = ref
        )
        test_score["factcc_score"] = factcc_scores
        
        return test_score
        
    def classification_scoring_metrics(self, y_pred, y_true):
        test_scores = {
            "correct" : 0,
            "unknown" : 0,
            "incorrect" : 0,
            "loss": 0,
            "precission_macro" : 0,
            "recall_macro" : 0,
            "f1_macro" : 0,
            "precission_micro" : 0,
            "recall_micro" : 0,
            "f1_micro" : 0,
            "precission_weighted" : 0,
            "recall_weighted" : 0,
            "f1_weighted" : 0,
            "accuracy" : 0,
            "accuracy_manual" : 0,
            "auc": 0,
            "spauc": 0,
            "precision_fake": 0,
            "recall_fake": 0,
            "f1_fake": 0,
            "support_fake": 0,
            "precision_real": 0,
            "recall_real": 0,
            "f1_real": 0,
            "support_real": 0,
        }
        
        try:
            test_scores['auc'] = roc_auc_score(y_true, y_pred, average='macro')
        except ValueError:
            test_scores['auc'] = -1
        try:
            test_scores['spauc'] = roc_auc_score(y_true, y_pred, average='macro', max_fpr=0.1)
        except ValueError:
            test_scores['spauc'] = -1
        
        y_pred = np.around(np.array(y_pred)).astype(int)
        
        results_macro = precision_recall_fscore_support(y_true, y_pred, average='macro')
        results_micro = precision_recall_fscore_support(y_true, y_pred, average='micro')
        results_weighted = precision_recall_fscore_support(y_true, y_pred, average='weighted')
        result_accuracy = accuracy_score(y_true, y_pred)
        
        classification_labels = ["fake", "real"]
        result_labels = classification_report(y_true, y_pred, target_names = classification_labels, output_dict = True)
        
        test_scores["precission_macro"] = results_macro[0]
        test_scores["recall_macro"] = results_macro[1]
        test_scores["f1_macro"] = results_macro[2]
        
        test_scores["precission_micro"] = results_micro[0]
        test_scores["recall_micro"] = results_micro[1]
        test_scores["f1_micro"] = results_micro[2]
        
        test_scores["precission_weighted"] = results_weighted[0]
        test_scores["recall_weighted"] = results_weighted[1]
        test_scores["f1_weighted"] = results_weighted[2]
        
        test_scores["precision_fake"] = result_labels["fake"]["precision"]
        test_scores["recall_fake"] = result_labels["fake"]["recall"]
        test_scores["f1_fake"] = result_labels["fake"]["f1-score"]
        test_scores["support_fake"] = result_labels["fake"]["support"]
        
        test_scores["precision_real"] = result_labels["real"]["precision"]
        test_scores["recall_real"] = result_labels["real"]["recall"]
        test_scores["f1_real"] = result_labels["real"]["f1-score"]
        test_scores["support_real"] = result_labels["real"]["support"]
        
        test_scores["accuracy"] = result_accuracy
        
        return test_scores