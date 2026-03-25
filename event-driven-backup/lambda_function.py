import json
import urllib.parse
import boto3

s3 = boto3.client('s3')

DEST_BUCKET = 'mxali-backup-files'  # change this to your backup bucket name

def lambda_handler(event, context):
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        source_key = urllib.parse.unquote_plus(record['s3']['object']['key'])

        copy_source = {
            'Bucket': source_bucket,
            'Key': source_key
        }

        s3.copy_object(
            Bucket=DEST_BUCKET,
            Key=source_key,
            CopySource=copy_source
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Files copied successfully')
    }