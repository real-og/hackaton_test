from loader import BASE_URL, BANK_CODE
import requests

BASE_URL='http://46.19.65.223:7998/'
headers = {'accept': "application/json"}

def get_available_banks():
    url = BASE_URL + 'api/banks'
    try:
        resp = requests.get(url)
    except:
        return None
    if resp.status_code == 200: 
        return resp.json()
    return None


def get_currencies_by_bank(bank):
    url = BASE_URL + 'api/banks/' + bank + '/currencies'
    try:
        resp = requests.get(url)
    except:
        return None
    if resp.status_code == 200: 
        return resp.json()
    return None

def get_exchange_rate(bank, currency_code, date):
    url = BASE_URL + 'rate/'
    print(BANK_CODE.get(bank))
    print(currency_code)
    print(date)
    params = {'bank': BANK_CODE.get(bank),
              'currencyCode': currency_code,
              'yourDate': date}
    try:
        resp = requests.get(url, params=params)
    except:
        return None
    if resp.status_code == 200: 

        return resp.json().get('USDCARD_in')

    return None