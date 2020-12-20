import json
from categoriesService import getCategories, postCategory, updateCategory, deleteCategory


def handler(event, context):
    if (event['httpMethod']=='GET'):
        response = getCategories()
        return {'statusCode': 200,
                'body': json.dumps(response),
                'headers': {'Content-Type': 'application/json'}}
    elif (event['httpMethod']=='POST'):
        categoryName = event['body']['categoryName'];
        response = postCategory(categoryName);
        return {'statusCode': 200,
                'body': json.dumps(response),
                'headers': {'Content-Type': 'application/json'}}
    elif (event['httpMethod']=='PUT'):
        id = event['body']['id'];
        categoryName = event['body']['categoryName'];
        response = updateCategory(id, categoryName);
        return {'statusCode': 200,
                'body': json.dumps(response),
                'headers': {'Content-Type': 'application/json'}}
    elif (event['httpMethod']=='DELETE'):
        id = event['body']['id'];
        response = deleteCategory(id);
        return {'statusCode': 200,
                'body': json.dumps(response),
                'headers': {'Content-Type': 'application/json'}}
    