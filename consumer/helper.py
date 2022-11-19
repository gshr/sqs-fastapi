import boto3
import json
from config import setting

sqs_client = boto3.client("sqs",
                          aws_access_key_id=setting.aws_access_key,
                          aws_secret_access_key=setting.aws_secret_key,
                          region_name=setting.region_name)


def get_queue_url():
    response = sqs_client.get_queue_url(
        QueueName="MyQueue",
    )
    return response['QueueUrl']


def receive_message():
    response = sqs_client.receive_message(
        QueueUrl=get_queue_url(),
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10,
    )

    print(f"Number of messages received: {len(response.get('Messages', []))}")
    response_body = []

    for message in response.get("Messages", []):
        message_body = message["Body"]
        print(f"Message body: {message_body}")
        response_body.append(json.loads(message_body))
        # print(f"Receipt Handle: {message['ReceiptHandle']}")
        delete_message(message['ReceiptHandle'])

    return response_body


def delete_message(receipt_handle):
    response = sqs_client.delete_message(
        QueueUrl=get_queue_url(),
        ReceiptHandle=receipt_handle,
    )
    print(f"{receipt_handle[:7]} deleted Successfully")
