import dynamo_json
import boto3

client = boto3.client('dynamodb')

def unmarshall_array(array):
    array_return = []
    for item in array:
        array_return.append(dynamo_json.unmarshall(item))
    return array_return

def put_item(table, item):
    response = client.put_item(
        TableName=table,
        Item=dynamo_json.marshall(item)
        )
    return response

def delete_item(table, key):
    response = client.delete_item(
        TableName=table,
        Key=dynamo_json.marshall(key)
    )
    return response
