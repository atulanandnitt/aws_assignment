from __future__ import print_function

import boto3
import os
import sys
import uuid
import urllib
import json
import csv


s3_client = boto3.client('s3')

#convert json data into csv file
def jsonToCsv(download_path, upload_path) :
   with open(download_path, 'r') as f:
       jsonData = json.load(f)
       
   csvData = open(upload_path, 'w')
   csvwriter = csv.writer(csvData)
   count = 0

   for data in jsonData:
         if count == 0:
                header = data.keys()
                csvwriter.writerow(header)
                count += 1
         csvwriter.writerow(data.values())
   csvData.close()
       

      
def lambda_handler(event, context):
   for record in event['Records']:
       bucket = record['s3']['bucket']['name']
       dest_bucket = 'atul-bucket-1-output-csv-files'
       key = record['s3']['object']['key'] 

       download_path = '/tmp/{}'.format(key.split("/")[-1])
       
       # derive upload path and destination bucket key
       upload_path = '/tmp/{}.csv'.format(key.split("/")[-1].split(".")[-2])
       dest_key = '{}.csv'.format(key.split("/")[-1].split(".")[-2])
       
       s3_client.download_file(bucket, key, download_path)
       jsonToCsv(download_path, upload_path)
       s3_client.upload_file(upload_path, dest_bucket, dest_key)
