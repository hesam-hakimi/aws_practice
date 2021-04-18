import boto3
import os


def upload_file(path=None, bucket='bucket-hesam-1', key='upload-small.py'):
    if path is None:
        path = os.path.dirname(__file__)+r"/upload-small.py"
        return boto3.client('s3').upload_file(path, bucket, key)


upload_file()
