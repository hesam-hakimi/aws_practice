import boto3
from botocore.exceptions import ClientError
import logging


def s3_client():
    return boto3.client('s3')


def create_bucket(bucket_name, region=None):
    if bucket_name.contain('_'):
        raise Error("")
    try:

        if region is None:
            result = s3_client().create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LocationConstraint": "us-east-2"}
            )

        else:
            result = s3_client().create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={"LcationConstraint": region}
            )
        return result
    except ClientError as e:
        logging.error(e)
        return False


create_bucket('test-create-bucket-v01')
