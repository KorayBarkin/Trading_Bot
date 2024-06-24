const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 8080;

let entryPrice = 0;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

app.post('/api/v1/tradingview/alert', (req, res) => {
    const alert = req.body;
    console.log(req.body);
    if (alert.type === 'dbs_buy') {
        console.log(`Buying ${alert.ticker} for ${alert.close}`);
        entryPrice = parseInt(alert.close);
    } else if (alert.type === 'dbs_sell') {
        console.log(`Selling ${alert.ticker} for ${alert.close}`);
        const pnl = parseInt(alert.close) - entryPrice;
        console.log(`PNL = ${pnl}`);
    }

    res.sendStatus(200);
});

app.listen(port, () => {
    console.log(`Server running on http://0.0.0.0:${port}`);
});
