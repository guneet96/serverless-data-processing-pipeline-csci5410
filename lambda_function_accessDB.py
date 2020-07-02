import urllib
import json
import boto3
import pymysql.cursors

def lambda_handler(event, context):
    print("event is :", event)    
    s3 = boto3.client("s3",aws_access_key_id='',aws_secret_access_key='')
    ss3 = boto3.resource('s3')
    bucket = event['Records'][0]
    print("bucket is :")
    print(bucket)
    file_name = str(bucket["s3"]["object"]["key"])
    print("file name is :", file_name)
    fileObj = s3.get_object(Bucket = "tagsb00843346", Key=file_name)
    file_content = fileObj["Body"].read().decode("utf-8")
    print(file_content)
    dic = json.loads(file_content)
    print(dic)
    dic = dic[file_name[0:5]]
    print(dic)
    # Connect to the database
    connection = pymysql.connect(host='csci5410-serverless-assignment3.<private>.rds.amazonaws.com',
								port=3306,
								user='admin',
								password='12345678',
								db='serverless_ass3')
								# charset='utf8mb4',
								# cursorclass=pymysql.cursors.DictCursor)
    cursorObject = connection.cursor()
    for i in dic:
        sql = "INSERT INTO `Assignment3` (`NamedEntity`, `Frequency`) VALUES (%s, %s)"
        cursorObject.execute(sql, (i, str(dic[i])))
    connection.commit()
