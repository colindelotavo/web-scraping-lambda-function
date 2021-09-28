import json
import urllib.parse
import boto3
import requests
import csv
from bs4 import BeautifulSoup

print('Loading function')

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    # bucket_get = event['Records'][0]['s3']['bucket']['name']
    # bucket_put = s3.Bucket('web-scrape-results')
    source_bucket = s3.Bucket('web-scrape-files')
    destination_bucket = s3.Bucket('web-scrape-results')
    # file_name = info.get('object', {}).get('key')
    # key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        # response = s3.get_object(Bucket=bucket, Key=key)
        results = s3.Object('web-scrape-results', 'results.csv').put(Body=open('/tmp/results.csv', 'rb'))
        # s3.Object('mybucket', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))

        # print("CONTENT TYPE: " + response['ContentType'])
        # return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket_get))
        raise e

    # header, rows = read(file_name)
    # for index, row in enumerate(rows):
    #     try:
    #         desc, title = scrape(row[0])
    #         print(f'Scraping {row[0]}...', end=' ')
    #         rows[index][1] = desc
    #         rows[index][2] = title
    #         print('Done.')
    #     except Exception as e:
    #         print(e)
    # write(results, header, rows)
    print(source_bucket, destination_bucket)

def read(file):
    rows = []
    with open(file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            rows.append(row)
    return header, rows

def write(results_file, header, rows):
    # # with open('results.csv', 'w') as f:
    # with open(results_file, 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(header)
    #     for row in rows:
    #         writer.writerow(row)
    print(results_file, header, rows)
