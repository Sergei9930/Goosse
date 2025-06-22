import asyncio
import json
import websockets
from typing import Callable, Awaitable


class BaseWS:
    URL = ""

    async def connect(self, callback: Callable[[str, float], Awaitable[None]]):
        async with websockets.connect(self.URL) as ws:
            async for message in ws:
                await self._handle_message(message, callback)

    async def _handle_message(self, message: str, callback: Callable[[str, float], Awaitable[None]]):
        raise NotImplementedError
