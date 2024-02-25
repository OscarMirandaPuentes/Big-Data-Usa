import boto3

# Retrieve the list of existing buckets
client = boto3.client('s3','us-east-1')
response = client.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

