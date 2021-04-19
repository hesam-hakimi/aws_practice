import boto3
import os
import time
from boto3.s3.transfer import TransferConfig
import threading

FILEPATH = "C:\\Users\\hesam\\Downloads\\Video\\thread.mp4"
BUCKET = "test-hesam-for-02"
KEY_NAME = 'thread.mp4'


def s3_source():
    return boto3.resource('s3')


def s3_client():
    return boto3.client('s3')


def s3_upload_file(file_path=FILEPATH):
    return s3_client().upload_file(file_path, BUCKET, KEY_NAME)


def upload_big_file(file_path=FILEPATH):
    configuration = TransferConfig(multipart_threshold=512*8,
                                   multipart_chunksize=512*8, io_chunksize=2*256, use_threads=True)
    s3_source().meta.client.upload_file(FILEPATH, BUCKET, KEY_NAME,
                                        ExtraArgs={"ACL": "public-read",
                                                   "ContentType": "video"},
                                        Config=configuration,
                                        Callback=PercentageCompleted(file_path)

                                        )


class PercentageCompleted(object):
    def __init__(self, file_path):
        self._file_path = file_path
        self._size = os.path.getsize(file_path)
        self._downloaded = 0
        self.lock = threading.Lock()

    def __call__(self, file_downloaded):
        with self.lock as _lock:
            self._downloaded += file_downloaded
            self._percent_completed = (self._downloaded / self._size)*100
            print(f"{self._percent_completed:0.2f} %")


if __name__ == "__main__":
    upload_big_file()
