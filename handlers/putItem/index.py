import json
import os
import uuid
import boto3
CATEGORIES_TABLE = os.getenv('CATEGORIES_TABLE')
client = boto3.client('dynamodb')


def handler(event, context):
    if (event['httpMethod']=='GET'):
        response = client.put_item(
            TableName=CATEGORIES_TABLE,
            Item={
                    'hello':{'S':'world'},
                    'id':{'S':str(uuid.uuid4())}
                }
        )
        data = {
            'output': f"Response: {json.dumps(response, separators=(',', ':'))}."
        }
        return {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
    if (event['httpMethod']=='POST'):
        data = {
            'output': json.loads(event['body'])
        }
        return {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
