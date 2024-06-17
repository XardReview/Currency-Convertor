import requests
from bs4 import BeautifulSoup
import warnings

warnings.filterwarnings("ignore")

def get_usd_exchange_rate():
    try:
        url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        valute_dict = {}
        valute_tags = soup.find_all('valute')
        for tag in valute_tags:
            valute_dict[tag.find('charcode').get_text()] = float(tag.find('value').get_text().replace(',', '.'))

        return valute_dict.get('USD')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def usd_to_rub(amount_usd):
    rub_rate = get_usd_exchange_rate()
    if rub_rate is None:
        return None

    amount_rub = amount_usd * rub_rate
    return amount_rub

def get_eur_exchange_rate():
    try:
        url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        valute_dict = {}
        valute_tags = soup.find_all('valute')
        for tag in valute_tags:
            valute_dict[tag.find('charcode').get_text()] = float(tag.find('value').get_text().replace(',', '.'))

        return valute_dict.get('EUR')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def eur_to_rub(amount_eur):
    rub_rate = get_eur_exchange_rate()
    if rub_rate is None:
        return None

    amount_rub = amount_eur * rub_rate
    return amount_rub

def get_uzs_exchange_rate():
    try:
        url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        valute_dict = {}
        valute_tags = soup.find_all('valute')
        for tag in valute_tags:
            valute_dict[tag.find('charcode').get_text()] = float(tag.find('value').get_text().replace(',', '.'))

        return valute_dict.get('UZS')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def uzs_to_rub(amount_uzs):
    rub_rate = get_uzs_exchange_rate()
    if rub_rate is None:
        return None

    amount_rub = amount_uzs * rub_rate
    return amount_rub

def get_cny_exchange_rate():
    try:
        url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        valute_dict = {}
        valute_tags = soup.find_all('valute')
        for tag in valute_tags:
            valute_dict[tag.find('charcode').get_text()] = float(tag.find('value').get_text().replace(',', '.'))

        return valute_dict.get('CNY')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def cny_to_rub(amount_cny):
    rub_rate = get_cny_exchange_rate()
    if rub_rate is None:
        return None

    amount_rub = amount_cny * rub_rate
    return amount_rub

def get_inr_exchange_rate():
    try:
        url = 'https://www.cbr.ru/scripts/XML_daily.asp'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        valute_dict = {}
        valute_tags = soup.find_all('valute')
        for tag in valute_tags:
            valute_dict[tag.find('charcode').get_text()] = float(tag.find('value').get_text().replace(',', '.'))

        return valute_dict.get('INR')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def inr_to_rub(amount_inr):
    rub_rate = get_inr_exchange_rate()
    if rub_rate is None:
        return None

    amount_rub = amount_inr * rub_rate
    return amount_rub