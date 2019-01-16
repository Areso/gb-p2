import logging
from logging import handlers

def setupClientLog():
    logging.basicConfig(
        filename="log/client.log",
        format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
        level=logging.INFO
    )


if __name__ == '__main__':
    setupClientLog()

