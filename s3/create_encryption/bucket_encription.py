import boto3


def s3_client():
    return boto3.client("s3")


def bucket_serverside_encryption(bucket_name):
    s3_client().put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration=[
            {
                "Rules": [
                    {
                        "ApplyServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "AES256"
                        }
                    }
                ]
            }
        ]
    )
