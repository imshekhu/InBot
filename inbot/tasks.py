from inbot.celery import app

@app.task
def myTest():
    print('hi')