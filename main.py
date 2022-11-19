import boto3
import json
from  fastapi import FastAPI

import consumer.consumer
from consumer import  consumer
from producer import  producer


app = FastAPI()


app.include_router(consumer.router)
app.include_router(producer.router)
