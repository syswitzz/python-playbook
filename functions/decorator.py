"""
A decorator is a callable that:
- Takes another function (or method, or class) as input.
- Returns a new callable that usually wraps the original.
- Lets you extend/modify behavior without changing the original code.

Real-World Uses of Decorators:
    Logging: Track function calls (e.g., @logger).
    Authentication: Restrict access in web apps (e.g., Flask/Django).
    Rate Limiting: Control API usage per user.
    Caching: Store results using functools.lru_cache.
    Retry Logic: Automatically retry failed network calls.
"""


# timer is an example of custom decorator
# used to calculate and prints time taken the run the function
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f'The function {func.__name__} took {end_time-start_time:.4f}s.')
    return wrapper

@timer
def example(n):
    print(f'The sum of {n} is {sum(range(n))}.')


# @functools.cache - writes a custom cache for us and automatically resize the cache
# use when youre calling the same function repeatedly with same arguments
import functools

@functools.cache
def fibonacci(n):
    if(n<2):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)