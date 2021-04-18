import boto3


def s3_client():
    return boto3.client("s3")


def bucket_server_side_encryption(bucket_name):
    return s3_client().put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            "Rules": [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        "SSEAlgorithm": "AES256"
                    }
                }
            ]
        }

    )


if __name__ == "__main__":
    print(bucket_server_side_encryption("bucket-hesam-1"))
