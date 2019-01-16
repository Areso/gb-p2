import logging
from logging import handlers


def setupServerLog():
    logging.basicConfig(
        filename="log/server.log",
        format="%(asctime)s %(levelname)-10s %(module)s %(message)s",
        level=logging.INFO
    )
    global mysetup
    mysetup = handlers.TimedRotatingFileHandler(
        filename="log/server.log",
        backupCount=5,
        interval=1,
        when='m'
    )



if __name__ == '__main__':
    mysetup = ''
    setupServerLog()


