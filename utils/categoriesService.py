import uuid
import boto3
from database import unmarshall_array, put_item, delete_item
from constants import CATEGORIES_TABLE

client = boto3.client('dynamodb')


def postCategory(name):
    response = put_item(CATEGORIES_TABLE, {
        'name': name,
        'id': str(uuid.uuid4())
    })
    return response


def updateCategory(id, name):
    response = put_item(CATEGORIES_TABLE, {
        'name': name,
        'id': id
    })
    return response


def getCategories():
    response = client.scan(TableName=CATEGORIES_TABLE)
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = client.scan(TableName=CATEGORIES_TABLE,
                               ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return unmarshall_array(data)


def deleteCategory(id):
    response = delete_item(CATEGORIES_TABLE, {'id': id})
    return response
