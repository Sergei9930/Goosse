from . import BaseWS

class MEXCWS(BaseWS):
    URL = "wss://wbs.mexc.com/raw/ws"

    async def _handle_message(self, message: str, callback):
        # TODO: parse real MEXC data
        pass
