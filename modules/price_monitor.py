import asyncio
from collections import deque
from typing import Dict

from loguru import logger

from exchanges import binance, bybit, bitget, okx, mexc


class PriceMonitor:
    def __init__(self, max_history: int = 900):
        self.price_history: Dict[str, deque] = {}
        self.max_history = max_history
        self.exchanges = [
            binance.BinanceWS(),
            bybit.BybitWS(),
            bitget.BitgetWS(),
            okx.OKXWS(),
            mexc.MEXCWS(),
        ]

    async def start(self):
        await asyncio.gather(*(ex.connect(self.on_price) for ex in self.exchanges))

    async def on_price(self, symbol: str, price: float):
        if symbol not in self.price_history:
            self.price_history[symbol] = deque(maxlen=self.max_history)
        self.price_history[symbol].append(price)
        logger.debug(f"{symbol} price: {price}")
