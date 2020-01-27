#!/usr/bin/env python3.7


import boto3



client = boto3.client('organizations')

account_ids = [account['Id'] for account in client.list_accounts()['Accounts']]



for id in account_ids:

    account_tags = {tag['Key']: tag['Value'] for tag in client.list_tags_for_resource(ResourceId=id)['Tags']}

    print(f"Account ID: {id}, Tags: {account_tags}.")

