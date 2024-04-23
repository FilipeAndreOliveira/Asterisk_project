import requests
from bs4 import BeautifulSoup as bs

def get_html(url):
    try:
        response = requests.get(url)
        return response
    except:
        print("Error getting the HTML data...\n")

def parse_price(raw_data):
    bsObj = bs(raw_data.content, "html.parser")
    new_data = bsObj.find_all("span", class_= "color-gray-xdark data-current-price")
    if len(new_data) > 0:
        return new_data[0].text.strip()
    else:
        return "Price data not found."


response = get_html("https://qontigo.com/index/sxxp/")
if response is not None:
    price = parse_price(response)
    print("The current price is:", price, "euro")

