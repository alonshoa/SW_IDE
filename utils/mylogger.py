import logging
from logging import Logger
import os
import gzip
import shutil

MAX_LOG_SIZE = 100000000

class MyLogger(Logger):
	def __init__(self):
		super().__init__(self)
		logging.basicConfig(filename="log.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
		self.logger = logging.getLogger()
		self.archive_log()
		self.logger.info("Logger created")

	def log_info(self, message):
		self.logger.info(message)

	def log_warning(self, message):
		self.logger.warning(message)

	def log_error(self, message):
		self.logger.error(message)

	def log_critical(self, message):
		self.logger.critical(message)

	def archive_log(self):
		if os.path.exists("log.txt") and os.path.getsize("log.txt") > MAX_LOG_SIZE:
			with open("log.txt", "rb") as f_in:
				with gzip.open("log.txt.gz", "wb") as f_out:
					shutil.copyfileobj(f_in, f_out)
			os.remove("log.txt")
