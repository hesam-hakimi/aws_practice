import boto3


def list_bucket():
    return [x['Name'] for x in boto3.client("s3").list_buckets()["Buckets"]]


print(list_bucket())
