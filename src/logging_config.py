import logging


logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logging_file.log")
file_handler.setLevel(logging.DEBUG)



