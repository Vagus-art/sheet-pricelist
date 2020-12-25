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
        unit = body['unit'];
        price = body['price'];
        response = postItem(categoryId,name,unit,price);
        return success_response(response)
    elif (event['httpMethod']=='PUT'):
        id = body['id'];
        categoryId = body['categoryId'];
        name = body['name'];
        unit = body['unit'];
        price = body['price'];
        created = body['created'];
        response = updateItem(id, created, categoryId, name, unit, price);
        return success_response(response)
    elif (event['httpMethod']=='DELETE'):
        id = body['id'];
        created = body['created'];
        response = deleteItem(id, created);
        return success_response(response)

    