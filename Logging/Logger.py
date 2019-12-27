import logging


class Customlogger():
    def __init__(self, module_name):
        logging.basicConfig(level=logging.DEBUG)

        self.logger = logging.getLogger(module_name)

    def log_message(self, message):
        self.logger.debug(message)
