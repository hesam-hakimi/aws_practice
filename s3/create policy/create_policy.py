import boto3
import json


BUCKET_NAME = "test-for-test-o2"


def create_bucket_policy(bucket_name):
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:*"],
                "Resource":F"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }
    policy_string = json.dumps(bucket_policy)
    return boto3.client('s3').put_bucket_policy(
        Bucket=bucket_name,
        Policy=policy_string
    )


if __name__ == "__main__":
    print(create_bucket_policy(BUCKET_NAME))
