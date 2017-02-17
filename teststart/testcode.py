import requests
import json
import urllib2

def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

while(internet_on()==0):
	pass


url="http://mahikanthnag.net23.net/solenoid_on_off.php"
payload={"Mode":"Manual","CropName":"Groundnut","ButtonStatus":"OFF"}
headers={"content-type":"application/json"}

response=requests.post(url,data=json.dumps(payload),headers=headers)

print response

