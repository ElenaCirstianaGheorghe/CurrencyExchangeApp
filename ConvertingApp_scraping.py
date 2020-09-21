from bs4 import BeautifulSoup
import requests
import csv

def Exchange_Rate():
    ''' It creates a list containing the names, the symbols and the values of the
    currencies found on 'https://www.bnr.ro/Cursul-de-schimb-524.aspx' and
    builds two dictionaries, one including the currency exchange rate for the
    current date for every currency and one including the symbols for every
    currency.'''

    items = []
    symbols_dict = {}
    exchange_dict = {}

    for item in soup.find_all('td'):
        items.append(item.text)


    i = 0
    while i <= len(items) - 8:
        exchange_dict[items[i]] = float(items[i+6].replace(',','.'))
        symbols_dict[items[i]] = items[i+1]
        i += 8

    exchange_dict[" Leul românesc"] = 1
    symbols_dict[" Leul românesc"] = "RON"

    return exchange_dict, symbols_dict

#========================================

source = requests.get('https://www.bnr.ro/Cursul-de-schimb-524.aspx').text

soup = BeautifulSoup(source, 'lxml')

exchange_dict, symbols_dict = Exchange_Rate()
