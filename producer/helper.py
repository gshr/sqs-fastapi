import boto3
import json
from config import  setting
sqs_client = boto3.client("sqs",
                          aws_access_key_id=setting.aws_access_key,
                          aws_secret_access_key=setting.aws_secret_key,
                          region_name=setting.region_name)


def get_queue_url():
    response = sqs_client.get_queue_url(
        QueueName="MyQueue",
    )
    return response['QueueUrl']


def send_message(body):
    print(body)

    response = sqs_client.send_message(
        QueueUrl=get_queue_url(),
        MessageBody=body
    )
    return response


