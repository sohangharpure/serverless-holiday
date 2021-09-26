import json, boto3, uuid

def save(event, context):
    print("Event: %s" % json.dumps(event))
    holidays = event['holidays']
    client = boto3.resource('dynamodb')
    table = client.Table('Holidays')
    for holiday in holidays:
        response = table.put_item(
           Item={
               'id' : str(uuid.uuid4()),
               'name': holiday['name'],
               'date': holiday['date'],
               'country': holiday['country']
           }
        )
        print(response)
    return {
       'statusCode': 201,
       'body': 'Holidays added'
    }
