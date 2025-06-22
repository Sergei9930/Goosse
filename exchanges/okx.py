from . import BaseWS

class OKXWS(BaseWS):
    URL = "wss://ws.okx.com:8443/ws/v5/public"

    async def _handle_message(self, message: str, callback):
        # TODO: parse real OKX data
        pass
