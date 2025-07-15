import json
THRESHOLD = 0.7
def lambda_handler(event, context):
    body = event["body"]
    inferences = json.loads(body["inferences"]) 

    # Check if any inference exceeds the threshold
    meets_threshold = max(inferences) > THRESHOLD

    # If the threshold is not met, raise an exception
    if not meets_threshold:
        raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }