import json
from . import BaseWS


class BinanceWS(BaseWS):
    URL = "wss://stream.binance.com:9443/stream?streams=!miniTicker@arr"

    async def _handle_message(self, message: str, callback):
        data = json.loads(message)
        if 'data' in data:
            for ticker in data['data']:
                symbol = ticker.get('s')
                price = float(ticker.get('c'))
                await callback(symbol, price)
