import json
from categoriesService import getCategories, postCategory, updateCategory


def handler(event, context):
    if (event['httpMethod']=='GET'):
        response = getCategories()
        data = {
            'output': json.dumps(response)
        }
        return {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
    if (event['httpMethod']=='POST'):
        categoryName = event['body']['categoryName'];
        response = postCategory(categoryName);
        data = {
            'output': json.dumps(response)
        }
        return {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
    if (event['httpMethod']=='PUT'):
        id = event['body']['id'];
        categoryName = event['body']['categoryName'];
        response = updateCategory(id, categoryName);
        data = {
            'output': json.dumps(response)
        }
        return {'statusCode': 200,
                'body': json.dumps(data),
                'headers': {'Content-Type': 'application/json'}}
    