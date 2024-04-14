# microhttp

[支持作者和技术服务](https://afdian.net/a/huoyo)

---

<div >
    <img src='https://shields.io/badge/version-1.0.0-green.svg'>
    <img src='https://shields.io/badge/author-Chang Zhang-dbab09.svg'>
    <h4>专门为ESP32/ESP8266等硬件开发的micropython版本的WebServer，让您可以通过注解的方式使用web服务</h4>
</div>


## 安装 
拷贝microhttp.py文件到硬件的根目录即可

## 快速开始

```python
from microhttp import WebServer


app = WebServer()

@app.get('/')
def index(request,response):
    response.content_type='text/html'
    return """
    <h2>你好</h2>
    """

@app.get('/testget')
def testget(request,response):
    print('test testget')
    return {'state':1,'message':"get成功"}

@app.post('/testpost')
def testpost(request,response):
    print('test testpost')
    return {'state':1,'message':"post成功"}


@app.put('/testput')
def testput(request,response):
    print('请求',request)
    print('test testput')
    return {'state':1,'message':"put成功"}


app.run(blocked=True,port=80)

```

## 详细说明

### 1.固件支持

使用该库的前提的前提条件是ESP32和ESP8266需要刷入micropython的固件，具体可以参考[官方文档](http://micropython.86x.net/en/latet/esp32/tutorial/intro.html#esp32-intro)

### 2.安装microhttp

刷入固件之后有很多种方法可以进入硬件的根目录，本人比较喜欢的是[Thonny](https://thonny.org/)和PyCharm，PyCharm的使用方法可以参考一下博客[知数SEO](https://blog.csdn.net/weixin_42019349/article/details/134534309),写得比较详细了！

以上步骤完毕后直接将本项目的microhttp.py文件复制到硬件的根目录，当然，你也可以选择其他目录，只要阁下熟练掌握python的包原理！

### 3.使用说明

#### 1.Request和Response

microhttp已经封装好了Request和Response，不需要去研究半天这两个重要的对象去哪里获取

```python
@app.route("/")
def index(request,response):
    pass
```

#### 2.参数获取
参数的获取统一从request对象获取：
* 类似get请求的参数，统一称为route_param，通过*request.route_param*获取
* 类似post请求的body参数，统一称为body_param，通过*request.body_param*获取



### 3.编写代码

#### 1.渲染网页

microhttp默认返回的是Content-Type为*application/json*，需要渲染网页时，需要修改content_type

```python
from microhttp import WebServer

app = WebServer()

@app.get('/')
def index(request,response):
    response.content_type='text/html'
    return """
    <h2>你好</h2>
    """

app.run(blocked=True,port=80)
```

#### 2.GET请求

```python
from microhttp import WebServer

app = WebServer()

@app.get('/testget')
def testget(request,response):
    print('param:',request.route_param)
    return {'state':1,'message':"get成功"}

app.run(blocked=True,port=80)
```


#### 3.POST请求

```python
from microhttp import WebServer

app = WebServer()

@app.post('/testpost')
def testpost(request,response):
    print('param:',request.body_param)
    return {'state':1,'message':"post成功"}

app.run(blocked=True,port=80)
```

## 版权说明
1.本项目版权属作者所有，并使用 GPL-2.0进行开源；

2.您可以使用本项目进行学习，并且免费将本项目作为第三方库引入后进行商用（无需开源）；

3.但不允许将本项目二次开发后闭源商用（除非得到作者授权）；

简单理解：开源项目直接使用永远是免费的，也不需要开源，这一点不会变，但是不允许二次开发以后进行闭源商用