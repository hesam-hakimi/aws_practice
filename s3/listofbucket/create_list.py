import boto3
import botocore


def client_s3():
    return boto3.client("s3")


def view_list_bucket():
    return [x["Name"] for x in client_s3().list_buckets()["Buckets"]]


if __name__ == "__main__":
    print(view_list_bucket())
