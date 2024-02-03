import json
import requests
from datetime import datetime

# date = input('Date no later than 4 days, yyyy-mm-dd: ')
input_date = '2024-01-31'
url = 'https://belarusbank.by/api/kurs_cards'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for date_time in data:
        date_time_object = datetime.strptime(date_time['kurs_date_time'], '%Y-%m-%d %H:%M:%S')
        date_only = date_time_object.strftime('%Y-%m-%d')
        if date_only == input_date:
            formatted_date_time = json.dumps(date_time, indent=2)
            print(formatted_date_time)
            break
    else:
        print('There is no data for this date')

else:
    print(f"Error {response.status_code}: {response.text}")
