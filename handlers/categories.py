import json
import datetime
from hello import HELLO_WORLD


def handler(event, context):
    if (event['httpMethod']=='GET'):
        data = {
            'output': HELLO_WORLD
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
    