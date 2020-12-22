import uuid
import boto3
from database import unmarshall_array, put_item, update_item, delete_item
from boto3.dynamodb.conditions import Attr
from constants import ITEMS_TABLE
import dynamo_json
from datetime import datetime

now = datetime.now() 

client = boto3.client('dynamodb')

def postItem(categoryId, name):
    response = put_item(ITEMS_TABLE, {
        'name': name,
        'categoryId': categoryId,
        'id': str(uuid.uuid4()),
        'created': now.strftime("%m/%d/%Y, %H:%M:%S")
    })
    return response

def updateItem(id, created, categoryId, name):
    response = update_item(
        ITEMS_TABLE,
        {'id':  id, 'created': created},
        'SET #name = :name, #categoryId = :categoryId',
        {'#name': 'name', '#categoryId': 'categoryId'},
        {':name': name, ':categoryId': categoryId})
    return response


def getItems(categoryId):

    if categoryId:
        query_kwargs = {
            'TableName':ITEMS_TABLE,
            'IndexName':'category',
            'Select': 'ALL_PROJECTED_ATTRIBUTES',
            'KeyConditionExpression' : '#categoryId = :categoryId',
            'ExpressionAttributeNames': {
                '#categoryId': 'categoryId'
            },
            'ExpressionAttributeValues': dynamo_json.marshall({':categoryId':categoryId})
        }
        response = client.query(
            **query_kwargs
        )
        data = response['Items']
        while 'LastEvaluatedKey' in response:
            response = client.query(
                **query_kwargs, ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
        return unmarshall_array(data)
    else:
        response = client.scan(TableName=ITEMS_TABLE)
        data = response['Items']
        while 'LastEvaluatedKey' in response:
            response = client.scan(
                TableName=ITEMS_TABLE, ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])
        return unmarshall_array(data)


def deleteItem(id):
    response = delete_item(ITEMS_TABLE, {
        'id': id
    })
    return response
