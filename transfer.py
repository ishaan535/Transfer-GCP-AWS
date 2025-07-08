import os
from google.cloud import storage as gcs
import boto3
gcp_bucket_name = os.environ['GCP_BUCKET_NAME']  
s3_bucket_name = os.environ['S3_BUCKET_NAME']
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
region_name = os.environ['REGION_NAME']
gcp_client=gcs.Client()
buckets=list(gcp_client.list_buckets())
print("GCP Bucket List:")
for b in buckets:
    print(b.name)
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
response = s3_client.list_buckets()
print("AWS Bucket List:")
for b in response['Buckets']:
    print(b['Name'])

blobs=gcp_client.list_blobs(gcp_bucket_name)
print("Blob Names:")
for blob in blobs:
    print(f"Blob: {blob.name}")
    data = blob.download_as_bytes()
    s3_key = blob.name
    print(f"s3 key: {s3_key}")
    s3_client.put_object(Bucket=s3_bucket_name, Key=s3_key, Body=data)
    print(f"{s3_key} Uploaded")

print("Transfer Complete")