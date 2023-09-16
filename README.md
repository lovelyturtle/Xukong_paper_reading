# Xukong_paper_reading
“虚空”文献辅助阅读系统，旨在帮助科研人员更好的阅读论文！接入4个大语言模型API，帮助进行翻译、总结、解释等任务，加快文献阅读效率。<br>
“虚空”一词出自游戏原神(Genshin)。
# 部署
将仓库下载到本地，将待阅读的文章重命名为paper.pdf并放到仓库目录下。
修改config.json的模型类型、API密钥等信息。
进入仓库所在目录，运行: python server.py。
浏览器访问127.0.0.1:8000端口，即可使用“虚空”文献辅助阅读系统。
# 接入的API
ChatGPT、ErnieBot、ChatGLM、Spark
