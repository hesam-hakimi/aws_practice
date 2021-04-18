import boto3
from botocore.exceptions import ClientError
import logging


def client_s3():
    return boto3.client("s3")


def create_bucket(bucket_name, region=None):
    try:
        result = client_s3().create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-2' if region is None else region
            }

        )
        return result
    except ClientError as e:
        logging.error(e)
        return False


def delete_bucket(bucket_name):
    return client_s3().delete_bucket(
        Bucket=bucket_name
    )


if __name__ == "__main__":
    BUCKET_NAME = "sample-for-demo-version-1-0-1"
    # print(create_bucket(bucket_name=BUCKET_NAME))
    print(delete_bucket(bucket_name=BUCKET_NAME))
