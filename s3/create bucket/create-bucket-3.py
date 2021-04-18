import logging
import boto3
from botocore.exceptions import ClientError
import json
Bucket_Name='test-for-test-o2'
def s3_client ():
    return boto3.client("s3")

def create_bucket(bucket_name, region=None):
 
    try:
        result=s3_client().create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint':'us-east-2'if region is None else region
            }
        )
        return result
    except ClientError as e:
        logging.error(e)
        return False

def create_bucket_policy(bucket_name):
    bucket_policy={
        'Version':'2012-10-17',#this is not the version of the the policy but the version of AWS model policy 
        'Statement':[
            {
                "Sid":"AddPerm",
                'Effect':"Allow",
                "Principal":"*",# who has the access to this bucket
                "Action":['s3:*'],#s3:GetObject , s3:PutObject, s3:DeleteObject, <= what kind of action he can do
                "Resource":[F'arn:aws:s3:::{bucket_name}/*']#on which 
                 
            }
        ]
    }
    
    policy_string=json.dumps(bucket_policy)
    return s3_client().put_bucket_policy(
        Bucket=Bucket_Name,
        Policy=policy_string
    )
if __name__=='__main__':
    # print (create_bucket("test-for-test-o2"))
    print (create_bucket_policy(Bucket_Name))
