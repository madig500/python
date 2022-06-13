import requests

url = 'https://www.w3schools.com/python/demopage.php'
myjson = {'somekey': 'somevalue'}

x = requests.post(url, json = myjson)

#print the response text (the content of the requested file):

print(x.text)
