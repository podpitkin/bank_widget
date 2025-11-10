import time
from functools import wraps


def log(filename=None):
    """Декоратор log, который автоматически регистрирует детали выполнения функций"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                start_func = time.time()
                result = func(*args, **kwargs)
                end_func = time.time()
                msg = (
                    f"{func.__name__} ok. Result: {result}\n"
                    f"Function start time: {start_func}\n"
                    f"End time of the function: {end_func}\n"
                    f"Function execution time: {end_func - start_func:.9f}\n"
                )
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(msg)
                else:
                    print(msg)

            except Exception as e:
                error_msg = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as log_file:
                        log_file.write(error_msg)
                else:
                    print(error_msg)
                raise
            return result

        return inner

    return wrapper


@log(filename="my_log.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
