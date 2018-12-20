import boto3
from .base import BackendBase
from pathlib import Path
import logging

class AWSBackend(BackendBase):
    def __init__(self, endpoint_url, bucket):
        session = boto3.session.Session()
        self.s3 = session.client(
            service_name='s3',
            endpoint_url=endpoint_url
        )
        self.bucket=bucket

    def copy_from_backend(self, src_path, dst_path):
        get_object_response = self.s3.get_object(Bucket=self.bucket, Key=src_path)
        dst_path = Path(dst_path)
        if dst_path.exists():
            logging.info("File {} exists and will be rewritten!".format(dst_path))
        with dst_path.open(mode="wb") as f:
            f.write(get_object_response['Body'].read())

    def copy_to_backend(self, src_path, dst_path):
        self.s3.upload_file(src_path, self.bucket, dst_path)


    def list_uploaded(self, path):
        #TODO path
        files = []
        for key in self.s3.list_objects(Bucket=self.bucket)['Contents']:
            files.append(key)
        return files
