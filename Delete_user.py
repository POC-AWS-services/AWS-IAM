__Author__ = 'Prameet Bisht'
__Version__ = "0.0.1"
__Email__ = "myprameet09@gmail.com"
__Github__ = "https://github.com/orgs/POC-AWS-services/dashboard"

import boto3

# Create IAM client
iam = boto3.client('iam')

# Delete a user
iam.delete_user(
    UserName='IAM_USER_NAME'
)