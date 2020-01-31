"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#timestrftime
"""
import logging

logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.DEBUG) # If you want 24 hour format instead I put H and remove %p
logging.warning("warning message")
logging.info("info message")
logging.error("error message")
