import uuid
import boto3
from database import unmarshall_array, put_item, delete_item
from boto3.dynamodb.conditions import Attr
from constants import ITEMS_TABLE

client = boto3.client('dynamodb')


def postItem(categoryId, name):
    response = put_item(ITEMS_TABLE, {
        'name': name,
        'categoryId': categoryId,
        'id': str(uuid.uuid4())
    })
    return response


def updateItem(id, categoryId, name):
    response = put_item(ITEMS_TABLE, {
        'name': name,
        'categoryId': categoryId,
        'id':  id
    })
    return response


def getItems(categoryId):
    FilterItems = 'categoryId = :categoryIdValue'
    ExpressionAttributeValues = {
        ':categoryIdValue': {'S': categoryId}
    }
    response = client.scan(TableName=ITEMS_TABLE, FilterExpression=FilterItems,
                           ExpressionAttributeValues=ExpressionAttributeValues)
    data = response['Items']
    while 'LastEvaluatedKey' in response:
        response = client.scan(
            TableName=ITEMS_TABLE, ExclusiveStartKey=response['LastEvaluatedKey'], FilterExpression=FilterItems, ExpressionAttributeValues=ExpressionAttributeValues)
        data.extend(response['Items'])
    return unmarshall_array(data)


def deleteItem(id):
    response = delete_item(ITEMS_TABLE, {
        'id': id
    })
    return response
