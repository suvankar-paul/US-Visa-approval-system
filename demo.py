from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

# logging.info("welcome to our custom logger module")

try:
    a= 1 / 0
except Exception as e:
    raise USvisaException(e, sys)