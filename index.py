import asyncio

from loguru import logger

from core.dispatcher import dispatcher
from modules.price_monitor import PriceMonitor


async def main():
    monitor = PriceMonitor()
    asyncio.create_task(monitor.start())
    logger.info("Price monitor started")

    await dispatcher.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
