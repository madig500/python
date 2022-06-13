import requests

#  Class required to convert text retrieved into a dic
import json

url='https://reqres.in/api/users'
myjson={ 'name' :'Rolando', 'job' : 'Developer in Python'}

#print(payload)
#  jason=payload is sending the data required to retrieve information from SERVER
#x = requests.post(url, json = myjson)
#r = requests.post(url,jason=payload)

#print(x.text)

hashdicc=dict()
hashdicc={}

idjason={'id' : '492'}
x = requests.post(url, json = myjson)


# CONVIERTE EL RESULTADO DE STRING A DICCIONARIO
hashdicc= json.loads(x.text)



# Try to Converts received text into a hash dicctionary --- but fall back to string
#hashdicc=x.text
#print(type(hashdicc))

for key, value in hashdicc.items() :
    print(key, ' : ', value)
