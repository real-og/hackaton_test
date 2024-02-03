import requests

url = 'https://api.nbrb.by/exrates/rates/dynamics/{cur_id}'
# no more than 365 days in advance
headers = {'startDate': '2024-01-01',
           'endDate': '2024-01-10'
           }

response = requests.get(url, params=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
