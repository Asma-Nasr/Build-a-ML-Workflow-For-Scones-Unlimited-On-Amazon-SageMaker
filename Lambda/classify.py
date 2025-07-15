import json
import base64
import boto3

ENDPOINT = 'image-classification-2025-07-15-03-49-06-780'

def lambda_handler(event, context):

    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])

    runtime= boto3.client('runtime.sagemaker')

    inferences = runtime.invoke_endpoint(EndpointName=ENDPOINT,
                                ContentType='image/png',
                                       Body=image)

    # We return the data back to the Step Function    
    event['inferences'] = inferences['Body'].read().decode('utf-8')
    return {
        'statusCode': 200,
        'body': event 
    }