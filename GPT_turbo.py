import openai
import json

with open(".\\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
API=config['GPT-API']

context=[{"role": "system", "content": "你是一个文献阅读助手；请根据用户要求回答有关论文的内容"}]

def GPT(prompt, _):
    openai.api_key = API
    prompt=prompt[0:16000]
    context.append({"role": "user", "content": prompt})
    print(context,len(context))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=context,
        temperature=0.1)
    context.append({"role":"assistant", "content":completion.choices[0].message.content})
    return completion.choices[0].message.content
