import logging
from functools import wraps

def get_logger():
    logger = logging.getLogger("calculator")
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('calculator.log')
        formatter = logging.Formatter('---- %(message)s ----')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger

logger = get_logger()

def log_function_call(function_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.debug(f"---- Function {function_name} Enter ----")
            result = func(*args, **kwargs)
            logger.debug(f"---- Function {function_name} Exit ----")
            return result
        return wrapper
    return decorator