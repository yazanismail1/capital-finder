from http.server import BaseHTTPRequestHandler
from urllib import parse 
from logic.logic import get_country, get_capital


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        '''A function that send request to vercel'''
        s=self.path
        url_components=parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary=dict(query_string_list)

        if 'country' in dictionary:
            country_name = dictionary['country']
            capital_city =  get_capital(country_name)
            if capital_city == "ERROR":
                message =  f"{country_name} is not a country, kindly enter a valid country name..."
            else:
                message = f"The capital of {country_name} is {capital_city}" 
        elif 'capital' in dictionary:
            capital_city = dictionary['capital']
            country_name =  get_country(capital_city) 
            if country_name == "ERROR":
                message =  f"{capital_city} is not a capital city, kindly enter a valid capital city name..."
            else:
                message = f"{capital_city} is the capital city of {country_name}" 
        else: 
            message = "Kindly enter a country or capital city name..."

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
     
        self.wfile.write(message.encode())
        return