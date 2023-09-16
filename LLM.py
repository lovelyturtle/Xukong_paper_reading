from GPT_turbo import GPT
from SparkApi import Spark
from ErnieBot_turbo import ErnieBot
import json

with open(".\\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
model=config['model']

class LLM:
    def __init__(self):
        if model=="Spark":
            self.model=Spark
        elif model=="ErnieBot" or model=="ChatGLM":
            self.model=ErnieBot
        elif model=="GPT":
            self.model=GPT

    def get_QA(self, prompt_):
        prompt=prompt_.replace("\n", "")
        ans=self.model(prompt, model)
        return ans