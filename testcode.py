import requests
import json

url="http://mahikanthnag.net23.net/solenoid_on_off.php"
payload={"Mode":"Manual","CropName":"Groundnut","ButtonStatus":"OFF"}
headers={"content-type":"application/json"}

response=requests.post(url,data=json.dumps(payload),headers=headers)

print response
