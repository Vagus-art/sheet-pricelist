import json
from responses import success_response
from itemsService import getItems, postItem, updateItem, deleteItem


def handler(event, context):
    body = json.loads(event['body']) if event['body'] else None
    if (event['httpMethod']=='GET'):
        categoryId = event['queryStringParameters']['categoryId'] if event['queryStringParameters'] else None;
        response = getItems(categoryId)
        return success_response(response)
    elif (event['httpMethod']=='POST'):
        categoryId = body['categoryId'];
        name = body['name'];
        response = postItem(categoryId,name);
        return success_response(response)
    elif (event['httpMethod']=='PUT'):
        id = body['id'];
        categoryId = body['categoryId'];
        name = body['name'];
        created = body['created'];
        response = updateItem(id, created, categoryId, name);
        return success_response(response)
    elif (event['httpMethod']=='DELETE'):
        id = body['id'];
        created = body['created'];
        response = deleteItem(id, created);
        return success_response(response)

    