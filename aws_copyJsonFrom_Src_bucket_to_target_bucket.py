from __future__ import print_function

import json
import boto3
import os
import sys
import uuid
import urllib

print("Loading function")
s3 = boto3.client('s3')

def lambda_handler(event, context):
	source_bucket = event['Records'][0]['s3']['bucket']['name']
	key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
	target_bucket = 'atul-bucket-1-output-csv-files'
	copy_source = {'Bucket' : source_bucket, 'Key':key}

	try :
		print("Waiting for the file persist ..")
		waiter = s3.get_waiter('object_exists')
		waiter.wait(Bucket=source_bucket, Key=key)
		print("copying")
		s3.copy_object(Bucket=target_bucket, Key=key, CopySource = copy_source)

	except Exception as e:
		print(e)
		raise(e)
	
#atul-bucket-1-input-json-files
#atul-bucket-1-output-csv-files
