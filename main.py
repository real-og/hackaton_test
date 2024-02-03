from fastapi import FastAPI, Response, status, Depends
from enum import Enum
from datetime import datetime, date
from typing import Annotated
app = FastAPI()
import requests

@app.get("/api/banks")
async def all_banks():
    spisok = ["Нацбанк Республики Беларусь", "Альфа-Банк", "Беларусбанк"]
    return spisok




class BanksName(str, Enum):
    nbrb = "nbrb"
    alfabank = "alfabank"
    belarusbank = "belarusbank"


@app.get("/api/banks/{bankName}/currencies", response_model=list)
async def all_bank_currencies(bankName:BanksName):
    currencies_list = {'nbrb': 'https://api.nbrb.by/exrates/currencies',
                       'alfabank': 'https://developerhub.alfabank.by:8273/partner/1.0.1/public/rates',
                       'belarusbank': 'https://belarusbank.by/api/kurs_cards'
                       }

    url = currencies_list[bankName]
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        spisok = []
        if bankName == "nbrb":
            for currencie in data:
                currencie_name = currencie["Cur_Name"]
                spisok.append(currencie_name)
        elif bankName == "alfabank":
            data = data["rates"]
            for currecie in data:
                currecie_name = currecie["sellIso"]
                spisok.append(currecie_name)
                spisok = list(set(spisok))
        elif bankName == "belarusbank":
            data = data[0]
            # for currencie in data:
            #     currencie_name = currencie["Cur_Name"]
            #     spisok.append(currencie_name)
            for currecie in data:
                if currecie == "kurs_date_time":
                    continue
                currecie_name = currecie[0:3]
                spisok.append(currecie_name)
                spisok = list(set(spisok))


    else:
        print(f"Error {response.status_code}: {response.text}")
    return spisok


@app.get("/rate")
async def currencie_rate_ondate(bank: BanksName, currencyCode: str = "840", yourdate: datetime = "2024-02-02"):

    if bank == 'alfabank':
        return Response(status_code=status.HTTP_404_NOT_FOUND)


    if bank == 'belarusbank':

        currencies_list = {
            "156": "CNY",
            "840": "USD",
            "643": "RUB",
            "978": "EUR",
        }
        currencie = currencies_list[currencyCode]
        url = "https://belarusbank.by/api/kurs_cards"
        response = requests.get(url)
        spisok = {}

        if response.status_code == 200:
            data = response.json()
            for date_time in data:
                date_time_object = datetime.strptime(date_time['kurs_date_time'], '%Y-%m-%d %H:%M:%S')
                date_only = date_time_object.strftime('%Y-%m-%d')
                yourdate = str(yourdate)[0:10]
                if date_only == yourdate:
                    for curr in date_time:
                        if currencie in curr and curr.count('_') == 1:
                            spisok[curr] = date_time[curr]

                    spisok["date"] = yourdate

                    return spisok

        else:
            return Response(status_code=status.HTTP_404_NOT_FOUND)


    # if bank == "nbrb":





@app.get("/Rate/rates")
async def read_item(bank: BanksName, currencyCode: str = "933", fromdate: datetime = "2008-09-15",
                    todate: datetime = "2008-09-16"):
    return [
        {
            "date": "somedate",
            "sellRate": "somesellRate",
            "buyRate": "somebuyRatee",
        }
    ]


@app.get("/Rate/statistics")
async def read_item(bank: BanksName, currencyCode: str = "933", fromdate: datetime = "2008-09-15",
                    todate: datetime = "2008-09-16"):
    return {
        "date": "somedate",
        "sellRate": "somesellRate",
        "buyRate": "somebuyRate",
    }