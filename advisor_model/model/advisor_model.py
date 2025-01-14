import sys

import torch
import torch.nn as nn

from .advisor_layers import *

from transformers import AutoModel
from pprint import pprint

class AdvisorModel(nn.Module):
    def __init__(self,
                 batch_size,
                 emb_dim = 1024,
                 mlp_dim = [384],
                 dropout = 0.2,
                 model_id = "bert-base-uncased",
                 ):
        super(AdvisorModel, self).__init__()
        
        self.batch_size = batch_size
        
        self.lm_content = AutoModel.from_pretrained(model_id).requires_grad_(False)
        self.lm_evidence_source = AutoModel.from_pretrained(model_id).requires_grad_(False)
        self.lm_rationale = AutoModel.from_pretrained(model_id).requires_grad_(False)
        
        self.cross_attention_content_feature_1 = SelfAttentionFeatureExtract(1, emb_dim)
        self.cross_attention_content_feature_2 = SelfAttentionFeatureExtract(1, emb_dim)
        self.cross_attention_content_feature_3 = SelfAttentionFeatureExtract(1, emb_dim)
        
        self.cross_attention_evid_feature_1 = SelfAttentionFeatureExtract(1, emb_dim)
        self.cross_attention_evid_feature_2 = SelfAttentionFeatureExtract(1, emb_dim)
        self.cross_attention_evid_feature_3 = SelfAttentionFeatureExtract(1, emb_dim)
        
        self.claim_attention = MaskAttention(emb_dim)
        self.db_evid_attention = MaskAttention(emb_dim)
        self.cs_evid_attention = MaskAttention(emb_dim)
        self.tx_evid_attention = MaskAttention(emb_dim)
        
        self.agregator = MaskAttention(emb_dim)
        self.mlp = MLP(emb_dim, mlp_dim, dropout)
        
        if batch_size > 1:
            self.score_mapper_feature_1 = nn.Sequential(
                nn.Linear(emb_dim, mlp_dim[-1]),
                nn.BatchNorm1d(mlp_dim[-1]),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(mlp_dim[-1], self.batch_size),
                nn.BatchNorm1d(self.batch_size),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(self.batch_size, 1),
                nn.Sigmoid()
            )
            
            self.score_mapper_feature_2 = nn.Sequential(
                nn.Linear(emb_dim, mlp_dim[-1]),
                nn.BatchNorm1d(mlp_dim[-1]),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(mlp_dim[-1], self.batch_size),
                nn.BatchNorm1d(self.batch_size),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(self.batch_size, 1),
                nn.Sigmoid()
            )
        
            self.score_mapper_feature_3 = nn.Sequential(
                nn.Linear(emb_dim, mlp_dim[-1]),
                nn.BatchNorm1d(mlp_dim[-1]),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(mlp_dim[-1], self.batch_size),
                nn.BatchNorm1d(self.batch_size),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(self.batch_size, 1),
                nn.Sigmoid()
            )

        else:
            self.score_mapper_feature_1 = nn.Sequential(
                nn.Linear(emb_dim, mlp_dim[-1]),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(mlp_dim[-1], self.batch_size),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(self.batch_size, 1),
                nn.Sigmoid()
            )
            
            self.score_mapper_feature_2 = nn.Sequential(
                nn.Linear(emb_dim, mlp_dim[-1]),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(mlp_dim[-1], self.batch_size),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(self.batch_size, 1),
                nn.Sigmoid()
            )
        
            self.score_mapper_feature_3 = nn.Sequential(
                nn.Linear(emb_dim, mlp_dim[-1]),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(mlp_dim[-1], self.batch_size),
                nn.ReLU(),
                nn.Dropout(0.2),
                nn.Linear(self.batch_size, 1),
                nn.Sigmoid()
            )
        
        
        self.hard_feature_1_mlp = MaskAttention(emb_dim)
        self.hard_mlp_feature_1 = nn.Sequential(
            nn.Linear(emb_dim, mlp_dim[-1]),
            nn.ReLU(),
            nn.Linear(mlp_dim[-1], 1),
            nn.Sigmoid()
        )
        
        self.hard_feature_2_mlp = MaskAttention(emb_dim)
        self.hard_mlp_feature_2 = nn.Sequential(
            nn.Linear(emb_dim, mlp_dim[-1]),
            nn.ReLU(),
            nn.Linear(mlp_dim[-1], 1),
            nn.Sigmoid()
        )
        
        
        self.hard_feature_3_mlp = MaskAttention(emb_dim)
        self.hard_mlp_feature_3 = nn.Sequential(
            nn.Linear(emb_dim, mlp_dim[-1]),
            nn.ReLU(),
            nn.Linear(mlp_dim[-1], 1),
            nn.Sigmoid()
        )
        
        
        self.simple_feature_1_attention = MaskAttention(emb_dim)
        self.simple_mlp_feature_1_attention = nn.Sequential(
            nn.Linear(emb_dim, mlp_dim[-1]),
            nn.ReLU(),
            nn.Linear(mlp_dim[-1], 3)
        )
        
        self.simple_feature_2_attention = MaskAttention(emb_dim)
        self.simple_mlp_feature_2_attention = nn.Sequential(
            nn.Linear(emb_dim, mlp_dim[-1]),
            nn.ReLU(),
            nn.Linear(mlp_dim[-1], 3)
        )
        
        self.simple_feature_3_attention = MaskAttention(emb_dim)
        self.simple_mlp_feature_3_attention = nn.Sequential(
            nn.Linear(emb_dim, mlp_dim[-1]),
            nn.ReLU(),
            nn.Linear(mlp_dim[-1], 3)
        )
        
    def forward(self, claim_ids, claim_att, db_evid_ids, db_evid_att, cs_evid_ids, cs_evid_att, tx_evid_ids, tx_evid_att):
        
        claim_feature = self.lm_content(claim_ids, attention_mask = claim_att).last_hidden_state
        db_evid_feature = self.lm_evidence_source(db_evid_ids, attention_mask = db_evid_att).last_hidden_state 
        cs_evid_feature = self.lm_rationale(cs_evid_ids, attention_mask = cs_evid_att).last_hidden_state 
        tx_evid_feature = self.lm_rationale(tx_evid_ids, attention_mask = tx_evid_att).last_hidden_state 
        
        claim_db_evid_feature, _ = self.cross_attention_content_feature_1(claim_feature, db_evid_feature, claim_att)
        claim_cs_evid_feature, _ = self.cross_attention_content_feature_2(claim_feature, cs_evid_feature, claim_att)
        claim_tx_evid_feature, _ = self.cross_attention_content_feature_3(claim_feature, tx_evid_feature, claim_att)
        
        expert_1 = torch.mean(claim_db_evid_feature, dim = 1)
        expert_2 = torch.mean(claim_cs_evid_feature, dim = 1)
        expert_3 = torch.mean(claim_tx_evid_feature, dim = 1)
        
        db_evid_claim_feature, _ = self.cross_attention_evid_feature_1(db_evid_feature, claim_feature, db_evid_att)
        cs_evid_claim_feature, _ = self.cross_attention_evid_feature_2(cs_evid_feature, claim_feature, cs_evid_att)
        tx_evid_claim_feature, _ = self.cross_attention_evid_feature_3(tx_evid_feature, claim_feature, tx_evid_att)
        
        db_evid_claim_feature = torch.mean(db_evid_claim_feature, dim = 1)
        cs_evid_claim_feature = torch.mean(cs_evid_claim_feature, dim = 1)
        tx_evid_claim_feature = torch.mean(tx_evid_claim_feature, dim = 1)
        
        hard_feature_1_pred = self.hard_mlp_feature_1(db_evid_claim_feature).squeeze(1)
        hard_feature_2_pred = self.hard_mlp_feature_2(cs_evid_claim_feature).squeeze(1)
        hard_feature_3_pred = self.hard_mlp_feature_3(tx_evid_claim_feature).squeeze(1)
        
        simple_feature_1_pred = self.simple_mlp_feature_1_attention(self.simple_feature_1_attention(db_evid_feature)[0]).squeeze(1)
        simple_feature_2_pred = self.simple_mlp_feature_2_attention(self.simple_feature_2_attention(cs_evid_feature)[0]).squeeze(1)
        simple_feature_3_pred = self.simple_mlp_feature_3_attention(self.simple_feature_3_attention(tx_evid_feature)[0]).squeeze(1)
        
                       
        attention_claim, _ = self.claim_attention(claim_feature, mask = claim_att)
        
        reweight_score_feature_1 = self.score_mapper_feature_1(db_evid_claim_feature)
        reweight_score_feature_2 = self.score_mapper_feature_2(cs_evid_claim_feature)
        reweight_score_feature_3 = self.score_mapper_feature_3(tx_evid_claim_feature)
        
        reweight_expert_1 = reweight_score_feature_1 * expert_1
        reweight_expert_2 = reweight_score_feature_2 * expert_2
        reweight_expert_3 = reweight_score_feature_3 * expert_3
        
        
        all_feature = torch.cat(
            (attention_claim.unsqueeze(1), reweight_expert_1.unsqueeze(1), reweight_expert_2.unsqueeze(1), reweight_expert_3.unsqueeze(1)),
            dim = 1
        )
        final_feature, _ = self.agregator(all_feature)
        
        label_pred = self.mlp(final_feature)
        gate_value = torch.concat([
            reweight_score_feature_1,
            reweight_score_feature_2,
            reweight_score_feature_3
        ], dim = 1)
        
        res = {
            "classify_pred": torch.sigmoid(label_pred.squeeze(1)),
            "gate_value": gate_value,
            "final_feature": final_feature,
            "claim_feature": claim_feature,
            "feature_1": reweight_expert_1,
            "feature_2": reweight_expert_2,
            "feature_3": reweight_expert_3,
            "hard_feature_1_pred": hard_feature_1_pred,
            "hard_feature_2_pred": hard_feature_2_pred,
            "hard_feature_3_pred": hard_feature_3_pred,
            "simple_feature_1_pred": simple_feature_1_pred,
            "simple_feature_2_pred": simple_feature_2_pred,
            "simple_feature_3_pred": simple_feature_3_pred,
        }
        
        return res