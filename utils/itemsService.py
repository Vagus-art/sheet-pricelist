import uuid
import os
import boto3
from boto3.dynamodb.conditions import Key
ITEMS_TABLE = os.getenv('ITEMS_TABLE')
client = boto3.client('dynamodb')


def postItem(categoryId, name):
    response = client.put_item(
        TableName=ITEMS_TABLE,
        Item={
            'name': {'S': name},
            'categoryId': {'S': categoryId},
            'id': {'S': str(uuid.uuid4())}
        }
    )
    return response


def updateItem(id, categoryId, name):
    response = client.put_item(
        TableName=ITEMS_TABLE,
        Item={
            'name': {'S': name},
            'categoryId': {'S': categoryId},
            'id': {'S': id}
        }
    )
    return response


def getItems(categoryId):
    response = client.scan(TableName=ITEMS_TABLE, FilterExpression=Key(
        'categoryId').eq(categoryId))
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = client.scan(TableName=ITEMS_TABLE, ExclusiveStartKey=response['LastEvaluatedKey'], FilterExpression=Key(
            'categoryId').eq(categoryId))
        data.extend(response['Items'])
    return data


def deleteItem(id):
    response = client.delete_item(
        TableName=ITEMS_TABLE,
        Key={
            'id': id
        }
    )
    return response
