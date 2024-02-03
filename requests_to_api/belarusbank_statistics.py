import requests
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://belarusbank.by/api/kurs_cards'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    numeric_columns = ['USDCARD_in', 'USDCARD_out', 'EURCARD_in', 'EURCARD_out', 'RUBCARD_in', 'RUBCARD_out']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

    USDCARD_in_average_rate = df['USDCARD_in'].mean()
    USDCARD_out_average_rate = df['USDCARD_out'].mean()
    EURCARD_in_average_rate = df['EURCARD_in'].mean()
    EURCARD_out_average_rate = df['EURCARD_out'].mean()
    RUBCARD_in_average_rate = df['RUBCARD_in'].mean()
    RUBCARD_out_average_rate = df['RUBCARD_out'].mean()

    USDCARD_in_max_rate = df['USDCARD_in'].max()
    USDCARD_out_max_rate = df['USDCARD_out'].max()
    EURCARD_in_max_rate = df['EURCARD_in'].max()
    EURCARD_out_max_rate = df['EURCARD_out'].max()
    RUBCARD_in_max_rate = df['RUBCARD_in'].max()
    RUBCARD_out_max_rate = df['RUBCARD_out'].max()

    USDCARD_in_min_rate = df['USDCARD_in'].min()
    USDCARD_out_min_rate = df['USDCARD_out'].min()
    EURCARD_in_min_rate = df['EURCARD_in'].min()
    EURCARD_out_min_rate = df['EURCARD_out'].min()
    RUBCARD_in_min_rate = df['RUBCARD_in'].min()
    RUBCARD_out_min_rate = df['RUBCARD_out'].min()

    print('Average value of the purchase rate in US dollars: ', USDCARD_in_average_rate)
    print('Max value of the purchase rate in US dollars: ', USDCARD_in_max_rate)
    print('Min value of the purchase rate in US dollars: ', USDCARD_in_min_rate)

    print('Average value of the sale rate in US dollars: ', USDCARD_out_average_rate)
    print('Max value of the sale rate in US dollars: ', USDCARD_out_max_rate)
    print('Min value of the sale rate in US dollars: ', USDCARD_out_min_rate)

    # Graph
    df['Date'] = pd.to_datetime(df['kurs_date_time'])
    df.set_index('Date', inplace=True)
    df['USDCARD_in'].plot(title='The purchase rate in US dollars', xlabel='Date', ylabel='Exchange Rate')
    plt.show()

    df['USDCARD_out'].plot(title='The sale rate in US dollars', xlabel='Date', ylabel='Exchange Rate')
    plt.show()

else:
    print(f"Error {response.status_code}: {response.text}")
