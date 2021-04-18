import boto3
import logging
from botocore.exceptions import ClientError
import json


def s3_client():
    return boto3.client("s3")


def create_bucket(bucket_name, region=None):
    try:
        x = s3_client().create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": 'us-east-2'if region is None else {
                "LocationConstraint": region}
            }

        )
        return x
    except ClientError as e:
        logging.error(e)
        return False


def create_bucket_policy(bucket_name):
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:*"],
                "Resource":[F"arn:aws:s3:::{bucket_name}/*"]

            }
        ]
    }
    policy_string = json.dumps(policy)
    return s3_client().put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string
    )


if __name__ == '__main__':
    # print(create_bucket("this-is-the-second-test-02"))
    print(create_bucket_policy("this-is-the-second-test-02"))
