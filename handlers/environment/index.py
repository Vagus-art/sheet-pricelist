import json
import os

CATEGORIES_TABLE = os.getenv('CATEGORIES_TABLE')

def handler(event, context):
    if (event['httpMethod']=='GET'):
        data = {
            'output': f"Table name: {CATEGORIES_TABLE}."
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
