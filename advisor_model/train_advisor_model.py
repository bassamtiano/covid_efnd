import sys
import os
import json
import statistics
import argparse

os.environ["TOKENIZERS_PARALLELISM"] = "false"


import torch
import pandas as pd
import numpy as np

from tqdm import tqdm

from models.advisor_model import AdvisorModel

from fake_reasoning_commonsense_textual_evidence_chooser import FakeReasoningEntailment
from utils.trainer_preprocessor import TrainerPreprocessor

from trainer_preprocessor import TrainerPreprocessor
from utils.reasoning_toolkit import ReasoningToolkit

from pprint import pprint
from prettytable import PrettyTable

from utils.unified_scoring import UnifiedScoring

from transformers import get_cosine_schedule_with_warmup

class TrainAdvisorModel(TrainerPreprocessor):
    def __init__(self, config):
        super(TrainAdvisorModel, self).__init__(
            model_id = config["model_id"],
            max_length = config["max_length"],
            batch_size = config["batch_size"],
            test_dataset_type = config["test_dataset_type"],
        )
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.config = config
        
        self.unified_score = UnifiedScoring()
        self.reasoning_toolkit = ReasoningToolkit()
        self.random_seed()
        
        self.advisor_model = AdvisorModel(
            model_id = config["model_id"],
            batch_size = config["batch_size"]
        )
        self.advisor_model.to(self.device)
        
        self.test_dataset_type = config["test_dataset_type"]
        self.available_datasets = ["mmcovar", "recovery", "mm_covid"]
        
        self.current_epoch = 0
        
        self.generated_fake_reasoning_dir = "datasets/advisor_data_{data_type}.json".strip()
        
        self.loss_fn = torch.nn.BCELoss()
        self.loss_hard_rat_aux_fn = torch.nn.BCELoss()
        self.loss_hard_db_aux_fn = torch.nn.BCELoss()
        
        self.loss_simple_rat_aux_fn = torch.nn.CrossEntropyLoss()
        self.loss_simple_db_aux_fn = torch.nn.CrossEntropyLoss()
        
        self.optimizer = torch.optim.Adam(
            params = self.advisor_model.parameters(), 
            lr = self.config["lr"], 
            weight_decay = self.config["weight_decay"]
        )
        
    def scoring_step(self, y_true, y_pred, step_status, loss = 0):        
        classification_score = self.unified_score.classification_scoring_metrics(
            y_pred = y_pred,
            y_true = y_true
        )
        classification_score['loss'] = loss
        
        classification_dir_save = f"results/{self.config['test_dataset_type']}/{step_status}_{self.current_epoch}_classification.json"
        with open(classification_dir_save, "w") as cl_json_w:
            json.dump(classification_score, cl_json_w, indent = 4)
        
        table_classification = PrettyTable()
        table_classification.field_names = ["method", "score"]
        for key, val in classification_score.items():
            table_classification.add_row([key, val])
        print(table_classification)
        
        return classification_score
    
    def random_seed(self):
        torch.manual_seed(self.config["seed"])
        torch.cuda.manual_seed(self.config["seed"])
        torch.cuda.manual_seed_all(self.config["seed"])
        torch.backends.cudnn.deterministic = True
    
    def prepare_data(self, ):
        self.available_datasets.remove(self.config["test_dataset_type"])
        
        train_datasets = []
        for train_d_type in self.available_datasets:
            data_dir = self.generated_fake_reasoning_dir.format(data_type = train_d_type)
            with open(data_dir, "r") as json_r:
                train_datasets.extend(json.load(json_r))
        
        print("Training Data")
        print("-"*50)
        print(self.available_datasets)
        print(len(train_datasets))
        self.preprocessor(datasets = train_datasets, data_type = "train")
        
        test_data_dir = self.generated_fake_reasoning_dir.format(data_type = self.test_dataset_type)
        with open(test_data_dir, "r") as json_r:
            test_datasets = json.load(json_r)
        
        print("Testing Data")
        print("-"*50)
        print(test_data_dir)
        print(len(test_datasets))

        self.preprocessor(datasets = test_datasets, data_type = "test")
        
    def train_step(self,):
        y_pred = []
        y_true = []
        avg_loss = []
        
        self.advisor_model.train()
        
        iters = len(self.train_dataloader())
        for i_batch, batch in enumerate(tqdm(self.train_dataloader(), desc = f"Training Step | Epoch : {self.current_epoch}")):
            batch = [b.to(self.device) for b in batch]
            
            claim_ids = batch[0]
            claim_att = batch[1]
            db_evid_ids = batch[2]
            db_evid_att = batch[3]
            cs_evid_ids = batch[4]
            cs_evid_att = batch[5]
            tx_evid_ids = batch[6]
            tx_evid_att = batch[7]
            y = batch[8]
            db_pred = batch[9]
            db_acc = batch[10]
            cs_pred = batch[11]
            cs_acc = batch[12]
            tx_pred = batch[13]
            tx_acc = batch[14]
            
            y_lbl = torch.argmax(y, dim = 1)
            
            res = self.advisor_model(claim_ids, claim_att, db_evid_ids, db_evid_att, cs_evid_ids, cs_evid_att, tx_evid_ids, tx_evid_att)
            loss_classify = self.loss_fn(res["classify_pred"], y_lbl.float())
            
            # Hard predict only if the prediction of label correct to grand truth or not
            loss_hard_rationale_aux = self.loss_hard_rat_aux_fn(res["hard_feature_2_pred"], cs_acc.float()) + self.loss_hard_rat_aux_fn(res["hard_feature_3_pred"], tx_acc.float())
            loss_hard_db_aux = self.loss_hard_db_aux_fn(res["hard_feature_1_pred"], db_acc.float())
            
            # Simple calculate the loss of llm prediction with grand truth
            loss_simple_rat_aux = self.loss_simple_rat_aux_fn(res["simple_feature_2_pred"], cs_pred.long()) + self.loss_simple_rat_aux_fn(res["simple_feature_3_pred"], tx_pred.long())
            loss_simple_db_aux = self.loss_simple_db_aux_fn(res["simple_feature_1_pred"], db_pred.long())
            
            loss = loss_classify
            loss += self.config["rationale_usefulness_weight"] * loss_hard_rationale_aux / 2
            loss += self.config["db_usefulnewss_weight"] + loss_hard_db_aux
            
            loss += self.config["rationale_judgement_weight"] * loss_simple_rat_aux / 2
            loss += self.config["db_judgement_weight"] + loss_simple_db_aux
            
            avg_loss.append(loss.item())
            
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()
            # self.scheduler.step(self.current_epoch + i_batch / iters)
            self.scheduler.step()
            
            y_pred.extend(res["classify_pred"].detach().cpu().tolist())
            y_true.extend(y_lbl.cpu().tolist())
            
        avg_loss = statistics.mean(avg_loss)
        # metrics, _ = self.reasoning_toolkit.scoring_util(y_pred = y_pred, y_true = y_true)
        metrics = self.scoring_step(y_true = y_true, y_pred = y_pred, step_status = "training", loss = avg_loss)
        return metrics
    
    def val_step(self):
        self.advisor_model.eval()
        
        y_pred = []
        y_true = []
        avg_loss = []
        
        
        
        with torch.no_grad():
            for i_batch, batch in enumerate(tqdm(self.val_dataloader(), desc = f"Validation Step | Epoch : {self.current_epoch}")):
                batch = [b.to(self.device) for b in batch]
            
                claim_ids = batch[0]
                claim_att = batch[1]
                db_evid_ids = batch[2]
                db_evid_att = batch[3]
                cs_evid_ids = batch[4]
                cs_evid_att = batch[5]
                tx_evid_ids = batch[6]
                tx_evid_att = batch[7]
                y = batch[8]
                db_pred = batch[9]
                db_acc = batch[10]
                cs_pred = batch[11]
                cs_acc = batch[12]
                tx_pred = batch[13]
                tx_acc = batch[14]
                
                y_lbl = torch.argmax(y, dim = 1)
                
                res = self.advisor_model(claim_ids, claim_att, db_evid_ids, db_evid_att, cs_evid_ids, cs_evid_att, tx_evid_ids, tx_evid_att)
                loss_classify = self.loss_fn(res["classify_pred"], y_lbl.float())
                
                # Hard predict only if the prediction of label correct to grand truth or not
                loss_hard_rationale_aux = self.loss_hard_rat_aux_fn(res["hard_feature_2_pred"], cs_acc.float()) + self.loss_hard_rat_aux_fn(res["hard_feature_3_pred"], tx_acc.float())
                loss_hard_db_aux = self.loss_hard_db_aux_fn(res["hard_feature_1_pred"], db_acc.float())
                
                # Simple calculate the loss of llm prediction with grand truth
                loss_simple_rat_aux = self.loss_simple_rat_aux_fn(res["simple_feature_2_pred"], cs_pred.long()) + self.loss_simple_rat_aux_fn(res["simple_feature_3_pred"], tx_pred.long())
                loss_simple_db_aux = self.loss_simple_db_aux_fn(res["simple_feature_1_pred"], db_pred.long())
                
                loss = loss_classify
                loss += self.config["rationale_usefulness_weight"] * loss_hard_rationale_aux / 2
                loss += self.config["db_usefulnewss_weight"] + loss_hard_db_aux
                
                loss += self.config["rationale_judgement_weight"] * loss_simple_rat_aux / 2
                loss += self.config["db_judgement_weight"] + loss_simple_db_aux
                
                avg_loss.append(loss.item())
                
                y_pred += res["classify_pred"].detach().cpu().tolist()
                y_true += y_lbl.cpu().tolist()
        
        
        avg_loss = statistics.mean(avg_loss)
        
        y_pred = np.around(np.array(y_pred)).astype(int).tolist()
        metrics = self.scoring_step(y_true = y_true, y_pred = y_pred, step_status = "validation", loss = avg_loss)
        return metrics
    
    def test_step(self):
        self.advisor_model.eval()
        
        y_pred = []
        y_true = []
        
        for batch in tqdm(self.test_dataloader(), desc = f"Test Step"):
            with torch.no_grad():
                batch = [b.to(self.device) for b in batch]
            
                claim_ids = batch[0]
                claim_att = batch[1]
                db_evid_ids = batch[2]
                db_evid_att = batch[3]
                cs_evid_ids = batch[4]
                cs_evid_att = batch[5]
                tx_evid_ids = batch[6]
                tx_evid_att = batch[7]
                y = batch[8]
                
                y_lbl = torch.argmax(y, dim = 1)
                
                res = self.advisor_model(claim_ids, claim_att, db_evid_ids, db_evid_att, cs_evid_ids, cs_evid_att, tx_evid_ids, tx_evid_att)
                y_pred += res["classify_pred"].detach().cpu().tolist()
                y_true += y_lbl.cpu().tolist()
                
        
        y_pred = np.around(np.array(y_pred)).astype(int).tolist()
        metrics = self.scoring_step(y_true = y_true, y_pred = y_pred, step_status = "test")
        with open(f"results/{self.test_dataset_type}/test_predict.json", "w") as json_w:
            json.dump({"true": y_true, "pred": y_pred}, json_w, indent = 4)
        
        return metrics
        
        
        
    def training(self, patience = 3):
        self.prepare_data()
        
        current_loss = None
        
        for epoch in range(self.config["epoches"]):
            self.current_epoch = epoch + 1
            train_metrics = self.train_step()    
            model_save_dir = f"../pretrained_advisor_model/test_{self.test_dataset_type}/advisor_roberta_model_weights.pt"
            torch.save(self.advisor_model.state_dict(), model_save_dir)
            
            val_metrics = self.val_step()
            
            pprint(val_metrics)
        
        self.test_step()
        
