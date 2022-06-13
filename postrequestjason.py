
#import requests

#data = {'firstname':'John'}

#r = requests.post('https://httpbin.org/post', json=data)
#print(r.text)


# WITH A SERVER THAT REQUIRES HTML REQUESTS
import requests
from requests.structures import CaseInsensitiveDict

url = "https://reqbin.com/echo/post/json"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"

data = """
{
  "Id": 78912,
  "Customer": "Jason Sweet",
  "Quantity": 1,
  "Price": 18.00
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
