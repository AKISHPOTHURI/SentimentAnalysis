from transformers import AutoTokenizer,AutoModelForSequenceClassification
import torch

from Sentiment.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
        
    def prediction(self,text):
        tok = AutoTokenizer.from_pretrained(self.config.modelname)
        mod = AutoModelForSequenceClassification.from_pretrained(self.config.modelname)
        input_ids = tok.encode(text, return_tensors='pt')
        output = mod(input_ids)
        preds = torch.nn.functional.softmax(output.logits, dim=-1)
        prob = torch.max(preds).item()
        idx = torch.argmax(preds).item()
        # sentiment = id2label[idx]

        return {'text':text,'sentiment':idx, 'prob':prob}