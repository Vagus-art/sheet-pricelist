import json
from itemsService import getItems, postItem, updateItem, deleteItem


def handler(event, context):
    if (event['httpMethod']=='GET'):
        categoryId = event['queryStringParameters']['categoryId'];
        response = getItems(categoryId)
        return {'statusCode': 200,
                'body': json.dumps(response),
                'headers': {'Content-Type': 'application/json'}}
    elif (event['httpMethod']=='POST'):
        categoryId = event['body']['categoryId'];
        name = event['body']['name'];
        response = postItem(categoryId,name);
        return {'statusCode': 200,
                'body': json.dumps(response),
                'headers': {'Content-Type': 'application/json'}}
    elif (event['httpMethod']=='PUT'):
        id = event['body']['id'];
        categoryId = event['body']['categoryId'];
        name = event['body']['name'];
        response = updateItem(id, categoryId, name);
        return {'statusCode': 200,
                'body': json.dumps(response),
                'headers': {'Content-Type': 'application/json'}}
    elif (event['httpMethod']=='DELETE'):
        id = event['body']['id'];
        response = deleteItem(id);
        return {'statusCode': 200,
                'body': json.dumps(response),
                'headers': {'Content-Type': 'application/json'}}

    