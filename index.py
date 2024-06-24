import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

entry_price = 0

@app.route('/api/v1/tradingview/alert', methods=['POST'])
def process_alert():
    global entry_price

    # Read the body from request
    body = request.data
    alert = json.loads(body)
    print(alert)
    if alert['type'] == 'dbs_buy':
        print("Buying %s for %s" % (alert['ticker'], alert['close']))
        entry_price = int(alert['close'])
    elif alert['type'] == 'dbs_sell':
        print("Selling %s for %s" % (alert['ticker'], alert['close']))
        pnl = int(alert['close']) - entry_price
        print("PNL = %d" % pnl)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8031, debug=True)
