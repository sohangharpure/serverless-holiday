import json, boto3
from boto3.dynamodb.conditions import Key,Attr

def is_holiday(event, context) :
    print("Event: %s" % json.dumps(event))
    client = boto3.resource('dynamodb')
    table = client.Table('Holidays')
    response = table.query(
        IndexName='date-index',
        KeyConditionExpression=Key('date').eq(event['date']),
        FilterExpression=Attr('country').eq(event['country'])
    )
    print(response)
    if 'Items' in response and response['Items']:
        return response['Items']
    else:
        return {
           'statusCode': '404',
           'body': 'Not found'
        }
