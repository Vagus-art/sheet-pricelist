import json

def success_response(body):
    return {'statusCode': 200,
            'body': json.dumps(body),
            'headers': {'Content-Type': 'application/json'}}
