from contextlib import contextmanager
from datetime import timedelta
from time import perf_counter


@contextmanager
def timer(message: str = "Time elapsed:", digits: int = -1):
    """
    Context manager based timer.
    """

    start = perf_counter()
    yield
    stop = perf_counter()

    delta = str(timedelta(seconds=stop - start))

    if digits >= 0:
        # format microseconds
        delta = delta.split(".")
        delta[1] = delta[1][:digits]
        delta = ".".join(delta)

    print(f"{message} {delta}")
