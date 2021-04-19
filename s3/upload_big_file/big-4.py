import boto3
import botocore.exceptions as aws_exception
import time
import os
import sys
import threading
import logging
import json


def s3_client():
    return boto3.client("s3")


def s3_resource():
    return boto3.resource('s3')


def create_bucket(bucket_name, region="us-east-2"):

    try:
        result = s3_client().create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                "LocationConstraint": region
            }
        )
        return result
    except aws_exception.ClientError as e:
        logging.error(e)
        return False


def create_bucket_policy(bucket_name):
    BucketPolicy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
                "Resource":[F"arn:aws:s3:::{bucket_name}/*"]

            }
        ]
    }
    BucketPolicy = json.dumps(BucketPolicy)
    try:
        return s3_client().put_bucket_policy(
            Bucket=bucket_name,
            Policy=BucketPolicy
        )

    except aws_exception.ClientError as e:
        logging.error(e)
        return False


def put_bucket_encryption(bucket_name):
    return s3_client().put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    "ApplyServerSideEncryptionByDefault":
                    {"SSEAlgorithm": "AES256"}
                }
            ]
        }
    )


def create_bucket_encryption(bucket_name):
    return s3_client().put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'rules': [
                {
                    'ApplyServerSideEncryptionByDefalt':
                    {
                        "SSEAlgorithm": "AES256"
                    }
                }
            ]
        }
    )


def upload_file_to_s3(file_path, bucket_name, file_name):
    return s3_client().upload_file(
        file_path, bucket_name, file_name
    )


def delete_bucket(bucket_name):
    s3_client().delete_bucket(
        Bucket=bucket_name
    )


def all_file_im_folder(folder_name):
    for _, _, file_names in os.walk(folder_name):
        return file_names
    break


def upload_multiple_file(file_name):
    

if __name__ == "__main__":
    bucket_name = "hesam-bucket-for-demo-v1"
    pic_folder = "D:\\job\\Code\\create_bucket\\ax"
    pic_dir = "D:\\job\\Code\\create_bucket\\ax\\photo-1599662493445-8ab307c0e62e.jpg"
    pic_name = pic_dir.split('\\')[5]
    # print(create_bucket("hesam-bucket-for-demo-v1"))
    # print(create_bucket_policy(bucket_name=bucket_name))
    # print(put_bucket_encryption(bucket_name=bucket_name))
    # print(upload_file_to_s3(pic_dir, bucket_name, pic_name))
