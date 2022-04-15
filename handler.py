import json
import boto3

def handler_main(event, context):

    client = boto3.client('comprehend')
    print("Received event: " + json.dumps(event, indent=2))
    body = event["body"]
    sentiment = client.detect_sentiment(LanguageCode = "en", Text = body["text"])
    return json.dumps(sentiment)


