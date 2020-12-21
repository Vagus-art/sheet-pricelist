import json
from responses import success_response
from itemsService import getItems, postItem, updateItem, deleteItem


def handler(event, context):
    if (event['httpMethod']=='GET'):
        categoryId = event['queryStringParameters']['categoryId'] if event['queryStringParameters'] else None;
        response = getItems(categoryId)
        return success_response(response)
    elif (event['httpMethod']=='POST'):
        categoryId = json.loads(event['body'])['categoryId'];
        name = json.loads(event['body'])['name'];
        response = postItem(categoryId,name);
        return success_response(response)
    elif (event['httpMethod']=='PUT'):
        id = json.loads(event['body'])['id'];
        categoryId = json.loads(event['body'])['categoryId'];
        name = json.loads(event['body'])['name'];
        response = updateItem(id, categoryId, name);
        return success_response(response)
    elif (event['httpMethod']=='DELETE'):
        id = json.loads(event['body'])['id'];
        response = deleteItem(id);
        return success_response(response)

    