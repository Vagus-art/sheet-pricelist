import uuid
import boto3
CATEGORIES_TABLE = os.getenv('CATEGORIES_TABLE')
client = boto3.client('dynamodb')


def postCategory(category_name):
    response = client.put_item(
            TableName=CATEGORIES_TABLE,
            Item={
                    'name':{'S':category_name},
                    'id':{'S':str(uuid.uuid4())}
                }
    )
    return response;

def updateCategory(id, category_name):
    response = client.put_item(
            TableName=CATEGORIES_TABLE,
            Item={
                    'name':{'S':category_name},
                    'id':{'S':id}
                }
    )
    return response;
def getCategories():
    response = client.scan(TableName=CATEGORIES_TABLE)
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(TableName=CATEGORIES_TABLE,ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return response;