import requests

def get_capital(country):
    try:
        url = f'https://restcountries.com/v3.1/name/{country}'
        r = requests.get(url)
        data = r.json()
        capital = data[0]["capital"][0]
        return capital
    except KeyError:
        return "ERROR"

def get_country(capital):
    try:
        url = f'https://restcountries.com/v3.1/capital/{capital}'
        r = requests.get(url)
        data = r.json()
        country = data[0]["name"]["common"]
        return country
    except KeyError:
        return "ERROR"
        

