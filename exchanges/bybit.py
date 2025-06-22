from . import BaseWS

class BybitWS(BaseWS):
    URL = "wss://stream.bybit.com/v5/public/quote"

    async def _handle_message(self, message: str, callback):
        # TODO: parse real Bybit data
        pass
