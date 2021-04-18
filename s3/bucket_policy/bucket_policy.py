import boto3


def s3_client():
    return boto3.client('s3')


print(s3_client().get_bucket_policy(
    Bucket="test-for-test-o2")["Policy"])  # ["Statement"]
