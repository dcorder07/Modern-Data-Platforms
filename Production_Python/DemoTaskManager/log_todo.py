
import logging

# Create a custom logger
logger = logging.getLogger('todo_logger')
logger.setLevel(logging.INFO)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('todo_logger.log', mode='w')

# Set logging level for handlers
stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

# Create formatters
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
