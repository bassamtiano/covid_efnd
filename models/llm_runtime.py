import sys

import torch

import ollama
from ollama import Client

from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

class LLMRuntime():
    def __init__(self, 
                 model_id,
                 seed = 46,
                 temperature = 0.2,
                 repetition_penalty = 1.2,
                 use_ollama = True,
                 network_ollama = False,
                 ollama_api_address = None):
        self.model_id = model_id
        
        self.seed = seed
        self.random_seed()

        self.temperature = temperature
        self.repetition_penalty = repetition_penalty
        
        self.use_ollama = use_ollama
        self.network_ollama = network_ollama
        self.ollama_api_address = ollama_api_address
        
        if self.network_ollama == True and self.ollama_api_address != None:
            print(f"address")
            print(f'http://{ollama_api_address}:11435')
            print("NETWORK")
            self.ollama_client = Client(host = f'http://{ollama_api_address}:11435')
        
        if not self.use_ollama and not self.network_ollama:
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            self.prepare_huggingface_llm()

    def random_seed(self):
        torch.manual_seed(self.seed)
        torch.cuda.manual_seed(self.seed)
        torch.cuda.manual_seed_all(self.seed)
        torch.backends.cudnn.deterministic = True
    
    def prepare_huggingface_llm(self):
        if "mistral" in self.model_id: 
            model_id = "mistralai/Mistral-7B-Instruct-v0.2"
            self.max_new_token = 4096
        elif "llama3" in self.model_id:
            model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
            self.max_new_token = 8192
        elif "llama3:70b" in self.model_id:
            model_id = "meta-llama/Meta-Llama-3-70B-Instruct"
            self.max_new_token = 8192
        
        nf4_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16
        )
        
        self.llm_tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.llm_model = AutoModelForCausalLM.from_pretrained(model_id,
                                                              quantization_config = nf4_config)
        self.llm_model.to(self.device)
    
    def generate_response(self, 
                          prompt,
                          max_new_tokens = 8192):
        if self.use_ollama and self.network_ollama == False:
            response = ollama.generate(
                model = self.model_id, 
                prompt = prompt,
                options = {
                    "seed": self.seed,
                    "temperature" : self.temperature,
                    "repeat_penalty": self.repetition_penalty,
                    "num_ctx": max_new_tokens
                }
            )
            return response["response"]
        
        elif self.network_ollama == True and self.ollama_api_address != None:
            ollama_options = {}
            if self.seed:
                ollama_options["seed"] = self.seed
            
            if self.temperature:
                ollama_options["temperature"] = self.temperature
            
            if self.repetition_penalty:
                ollama_options["repetition_penalty"] = self.repetition_penalty
                
            if max_new_tokens:
                ollama_options["num_ctx"] = max_new_tokens
            
            response = self.ollama_client.generate(
                model = self.model_id,
                prompt = prompt,
                options = ollama_options,
            )

            return response["response"]
        else:
            with torch.no_grad():
                prompt_token = self.llm_tokenizer([prompt], return_tensors = "pt").to(torch.device("cuda"))
                generated_id = self.llm_model.generate(
                    input_ids = prompt_token["input_ids"],
                    attention_mask = prompt_token["attention_mask"], 
                    temperature = self.temperature,
                    repetition_penalty = self.repetition_penalty,
                    max_new_tokens = self.max_new_tokens, 
                    do_sample = True, 
                    pad_token_id=self.tokenizer.eos_token_id,
                    output_scores=True,
                )
                
            torch.cuda.empty_cache()
            
            response = self.tokenizer.batch_decode(generated_id)
            
            if "mistral" in self.model_id: 
                tail_prompt_index = response[0].find('[/INST]')
                response = response[0][tail_prompt_index:].replace("[/INST]", "").strip()
                response = response.replace("</s>", "").strip()
            elif "llama3" in self.model_id:
                tail_prompt_index = response[0].find('<|start_header_id|>assistant<|end_header_id|>')
                response = response[0][tail_prompt_index:].replace("<|start_header_id|>assistant<|end_header_id|>", "").strip()
                response = response.replace("<|eot_id|>", "").strip()
            return response
        
    def generate_chat_response(self, 
                               message,
                               chat_format = False,
                               max_new_tokens = 8192):
        
        if chat_format == True:
            messages_template = message
        else:
            messages_template = [
                {
                    "role": "system",
                    "content": "You are a helpful, straight forward, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Please ensure that your responses are socially unbiased and positive in nature."
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
            
        
        ollama_options = {}
        if self.seed:
            ollama_options["seed"] = self.seed
        
        if self.temperature:
            ollama_options["temperature"] = self.temperature
        
        if self.repetition_penalty:
            ollama_options["repetition_penalty"] = self.repetition_penalty
            
        if max_new_tokens:
            ollama_options["num_ctx"] = max_new_tokens
        
        if self.use_ollama and self.network_ollama == False:
            response = ollama.chat(
                model = self.model_id, 
                messages = messages_template,
                options = ollama_options,
            )
            
            return response["message"]["content"]
        
        elif self.network_ollama == True and self.ollama_api_address != None:
            response = self.ollama_client.chat(
                model = self.model_id, 
                messages = messages_template,
                options = ollama_options
            )
            
            return response["message"]["content"]
            
        else:
            with torch.no_grad():
                
                # messages_template = [
                #     {
                #         "role": "system",
                #         "content": "You are a helpful, straight forward, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Please ensure that your responses are socially unbiased and positive in nature."
                #     },
                #     {
                #         "role": "user",
                #         "content": message
                #     }
                # ]
                
                tokenized_chat = self.llm_tokenizer.apply_chat_template(
                    messages_template, 
                    tokenize = True, 
                    add_generation_prompt = True, 
                    return_tensors="pt"
                ).to(torch.device("cuda"))
                
                
                generated_id = self.llm_model.generate(
                    input_ids = tokenized_chat["input_ids"],
                    attention_mask = tokenized_chat["attention_mask"], 
                    temperature = self.temperature,
                    repetition_penalty = self.repetition_penalty,
                    max_new_tokens = self.max_new_tokens, 
                    do_sample = True, 
                    pad_token_id=self.tokenizer.eos_token_id,
                    output_scores=True,
                )
                
            torch.cuda.empty_cache()
            
            response = self.tokenizer.batch_decode(generated_id)
            
            if "mistral" in self.model_id: 
                tail_prompt_index = response[0].find('[/INST]')
                response = response[0][tail_prompt_index:].replace("[/INST]", "").strip()
                response = response.replace("</s>", "").strip()
            elif "llama3" in self.model_id:
                tail_prompt_index = response[0].find('<|start_header_id|>assistant<|end_header_id|>')
                response = response[0][tail_prompt_index:].replace("<|start_header_id|>assistant<|end_header_id|>", "").strip()
                response = response.replace("<|eot_id|>", "").strip()
            return response