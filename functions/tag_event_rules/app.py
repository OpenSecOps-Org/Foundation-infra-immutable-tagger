import os
import json
import botocore
import boto3


sts_client = boto3.client('sts')

ROLE_TO_ASSUME = os.environ['ROLE_TO_ASSUME']
PREFIXES = os.environ['PREFIXES'].split(',')


def lambda_handler(data, _context):
    print("Data: ", data)

    account_id = data['AccountId'].strip('"')
    print(f'Processing account {account_id}...')

    client = get_client('events', account_id)

    event_buses = get_event_buses(client)

    rules = get_rules(client, event_buses)

    for rule in rules:
        put_tags(client, rule)

    return True


def get_event_buses(client):
    result = []
    response = client.list_event_buses()
    for event_bus in response['EventBuses']:
        result.append(event_bus['Name'])
    return result


def get_rules(client, event_buses):
    result = []
    for event_bus in event_buses:
        for prefix in PREFIXES:
            response = client.list_rules(
                NamePrefix=prefix,
                EventBusName=event_bus
            )
        result.extend(response['Rules'])
    return result


def put_tags(client, rule):
    print(rule['Name'])
    response = client.tag_resource(
        ResourceARN=rule['Arn'],
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
        RoleSessionName=f"tag_event_rules_{account_id}"
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
