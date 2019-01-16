import logging
from logging import handlers

def setupServerLog():
    logging.basicConfig(
        filename="log/server.log",
        format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
        level=logging.INFO
    )


if __name__ == '__main__':
    setupServerLog()

