import json
f=open("tech/001.txt","r")
dic ={}
stop_words = ['The','In','At','This','These','However','Of','If','It']
for i in f:
	li=i.split(' ')
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
dic2['001ne']=dic
js = json.dumps(dic2)
print(js)