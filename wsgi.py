from mondohook import application
import logger
from logging.handlers import RotatingFileHandler

if __name__ == "__main__":
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

    handler = RotatingFileHandler('/home/mainuser/mondohook/error.log', maxBytes=1000000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    application.logger.addHandler(handler)

    application.run()

