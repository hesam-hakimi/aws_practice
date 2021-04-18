import boto3
import json


BUCKET_NAME = "test-for-test-o2"


def create_bucket_policy(BucketName):
    BucketPolicy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
                "Resource":[F"arn:aws:s3:::{BucketName}/*"]

            }
        ]
    }
    policy_string = json.dumps(BucketPolicy)
    return boto3.client("s3"). put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=policy_string
    )


if __name__ == "__main__":
    print(create_bucket_policy(BUCKET_NAME))
