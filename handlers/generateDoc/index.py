from responses import success_response
from generate import generate

def handler(event, context):
    return success_response(generate())
    