import boto3


def delete_bucket(bucket_name):
    return boto3.client().delete_bucket(Bucket=bucket_name)
