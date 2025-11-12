import time
import functools


def profile_function(func):
    """
    Decorator that measures the execution time of a function
    and prints the duration.

    Example:
        @profile_function
        def slow_func():
            for _ in range(1000000):
                pass
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        exec_time = end - start
        print(f"[autopyperf] {func.__name__} executed in {exec_time:.6f}s")
        return result
    return wrapper
