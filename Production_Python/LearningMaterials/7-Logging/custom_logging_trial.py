import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

custom_file_handler = logging.FileHandler('custom_logging.log', mode = 'w')
custom_file_handler.setLevel(logging.WARNING)

custom_file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d')
custom_file_handler.setFormatter(custom_file_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_formatter = logging.Formatter('%(module)s - %(lineno)d - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

logger.addHandler(custom_file_handler)
logger.addHandler(console_handler)

logger.debug("This is a debug message")
logger.info("This is a info message") 
logger.warning("This is a warning message") 
logger.error("This is a error message") 
logger.critical("This is a critical message") 