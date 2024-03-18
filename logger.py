import logging
from colorlog import ColoredFormatter


class BaseLogger(logging.getLogger(__name__).__class__):
    """
    Override this class for more customizations.
    """
    LOGGER_FORMAT = ("  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s"
                     " {%(filename)s:%(lineno)s - %(funcName)s} %(message)s%(reset)s")

    def __init__(self, name, level=logging.DEBUG):
        super().__init__(name, level)

        stream = logging.StreamHandler()
        stream.setFormatter(ColoredFormatter(self.LOGGER_FORMAT))

        self.addHandler(stream)


logger = BaseLogger(__name__)

if __name__ == '__main__':
    logger.debug("A quirky message only developers care about")
    logger.info("Curious users might want to know this")
    logger.warning("Something is wrong and any user should be informed")
    logger.error("Serious stuff, this is red for a reason")
    logger.critical("OH NO everything is on fire")
