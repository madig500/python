#  Class required to convert text retrieved into a dic

import requests


url='http://ip-api.com/json/'

def get_location():
    ip_address = "220.185.3.43"
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    return location_data


print(get_location())