def input_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", type = float, default = 5e-5)
    parser.add_argument("--weight_decay", type = float, default = 5e-5)

    parser.add_argument("--test_dataset_type", type = str)
    
    parser.add_argument("--model_id", type = str, default="FacebookAI/roberta-large")
    parser.add_argument("--max_length", type = int, default = 512)
    parser.add_argument("--batch_size", type = int, default = 1)
    
    parser.add_argument("--epoches", type = int, default=10)
    
    parser.add_argument("--seed", type = int, default=46)
    
    parser.add_argument("--rationale_usefulness_weight", type = float, default=1.5)
    parser.add_argument("--db_usefulnewss_weight", type = float, default=1.5)
    parser.add_argument("--rationale_judgement_weight", type = float, default=1.0)
    parser.add_argument("--db_judgement_weight", type = float, default=1.0)
    
    args = parser.parse_args()
    
    config = {
        "lr": args.lr,
        "weight_decay": args.weight_decay,
        "test_dataset_type": args.test_dataset_type,
        "model_id": args.model_id,
        "max_length": args.max_length,
        "batch_size": args.batch_size,
        "epoches": args.epoches,
        "seed": args.seed,
        
        "rationale_usefulness_weight": args.rationale_usefulness_weight,
        "db_usefulnewss_weight": args.db_usefulnewss_weight,
        "rationale_judgement_weight": args.rationale_judgement_weight, 
        "db_judgement_weight": args.db_judgement_weight,
    }
    
    return config
            
if __name__ == '__main__':
    
    config = input_parser()
    
    print("Training Hyperparameters")
    table_hyperparameter = PrettyTable()
    table_hyperparameter.field_names = ["parameters", "value"]
    for key, val in config.items():
        table_hyperparameter.add_row([key, val])
    print(table_hyperparameter)
    
    train_fake = TrainAdvisorModel(
        config = config,   
    )
    
    train_fake.training()