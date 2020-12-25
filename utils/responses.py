import json
from base64 import b64encode

def success_response(body):
    return {'statusCode': 200,
            'body': json.dumps(body),
            'headers': {'Content-Type': 'application/json'}}

def success_response_pdf(body):
    return {'statusCode': 200,
            'body': b64encode(body).decode("utf-8"),
            'headers': {'Content-Type': 'application/pdf'},
            'isBase64Encoded': True}