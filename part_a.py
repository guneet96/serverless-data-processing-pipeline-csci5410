import boto3
import time
# initiating the resource variable
s3 = boto3.resource('s3')
for i in s3.buckets.all():
	print(i.name)
	b=i.name
	break
# name of first bucket created through console


fn = 1
for i in range(1,402):
	fname="tech/"
	if i < 10:
		fname += "00" + str(i)
	elif i < 100:
		fname += "0" + str(i)
	else:
		fname += str(i)
	fname+=".txt"
	print(fname[5:])
	f = open(fname, "rb")
	s3.Bucket(b).put_object(Key=fname[5:],Body=f)
	time.sleep(0.1)

