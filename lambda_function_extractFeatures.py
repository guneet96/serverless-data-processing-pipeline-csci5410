import urllib
import json
import boto3

def lambda_handler(event, context):
    print("event is :", event)    
    s3 = boto3.client("s3",aws_access_key_id='',aws_secret_access_key='')
    ss3 = boto3.resource('s3')
    bucket = event['Records'][0]
    print("bucket is :")
    print(bucket)
    file_name = str(bucket["s3"]["object"]["key"])
    print("file name is :", file_name)
    fileObj = s3.get_object(Bucket = "sampledatab00843346", Key=file_name)
    file_content = fileObj["Body"].read().decode("utf-8")
    # print(file_content)
    dic ={}
    stop_words = ['The','In','At','This','These','However','Of','If','It']
    print("the content type of file content is : ")
    print(file_content)
    li = file_content.split(' ')
    for j in li:
        if j[0].isupper() and j not in stop_words:
            j=j.strip()
            if j[-1].islower() == False and j[-1].isupper() == False:
                j=j[0:-1]
            if j not in dic:
                dic[j]=1
            else:
                dic[j]+=1
    dic2 = {}
    fn = file_name[0:3] + "ne"
    dic2[fn]=dic
    js_tags = json.dumps(dic2)
    print(js_tags)
    fn+=".txt"
    tag_bucket = "tagsb00843346"
    # f = open(fn, "rb")
    ss3.Bucket(tag_bucket).put_object(Key=fn,Body=str(js_tags))