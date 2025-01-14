import os
import sys

import json
import pandas as pd

import torch
from torch.utils.data import TensorDataset, DataLoader

from transformers import AutoTokenizer
from utils.response_parser import ResponseParser

from pprint import pprint
from tqdm import tqdm

class TrainerPreprocessor():
    def __init__(self, 
                 model_id,
                 max_length,
                 batch_size,
                 test_dataset_type):
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.max_length = max_length
        self.batch_size = batch_size
        
        self.response_parser = ResponseParser()
        self.test_dataset_type = test_dataset_type 
    
    def preprocessor(self, datasets, data_type):
        
        if not os.path.exists(f"datasets/preprocessed/test_{self.test_dataset_type}/{data_type}.pt"):
            prep_data = {
                "claim_ids" : [],
                "claim_att" : [],
                "db_evid_ids" : [],
                "db_evid_att" : [],
                "cs_evid_ids" : [],
                "cs_evid_att" : [],
                "tx_evid_ids" : [],
                "tx_evid_att" : [],
                "y" : [],
                "db_pred" : [],
                "db_acc" : [],
                "cs_pred" : [],
                "cs_acc" : [],
                "tx_pred" : [],
                "tx_acc" : [],
            }
            
            for i_data, data in enumerate(tqdm(datasets)):
                claim = data["claim"]
                context = data["context"]
                
                if len(data["db_evidence"]) > 0:
                    db_evidence = data["db_evidence"][0]["summary"]
                else:
                    data["db_evidence"] = data["rationale_evidence"][0]["summary"]
                
                for i_all_evid, rat_evid in enumerate(data["rationale_evidence"]):
                    if rat_evid["source"] == "commonsense":
                        commonsense_evidence = rat_evid["summary"]
                    elif rat_evid["source"] == "textual description":
                        textual_evidence = rat_evid["summary"]
                
                prep_data["db_pred"].append(data["db_pred"])
                prep_data["db_acc"].append(data["db_acc"])
                prep_data["cs_pred"].append(data["cs_pred"])
                prep_data["cs_acc"].append(data["cs_acc"])
                prep_data["tx_pred"].append(data["tx_pred"])
                prep_data["tx_acc"].append(data["tx_acc"])
                
                y_target = data["real_label"]
                # db_evid_pred = self.response_parser.evidence_compiler_parser(c_evid = db_evidence)
                # cs_evid_pred = self.response_parser.evidence_compiler_parser(c_evid = commonsense_evidence)
                # tx_evid_pred = self.response_parser.evidence_compiler_parser(c_evid = textual_evidence)
                
                prep_data["y"].append(y_target)
                # y_db.append(db_evid_pred)
                # y_cs.append(cs_evid_pred)
                # y_tx.append(tx_evid_pred)
                
                claim_tok = self.tokenizer(
                    f"{claim} {context}",
                    truncation = True,
                    max_length = self.max_length,
                    padding = "max_length"
                )
                prep_data["claim_ids"].append(claim_tok["input_ids"])
                prep_data["claim_att"].append(claim_tok["attention_mask"])
                
                db_evid_tok = self.tokenizer(
                    db_evidence,
                    truncation = True,
                    max_length = self.max_length,
                    padding = "max_length"
                )
                
                prep_data["db_evid_ids"].append(db_evid_tok["input_ids"])
                prep_data["db_evid_att"].append(db_evid_tok["attention_mask"])
                
                cs_evid_tok = self.tokenizer(
                    commonsense_evidence,
                    truncation = True,
                    max_length = self.max_length,
                    padding = "max_length"
                )
                
                prep_data["cs_evid_ids"].append(cs_evid_tok["input_ids"])
                prep_data["cs_evid_att"].append(cs_evid_tok["attention_mask"])
                
                tx_evid_tok = self.tokenizer(
                    textual_evidence,
                    truncation = True,
                    max_length = self.max_length,
                    padding = "max_length"
                )
                
                prep_data["tx_evid_ids"].append(tx_evid_tok["input_ids"])
                prep_data["tx_evid_att"].append(tx_evid_tok["attention_mask"])
                
            prep_data["claim_ids"] = torch.tensor(prep_data["claim_ids"])
            prep_data["claim_att"] = torch.tensor(prep_data["claim_att"])
            prep_data["db_evid_ids"] = torch.tensor(prep_data["db_evid_ids"])
            prep_data["db_evid_att"] = torch.tensor(prep_data["db_evid_att"])
            prep_data["cs_evid_ids"] = torch.tensor(prep_data["cs_evid_ids"])
            prep_data["cs_evid_att"] = torch.tensor(prep_data["cs_evid_att"])
            prep_data["tx_evid_ids"] = torch.tensor(prep_data["tx_evid_ids"])
            prep_data["tx_evid_att"] = torch.tensor(prep_data["tx_evid_att"])
            
            prep_data["db_pred"] = torch.tensor(prep_data["db_pred"])
            prep_data["db_acc"] = torch.tensor(prep_data["db_acc"])
            prep_data["cs_pred"] = torch.tensor(prep_data["cs_pred"])
            prep_data["cs_acc"] = torch.tensor(prep_data["cs_acc"])
            prep_data["tx_pred"] = torch.tensor(prep_data["tx_pred"])
            prep_data["tx_acc"] = torch.tensor(prep_data["tx_acc"])
            
            prep_data["y"] = torch.tensor(prep_data["y"])
            
            tensor_data = TensorDataset(
                prep_data["claim_ids"],
                prep_data["claim_att"],
                prep_data["db_evid_ids"],
                prep_data["db_evid_att"],
                prep_data["cs_evid_ids"],
                prep_data["cs_evid_att"],
                prep_data["tx_evid_ids"],
                prep_data["tx_evid_att"],
                prep_data["y"],
                prep_data["db_pred"],
                prep_data["db_acc"],
                prep_data["cs_pred"],
                prep_data["cs_acc"],
                prep_data["tx_pred"],
                prep_data["tx_acc"],
            )
            
            if data_type == "train":
                print("Build Train Data")
                train_len = int(prep_data["claim_ids"].shape[0] * 0.9)
                val_len = prep_data["claim_ids"].shape[0] - train_len
                
                self.train_data, self.val_data = torch.utils.data.random_split(tensor_data, [train_len, val_len])
                torch.save(self.train_data, f"datasets/preprocessed/test_{self.test_dataset_type}/train.pt")
                torch.save(self.val_data, f"datasets/preprocessed/test_{self.test_dataset_type}/val.pt")
            else:
                print("Build Test Data")
                test_data = tensor_data
                self.test_data = test_data
                torch.save(self.test_data, f"datasets/preprocessed/test_{self.test_dataset_type}/test.pt")

        else:
            print("Load Preprocessed Data")
            if data_type == "train":
                self.train_data = torch.load(f"datasets/preprocessed/test_{self.test_dataset_type}/train.pt")
                self.val_data = torch.load(f"datasets/preprocessed/test_{self.test_dataset_type}/val.pt")
            else:
                print("load test data")
                self.test_data = torch.load(f"datasets/preprocessed/test_{self.test_dataset_type}/test.pt")
            
        
    def train_dataloader(self):
        return DataLoader(
            dataset = self.train_data,
            batch_size = self.batch_size,
            shuffle = True,
            num_workers = 3,
        )
        
    def val_dataloader(self):
        return DataLoader(
            dataset = self.val_data,
            batch_size = self.batch_size,
            shuffle = False,
            num_workers = 3,
        )
        
    def test_dataloader(self):
        return DataLoader(
            dataset = self.test_data,
            batch_size = self.batch_size,
            shuffle = False,
            num_workers = 3,
        )