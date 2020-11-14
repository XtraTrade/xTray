import time
import os

import rumps
import requests


def get_price(_symbol):
    resp = requests.get(f'https://api.xtra.trade/quote/by/contract/{_symbol}').json()
    price = resp['data']['price']
    rise = resp['data']['rise']
    return price, rise

@rumps.timer(5)
def a(sender):
    symbol = 'btc.usdt'
    token, _ = symbol.split('.')
    price, rise = get_price(symbol)
    app.title = ' {} {:.2}% '.format(price, rise)
    icon_name = f'{token}.png'
    if os.path.exists(icon_name):
        app.icon = icon_name
    else:
        app.icon = 'default.png'


app = rumps.App('Xtra.Trade', quit_button=rumps.MenuItem('Quit', key='q'))
app.run()

