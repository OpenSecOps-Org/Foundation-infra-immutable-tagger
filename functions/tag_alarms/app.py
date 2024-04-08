import os
import boto3

sts_client = boto3.client('sts')

ROLE_TO_ASSUME = os.environ['ROLE_TO_ASSUME']
PREFIXES = os.environ['PREFIXES'].split(',')


def lambda_handler(data, _context):
    print("Data: ", data)

    account_id = data['AccountId'].strip('"')
    print(f'Processing account {account_id}...')

    client = get_client('cloudwatch', account_id)

    alarms = get_alarms(client)

    for alarm in alarms:
        put_tags(client, alarm)

    return True


def get_alarms(client):
    result = []
    paginator = client.get_paginator('describe_alarms')
    for prefix in PREFIXES:
        for page in paginator.paginate(AlarmNamePrefix=prefix):
            result.extend(page['MetricAlarms'])  # Assuming we're dealing with Metric Alarms; adjust if needed
    return result


def put_tags(client, alarm):
    print(alarm['AlarmName'])
    response = client.tag_resource(
        ResourceARN=alarm['AlarmArn'],
        Tags=[
            {
                'Key': 'infra:immutable',
                'Value': 'true'
            },
        ]
    )


def get_client(client_type, account_id, role=ROLE_TO_ASSUME):
    other_session = sts_client.assume_role(
        RoleArn=f"arn:aws:iam::{account_id}:role/{role}",
        RoleSessionName=f"tag_cloudwatch_alarms_{account_id}"
    )
    access_key = other_session['Credentials']['AccessKeyId']
    secret_key = other_session['Credentials']['SecretAccessKey']
    session_token = other_session['Credentials']['SessionToken']
    return boto3.client(
        client_type,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session_token
    )
