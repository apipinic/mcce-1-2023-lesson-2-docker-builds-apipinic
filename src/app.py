# app.py
from flask import Flask, render_template, jsonify
import requests
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

@app.route('/static/js/update_data.js')
def serve_js(filename):
    return send_from_directory('static/js', filename, mimetype='application/javascript')


# Dummy data for demonstration purposes
dummy_crypto_symbols = ["bitcoin", "ethereum", "xrp", "litecoin", "cardano"]
dummy_etf_symbols = ["SPY", "QQQ", "DIA", "GLD", "VGT"]

def fetch_crypto_data():
    crypto_data = {}  # Clear existing data
    for symbol in dummy_crypto_symbols:
        response = requests.get(f'https://api.coincap.io/v2/assets/{symbol}')
        data = response.json()

        # Check if the symbol is present in the API response
        if 'data' in data and 'priceUsd' in data['data']:
            crypto_data[symbol.upper()] = data['data']['priceUsd']  # Use uppercase symbols for consistency
        else:
            print(f"Error fetching data for {symbol.upper()}. Check if the symbol is correct. Error Message: {data.get('error', 'Unknown error')}")

    print("Crypto Data:", crypto_data)
    return crypto_data

def fetch_etf_data():
    etf_data = {}  # Clear existing data
    for symbol in dummy_etf_symbols:
        # Fetch ETF data from your preferred source or API
        # Here, we're using dummy data for demonstration purposes
        etf_data[symbol] = round(100 + (symbol.__hash__() % 10), 2)

    print("ETF Data:", etf_data)
    return etf_data

# Schedule background jobs to fetch data
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(fetch_crypto_data, 'interval', seconds=5)
scheduler.add_job(fetch_etf_data, 'interval', seconds=5)
scheduler.start()

@app.route('/')
def home():
    crypto_data = fetch_crypto_data()
    etf_data = fetch_etf_data()
    return render_template('index.html', crypto_data=crypto_data, etf_data=etf_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
