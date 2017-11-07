import json

import requirements
import numpy

def hello(event, context):

    n = numpy.random.randint(100)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "randomNumber": n
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

