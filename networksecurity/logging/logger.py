import logging
import os
from datetime import datetime

# structure of LOG File
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# path where we'll be storing our logs
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

# complete path
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# filename=LOG_FILE_PATH: Specifies the file where the log messages will be written.
# format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s": Defines the format of the log messages. It includes:
# %(asctime)s: The time when the log message was created.
# %(lineno)d: The line number in the source code where the log message was generated.
# %(name)s: The name of the logger.
# %(levelname)s: The severity level of the log message.
# %(message)s: The actual log message.
# level=logging.INFO: Sets the logging level to INFO, meaning that all messages at this level and above will be logged.