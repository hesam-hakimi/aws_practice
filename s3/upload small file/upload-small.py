import os
import boto3


def client_s3():
    return boto3.client("s3")


def upload_file(file_path=None, bucket_name=None, key=None):
    path = os.path.dirname(__file__)+r'\sample1.txt'
    client_s3().upload_file(path, 'bucket-hesam-1', 'sample.txt')


print(upload_file())
