import requests
import json
data={'name':'pratik'}
resp=requests.get("https://httpbin.org/get",params=json.dumps(data))
print(resp.status_code)
r=resp.json()
print(r)
# print(dir(resp))
# print(json.loads(resp.cont))
