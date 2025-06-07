from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

class LocalLLM:
    def __init__(self, model_name='gpt2', device=None):
        self.device = device if device else ('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name).to(self.device)
        self.model.eval()

    def expand(self, prompt, max_length=100):
        inputs = self.tokenizer(prompt, return_tensors='pt').to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                do_sample=True,
                top_p=0.9,
                temperature=0.8,
                num_return_sequences=1
            )
        expanded_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return expanded_text
