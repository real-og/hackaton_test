import banks
import requests

url = banks.currencies['nbrb']  # 'nbrb', 'alfabank', 'belarusbank'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
