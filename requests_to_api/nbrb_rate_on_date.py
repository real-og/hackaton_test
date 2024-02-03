import requests

url = 'https://api.nbrb.by/exrates/rates[/{cur_id}]'
headers = {'ondate': '2023-01-10'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
