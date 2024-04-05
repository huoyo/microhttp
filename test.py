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
