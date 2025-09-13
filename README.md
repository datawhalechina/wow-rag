# wow-rag


RAG(Retrieval Augmented Generation)是一种结合了检索和生成的AI技术框架。它通过从知识库中检索相关信息来增强大语言模型的生成能力,可以帮助模型生成更准确、更可靠的回答。本项目旨在探索和实现RAG技术,包括文档处理、向量检索、prompt engineering等核心模块,帮助开发者更好地理解和应用RAG技术。

秉持着自塾（zishu.co）学用合一的理念，有教程必有产品，wow-rag会同时打造RAG的教程和产品。学到的知识用来打造产品，打造产品用到的知识总结进教程。我们将会为企业打造一个系列的极简、跨平台、易定制的RAG产品。

## 快速体验RAG

- 第一步：克隆仓库到本地，克隆后，可以麻烦给我们点个star吗？鼓励我们做得更好！
```bash
git clone https://github.com/datawhalechina/wow-rag.git
```

- 第二步：用python自带的venv模块创建虚拟环境
推荐使用python3.9以上版本。
在wow-rag目录下打开终端，运行以下命令：
```bash
python -m venv rag-venv
```

- 第三步：激活Windows虚拟环境
在第二步的终端环境中，运行以下命令：
```bash
.\rag-venv\Scripts\activate
```


- 第四步：安装依赖
输入`cd backend`，进入到wow-rag/backend目录下，运行以下命令：
```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 第五步：运行后端服务
在wow-rag/backend目录下打开终端，运行以下命令：
```bash
python main.py
```

- 第六步：运行前端页面
在wow-rag/frontend目录下双击chat.html，在文本框中输入问题，然后点击发送按钮即可体验流式对话。
或者，在wow-rag/frontend目录下打开终端，输入这行代码：
```bash
python -m http.server 8080 --bind 0.0.0.0
```
然后在浏览器中输127.0.0.1:8080/chat.html即可体验流式对话。





## 课程内容
- 第1课：手搓一个土得掉渣的RAG
- 第2课：正式上路搞定模型
- 第3课：初步体验问答引擎
- 第4课：最脏最累的文档管理
- 第5课：流式部署

## 项目附属文件
- base.py 可以用来替换Lib\site-packages\llama_index\embeddings\openai\base.py这个文件。其实就是修改了四行代码。懒人专用。我们不要做一个懒人，而是动动手自己照着教程找到源代码的文件修改指定的四行即可。希望你永远不要用到这个文件。
- 本项目的前端页面chat.html，直接双击打开。在文本框中输入问题，然后点击发送按钮即可体验流式对话。
- 问答手册.txt 本项目第一课的那些文本。懒人专用。我们不要做一个懒人，而是动动手自己找篇长文本新建一个txt文件。希望你永远不要用到这个文件。
- learn.ipynb 本项目的所有运行代码。懒人专用。我们不要做一个懒人，而是动动手把本教程所有代码自己复制到空白ipynb文件中亲自运行。希望你永远不要用到这个文件。

## 参与贡献

- 如果你想参与到项目中来欢迎查看项目的 [Issue]() 查看没有被分配的任务。
- 如果你发现了一些问题，欢迎在 [Issue]() 中进行反馈🐛。
- 如果你对本项目感兴趣想要参与进来可以通过 [Discussion]() 进行交流💬。
- 或者直接发邮件到zishuco@163.com

如果你对 Datawhale 很感兴趣并想要发起一个新的项目，欢迎查看 [Datawhale 贡献指南](https://github.com/datawhalechina/DOPMC#%E4%B8%BA-datawhale-%E5%81%9A%E5%87%BA%E8%B4%A1%E7%8C%AE)。


## 待做清单
- [x] 美化chat.html
- [x] 解决“快速体验RAG”最后一步流式输出失灵的问题
- [x] 把cs-408考研科目的计算机网络和操作系统做到docs里边
- [ ] 把cs-408考研科目的计算机组成和数据结构做到docs里边
- [x] 用Qdrant做后端磁盘保存的向量数据库
- [ ] 在Linux云电脑跑本教程的说明
- [ ] 申请零一万物的36元额度的说明
- [ ] chat.html输出消息后让页面自动滚动到最底部
- [ ] 如果先运行main.py，再打开chat.html，会卡。反之就不卡，解决这个bug。




## 贡献者名单

| 姓名 | 职责 | 简介 |
| :----| :---- | :---- |
| [黎伟](https://github.com/omige) | 项目负责人 | datawhale成员，构建整个教程 |
| [坐看云起](https://github.com/netbuddy) | 贡献者 | 内测学员，第2课智谱官方包接口 |
| [阿鲁](https://github.com/abchbx) | 贡献者 | 内测学员，第2课自定义模型接口 |
| [吴小龙](https://github.com/LouisCanBe) | 贡献者 | 内测学员，第5课美化chat.html |
| [宏辉](https://github.com/cheunghonghui) | 贡献者 | 助教，第2课构建自塾开放API服务 |
| [胡琦](https://github.com/hu-qi) | 贡献者 | 助教，后端engine.py接入自塾开放API服务 |
| [邢思宇](https://github.com/xiaoyuhuv) | 贡献者 | 塾员，计网和操作系统的文档 |

## 关注我们

<div align=center>
<p>扫描下方二维码关注公众号：Datawhale</p>
<img src="https://raw.githubusercontent.com/datawhalechina/pumpkin-book/master/res/qrcode.jpeg" width = "180" height = "180">
</div>

## LICENSE

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议</a>进行许可。

*注：默认使用CC 4.0协议，也可根据自身项目情况选用其他协议*

