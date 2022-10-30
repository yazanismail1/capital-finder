import requests

def get_capital(country:str) -> str:
    '''A function that given a country name, it sends a request to rest countries API and gets it corresponding capital city.
    
    Input: country name (str)
    return: capital city (str)
    '''
    try:
        url = f'https://restcountries.com/v3.1/name/{country}'
        r = requests.get(url)
        data = r.json()
        capital = data[0]["capital"][0]
        return capital
    except KeyError:
        return "ERROR"

def get_country(capital:str) -> str:
    '''A function that given a capital city, it sends a request to rest countries API and gets it corresponding country.
    
    Input: capital city (str)
    return: country name (str)
    '''
    try:
        url = f'https://restcountries.com/v3.1/capital/{capital}'
        r = requests.get(url)
        data = r.json()
        country = data[0]["name"]["common"]
        return country
    except KeyError:
        return "ERROR"
