import json
import os
import boto3

CATEGORIES_TABLE = os.getenv('CATEGORIES_TABLE')

def handler(event, context):
    if (event['httpMethod']=='GET'):
        table = dynamodb.Table(CATEGORIES_TABLE)
        response = table.put_item(
        Item={
                'hello':'world'
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
