import logging
from logging import handlers


def setupServerLog():
    logging.basicConfig(
        format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
        level=logging.INFO,
        handlers=[handlers.TimedRotatingFileHandler(filename='log/server1.log', interval=1, when='d', backupCount=5)]
    )


if __name__ == '__main__':
    mysetup = ''
    setupServerLog()


