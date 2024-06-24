import os
import json
from bottle import route, run, request

entry_price = 0

@route('/api/v1/tradingview/alert', method='POST')
def process_alert():
    global entry_price

    # Read the body from request
    body = request.body.read()
    req_val = request.body.getvalue()
    alert = json.loads(req_val)

    if alert['type'] == 'dbs_buy':
        print("Buying %s for %s" % (alert['ticker'], alert['close']))
        entry_price = int(alert['close'])
    elif alert['type'] == 'dbs_sell':
        print("Selling %s for %s" % (alert['ticker'], alert['close']))
        pnl = int(alert['close']) - entry_price
        print("PNL = %d" % pnl)

if __name__ == '__main__':
    run(host='0.0.0.0', port=8031, debug=True)

