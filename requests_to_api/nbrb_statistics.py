import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://api.nbrb.by/exrates/rates/dynamics/{Cur_ID}'
# no more than 365 days in advance
headers = {'startDate': '2024-01-01',
           'endDate': '2024-01-10'
           }

response = requests.get(url, params=headers)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    average_rate = df['Cur_OfficialRate'].mean()
    max_rate = df['Cur_OfficialRate'].max()
    min_rate = df['Cur_OfficialRate'].min()

    print('Average value: ', average_rate)
    print('Max value: ', max_rate)
    print('Min value: ', min_rate)

    # Graph
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df['Cur_OfficialRate'].plot(title='Official Exchange Rate Over Time', xlabel='Date', ylabel='Exchange Rate')
    plt.show()

else:
    print(f"Error {response.status_code}: {response.text}")
