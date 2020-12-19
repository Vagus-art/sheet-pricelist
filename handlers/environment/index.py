import json
import os

RDS_HOST = os.getenv('RDS_HOST')
RDS_DB_NAME = os.getenv('RDS_DB_NAME')

def handler(event, context):
    if (event['httpMethod']=='GET'):
        data = {
            'output': f"Database host: {RDS_HOST}. Database name {RDS_DB_NAME}."
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
    