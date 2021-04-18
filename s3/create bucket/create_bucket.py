import boto3
import logging
from botocore.exceptions import ClientError
import os


def s3_client():
    return boto3.client("s3")


def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            result = s3_client().create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": "us-east-2"}
            )
            return result
        else:
            result = s3_client().create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=region
            )
            return result
    except ClientError as e:
        logging.error(e)
        return False


create_bucket('test-hesam-for-02')
