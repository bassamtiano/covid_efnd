import os
import sys
import json

import torch
import spacy

from sentence_transformers import CrossEncoder

# from utils.evidence_db import EvidenceDB
# from utils.entailment import Entailment
from sklearn.metrics import precision_recall_fscore_support, accuracy_score

import numpy as np
from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score, roc_auc_score

from pprint import pprint

class ReasoningToolkit():
    def __init__(self):
        pass

    '''
        Evidence Database
    
    '''
    def scoring_util(self, y_pred, y_true):
        test_scores = {
            "correct" : 0,
            "unknown" : 0,
            "incorrect" : 0,
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
        
        test_scores["precission_macro"] = results_macro[0]
        test_scores["recall_macro"] = results_macro[1]
        test_scores["f1_macro"] = results_macro[2]
        
        test_scores["precission_micro"] = results_micro[0]
        test_scores["recall_micro"] = results_micro[1]
        test_scores["f1_micro"] = results_micro[2]
        
        test_scores["precission_weighted"] = results_weighted[0]
        test_scores["recall_weighted"] = results_weighted[1]
        test_scores["f1_weighted"] = results_weighted[2]
        
        all_pair_predicted = {
            "true": y_pred.tolist(),
            "pred": y_pred.tolist(),
        }
        
        test_scores["accuracy"] = result_accuracy
        return test_scores, all_pair_predicted
    
    # def scoring_util(self, y_pred, y_true):
    #     all_metrics = {}

    #     try:
    #         all_metrics['auc'] = roc_auc_score(y_true, y_pred, average='macro')
    #     except ValueError:
    #         all_metrics['auc'] = -1
    #     try:
    #         all_metrics['spauc'] = roc_auc_score(y_true, y_pred, average='macro', max_fpr=0.1)
    #     except ValueError:
    #         all_metrics['spauc'] = -1
    #     y_pred = np.around(np.array(y_pred)).astype(int)
    #     all_metrics['metric'] = f1_score(y_true, y_pred, average='macro')
    #     try:
    #         all_metrics['f1_real'], all_metrics['f1_fake'] = f1_score(y_true, y_pred, average=None)
    #     except ValueError:
    #         all_metrics['f1_real'], all_metrics['f1_fake'] = -1, -1
    #     all_metrics['recall'] = recall_score(y_true, y_pred, average='macro')
    #     try:
    #         all_metrics['recall_real'], all_metrics['recall_fake'] = recall_score(y_true, y_pred, average=None)
    #     except ValueError:
    #         all_metrics['recall_real'], all_metrics['recall_fake'] = -1, -1
    #     all_metrics['precision'] = precision_score(y_true, y_pred, average='macro')
    #     try:
    #         all_metrics['precision_real'], all_metrics['precision_fake'] = precision_score(y_true, y_pred, average=None)
    #     except ValueError:
    #         all_metrics['precision_real'], all_metrics['precision_fake']= -1, -1
    #     all_metrics['acc'] = accuracy_score(y_true, y_pred)
        
    #     return all_metrics