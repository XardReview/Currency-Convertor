from flask import Flask
from conversion import get_exchange_rate

app = Flask(__name__)

@app.route('/rates')
def get_rates():
    usd = get_exchange_rate('USD')
    eur = get_exchange_rate('EUR')
    uzs = get_exchange_rate('UZS')
    cny = get_exchange_rate('CNY')
    inr = get_exchange_rate('INR')
    kzt = get_exchange_rate('KZT')
    return f"USD: {usd};EUR: {eur};UZS: {uzs};CNY: {cny};INR: {inr};KZT: {kzt}"

if __name__ == '__main__':
    app.run(port=5000)
