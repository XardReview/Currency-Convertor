import requests

def get_exchange_rate(currency_code):
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req="
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        if currency_code in data:
            start = data.find(currency_code)
            value_start = data.find("<Value>", start) + 7
            value_end = data.find("</Value>", value_start)
            value = data[value_start:value_end]
            return float(value.replace(',', '.'))
    return None

def usd_to_rub(amount):
    rate = get_exchange_rate("USD")
    if rate:
        return amount * rate
    return None

def eur_to_rub(amount):
    rate = get_exchange_rate("EUR")
    if rate:
        return amount * rate
    return None

def uzs_to_rub(amount):
    rate = get_exchange_rate("UZS")
    if rate:
        return amount * (rate / 10000)
    return None

def cny_to_rub(amount):
    rate = get_exchange_rate("CNY")
    if rate:
        return amount * rate
    return None
def inr_to_rub(amount):
    rate = get_exchange_rate("INR")
    if rate:
        return amount * (rate / 10)
    return None
def kzt_to_rub(amount):
    rate = get_exchange_rate("KZT")
    if rate:
        return amount * (rate / 100)
    return None
def rub_to_usd(amount):
    rate = get_exchange_rate("USD")
    if rate:
        return amount / rate
    return None
def rub_to_eur(amount):
    rate = get_exchange_rate("EUR")
    if rate:
        return amount / rate
    return None
def rub_to_uzs(amount):
    rate = get_exchange_rate("UZS")
    if rate:
        return amount / (rate / 10000)
    return None
def rub_to_cny(amount):
    rate = get_exchange_rate("CNY")
    if rate:
        return amount / rate
    return None
def rub_to_inr(amount):
    rate = get_exchange_rate("INR")
    if rate:
        return amount / (rate / 10)
    return None
def rub_to_kzt(amount):
    rate = get_exchange_rate("KZT")
    if rate:
        return amount / (rate / 100)
    return None