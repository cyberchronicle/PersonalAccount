import boto3
from botocore.client import BaseClient
from botocore.exceptions import ClientError

from app.config import cfg

s3_client: BaseClient = boto3.client(
    "s3",
    endpoint_url=cfg.minio_url,
    aws_access_key_id=cfg.minio_root_user,
    aws_secret_access_key=cfg.minio_root_password
)
bucket_name = cfg.s3_bucket_name
try:
    s3_client.head_bucket(Bucket=bucket_name)
except ClientError:
    # Если бакет не существует, создаем его
    s3_client.create_bucket(Bucket=bucket_name)


def upload_file_to_s3(file) -> str:
    s3_client.upload_fileobj(file.file, bucket_name, file.filename)
    link = s3_client.generate_presigned_url('get_object',
                                            Params={'Bucket': bucket_name, 'Key': file.filename},
                                            ExpiresIn=3600)
    return link