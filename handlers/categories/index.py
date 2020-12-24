import json
from responses import success_response
from categoriesService import getCategories, postCategory, updateCategory, deleteCategory


def handler(event, context):
    body = json.loads(event['body']) if event['body'] else None
    if (event['httpMethod']=='GET'):
        response = getCategories()
        return success_response(response)
    elif (event['httpMethod']=='POST'):
        name = body['name'];
        response = postCategory(name);
        return success_response(response)
    elif (event['httpMethod']=='PUT'):
        id = body['id'];
        name = body['name'];
        response = updateCategory(id, name);
        return success_response(response)
    elif (event['httpMethod']=='DELETE'):
        id = body['id'];
        response = deleteCategory(id);
        return success_response(response)
    