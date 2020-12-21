from responses import success_response
from categoriesService import getCategories, postCategory, updateCategory, deleteCategory


def handler(event, context):
    if (event['httpMethod']=='GET'):
        response = getCategories()
        return success_response(response)
    elif (event['httpMethod']=='POST'):
        name = json.loads(event['body'])['name'];
        response = postCategory(name);
        return success_response(response)
    elif (event['httpMethod']=='PUT'):
        id = json.loads(event['body'])['id'];
        name = json.loads(event['body'])['name'];
        response = updateCategory(id, name);
        return success_response(response)
    elif (event['httpMethod']=='DELETE'):
        id = json.loads(event['body'])['id'];
        response = deleteCategory(id);
        return success_response(response)
    