import requests
import json

with open(".\\config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
API_KEY = config['API_KEY']
SECRET_KEY = config['SECRET_KEY']

context=[{"role": "user", "content": "你是一个文献助手，按要求回答论文问题"},{"role": "assistant", "content": "好的，请开始提问"}]

def ErnieBot(prompt, model):
    prompt=prompt[0:11000]
    if model=="ErnieBot":
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
        prompt=prompt[0:11000]
    elif model=="ChatGLM":
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/chatglm2_6b_32k?access_token=" + get_access_token()
        prompt=prompt[0:2000]
    context.append({"role": "user", "content": prompt})
    payload = json.dumps({
        "messages": context,
        "temperature": 0.1
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    result = json.loads(response.text)['result']
    context.append({"role": "assistant", "content": result})
    return result

def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))