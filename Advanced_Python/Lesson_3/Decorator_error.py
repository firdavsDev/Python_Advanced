
from functools import wraps

import logging

def out_logger(level:str):

    def my_logger(original_function):
        logging.basicConfig(filename=f"{original_function.__name__}.log", level=level)

        @wraps(original_function)
        def wrapper(*args, **kwargs):
            logging.debug(
                f"Ran with args: {args}, and kwargs: {kwargs}")
            return original_function(*args, **kwargs)
        return wrapper
    return my_logger


def my_timer(original_function):
    import time
    
    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} ran in: {t2} sec")
        return result

    return wrapper

import time

@out_logger(logging.DEBUG)
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f"display_info ran with arguments ({name}, {age})")

display_info("Davron", 25)
