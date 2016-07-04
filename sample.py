from celery import Celery


app = Celery('sample', broker='amqp://guest:guest123@localhost:5672//')

@app.task
def hello():
    print("Hello world")
    return ("Hello, world")

for i in range(10):
    hello.delay()
