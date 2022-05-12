import logging
from logging import Logger

class MyLogger(Logger):
	def __init__(self):
		super().__init__(self)
		logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
		self.logger = logging.getLogger()
		self.logger.info("Logger created")

	def log_info(self, message):
		self.logger.info(message)

	def log_warning(self, message):
		self.logger.warning(message)

	def log_error(self, message):
		self.logger.error(message)

	def log_critical(self, message):
		self.logger.critical(message)
