# Infra Immutable Tagger

Some CloudFormation resource types do not support tags, even though the underlying API does.
This is a solution to this problem: when an account is created, the trigger function detects
it and schedules the account for processing. Also, a cron task is scheduled to process all
accounts once a day.

Accounts are processed by a step machine which runs processing of all accounts in parallel.
In the current implementation, the step machine performs the following tasks: 

1. It looks for EventBridge Rules deployed by the Foundational installations by name. If they
   begin with "INFRA-" or "StackSet-INFRA" or any other configurable prefix, then they are
   tagged with the list of tags specified. (Check the parameters for the details.)

2. It looks for CloudWatch alarms following the same naming scheme and tags them in the same
   way.

In future, other resources may be tagged in the same way as necessary.

This application, deployed in the main organisation account in your main region, is triggered by 
the "new account SNS" topic. It runs in the org account and assumes a system cross-account 
role in the target account to do its work.

NB: The lambda can also be triggered manually. If you provide it with input data of the form:

```
{"AccountId": "123456789012"}
```

the account with the given ID will be processed. If you, on the other hand, provide it with the following data:

```
{"AccountId": "ALL"}
```

then all organisation accounts will be processed. This is useful during initial setup.


## Deployment

First make sure that your SSO setup is configured with a default profile giving you AWSAdministratorAccess
to your AWS Organizations administrative account. This is necessary as the AWS cross-account role used 
during deployment only can be assumed from that account.

```console
aws sso login
```

Then type:

```console
./deploy
```
