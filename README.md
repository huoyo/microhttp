# microhttp

[支持作者和技术服务](https://afdian.net/a/huoyo)

---

<div >
    <img src='https://shields.io/badge/version-1.0.0-green.svg'>
    <img src='https://shields.io/badge/author-Chang Zhang-dbab09.svg'>
    <h4>专门为ESP32/ESP8266等硬件开发的micropthon版本的WebServer，让您可以通过注解的方式使用web服务</h4>
</div>


## 安装 
拷贝microhttp.py文件到硬件的根目录即可

## 使用

```python
from microhttp import WebServer


app = WebServer()

@app.get('/')
def test(request,response):
    response.content_type='text/html'
    return """
    <h2>你好</h2>
    """

@app.get('/testget')
def test2(request,response):
    print('test testget')
    return {'state':1,'message':"get成功"}

@app.post('/testpost')
def test2(request,response):
    print('test testpost')
    return {'state':1,'message':"post成功"}


@app.put('/testput')
def test3(request,response):
    print('请求',request)
    print('test testpost')
    return {'state':1,'message':"put成功"}


app.run(blocked=True,port=80)

```
