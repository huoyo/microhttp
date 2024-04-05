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
