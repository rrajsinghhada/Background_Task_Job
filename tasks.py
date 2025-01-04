# tasks.py
from celery import Celery
import time

app = Celery('myapp', broker='redis://redis:6379/0')

@app.task
def add(x, y):
    time.sleep(5)  # Simulate long task
    return x + y
