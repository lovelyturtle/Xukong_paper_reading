### Xukong_paper_reading

“虚空”文献辅助阅读系统，旨在帮助科研人员更好的阅读论文！
接入4个大语言模型API，帮助进行翻译、总结、解释等任务，加快文献阅读效率。“虚空”一词出自游戏原神(Genshin)。

#### 接入的LLM：

| LLM               | 厂家                          | 使用说明                                                     |
| ----------------- | ----------------------------- | ------------------------------------------------------------ |
| GPT-3.5-turbo-16k | openAI                        | 需前往[API keys - OpenAI API](https://platform.openai.com/account/api-keys)申请自己的API密钥，国内使用需VPN |
| ErnieBot-turbo    | Baidu                         | 需前往[百度智能云千帆大模型平台 (baidu.com)](https://console.bce.baidu.com/qianfan/overview)申请自己的API密钥 |
| ChatGLM2-6B-32k   | Tsinghua University, Zhipu AI | 需前往[百度智能云千帆大模型平台 (baidu.com)](https://console.bce.baidu.com/qianfan/overview)申请自己的API密钥 |
| Spark-v1.5        | iFLYTEK                       | 免费使用                                                     |

#### 项目部署：

按仓库的目录结构下载至本地，首先配置config.json文件：

- 使用GPT为基座模型时，model="GPT"，并填写申请的"GPT-API"
- 使用ErnieBot为基座模型时，model="ErnieBot"，并填写申请的"API_KEY"，"SECRET_KEY"
- 使用ChatGLM为基座模型时，model="ChatGLM"，并填写申请的"API_KEY"，"SECRET_KEY"
- 使用Spark为基座模型时，model="Spark"

需确保电脑已配置Python3的环境，并命令行运行以下指令安装必需的第三方库：

```
pip install openai
```

进入项目目录，运行server.py启动服务器；在浏览器访问127.0.0.1:8000端口即可。

#### About us：

Author: Yuli Q, Cindy He

from: BIT

code helper: ChatGPT
