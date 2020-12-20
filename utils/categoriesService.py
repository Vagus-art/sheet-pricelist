import uuid
import os
import boto3
CATEGORIES_TABLE = os.getenv('CATEGORIES_TABLE')
client = boto3.client('dynamodb')


def postCategory(name):
    response = client.put_item(
        TableName=CATEGORIES_TABLE,
        Item={
            'name': {'S': name},
            'id': {'S': str(uuid.uuid4())}
        }
    )
    return response


def updateCategory(id, name):
    response = client.put_item(
        TableName=CATEGORIES_TABLE,
        Item={
            'name': {'S': name},
            'id': {'S': id}
        }
    )
    return response


def getCategories():
    response = client.scan(TableName=CATEGORIES_TABLE)
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = client.scan(TableName=CATEGORIES_TABLE,
                               ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return data


def deleteCategory(id):
    response = client.delete_item(
        TableName=CATEGORIES_TABLE,
        Key={
            'id': {'S': id}
        }
    )
    return response
