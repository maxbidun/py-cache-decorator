from typing import Callable


def cache(func: Callable) -> Callable:
    cache_memory = {}

    def inner(*args, **kwargs) -> Callable:
        key = args + tuple(kwargs.values())
        if key in cache_memory:
            print("Getting from cache")
        else:
            result = func(*key)
            cache_memory[key] = result
            print("Calculating new result")
        return cache_memory[key]
    return inner
