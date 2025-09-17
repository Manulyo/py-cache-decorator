from typing import Callable


def cache(func: Callable) -> Callable:
    cash_store = {}

    def wrapper(*args, **kwargs) -> None:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cash_store:
            print("Getting from cache")
            return cash_store[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cash_store[key] = result
        return result
    return wrapper
