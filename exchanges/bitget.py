from . import BaseWS

class BitgetWS(BaseWS):
    URL = "wss://ws.bitget.com/spot/v1/stream"

    async def _handle_message(self, message: str, callback):
        # TODO: parse real Bitget data
        pass
