import boto3 
client = boto3.client('s3')
response = client.list_objects_v2(
	Bucket='mi-bucket-yorus-3',
	#Prefix='string'
)

for key in (response['Contents']):
    print(key)
	