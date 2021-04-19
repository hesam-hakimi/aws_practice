import boto3
import time
from boto3.s3.transfer import TransferConfig
import os
import threading
import sys

FILEPATH = "C:\\Users\\hesam\\Downloads\\Video\\thread.mp4"
BUCKET = "test-hesam-for-02"
KEY_NAME = 'thread.mp4'


def s3_source():
    return boto3.resource("s3")


def upload_big_data(file_path=FILEPATH):
    configuration = TransferConfig(multipart_threshold=1024*25, max_concurrency=10,
                                   multipart_chunksize=1024*25, use_threads=True)
    s3_source().meta.client.upload_file(
        FILEPATH, BUCKET, KEY_NAME,
        ExtraArgs={"ACL": "public-read", "ContentType": "Video"},
        Config=configuration,
        Callback=ProgressPercentage(file_path)


    )


class ProgressPercentage (object):
    def __init__(self, file_path):
        self._name = file_path
        self._size = float(os.path.getsize(file_path))
        self.dowloaded = 0
        self.lock = threading.Lock()
        self._start = time.perf_counter()

    def __call__(self, size):
        with(self.lock) as _lock:
            self.dowloaded += size
            self.percentage = round((self.dowloaded/self._size), 4)*100
            self.duration = round(time.perf_counter()-self._start, 2)
        # sys.stdout.write(F"   {self.percentage}%  completed...\t")
        # sys.stdout.flush()
        print(F"{self.percentage:0.2f}%  completed...{self.duration}",
              sep='-', flush=False)


if __name__ == "__main__":
    upload_big_data()
