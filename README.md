#### 环境

* elasticsearch6.4.0
* python3.6+

配置elasticsearch可以选择在linux或在windows下， 看官方文档中的介绍

选择安装[elasticsearch-head](https://github.com/mobz/elasticsearch-head)插件


#### 创建索引

* 执行insert_es.py脚本，或者当你安装好head插件后在http://localhost:9100下添加索引，也可以使用postman等工具请求处理

* 你需要注意你的elasticsearch的版本引发的问题，可以点击查看[官方文档](https://www.cnblogs.com/tcppdu/p/9598121.html)


#### 数据插入

* 执行insert_es.py脚本， 等待数据插入elasticsearch， 然后访问http://127.0.0.1:9100/