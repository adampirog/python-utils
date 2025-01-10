from itertools import islice
from typing import Iterable, Iterator, TypeVar


T = TypeVar("T")


def batched(iterable: Iterable[T], batch_size: int) -> Iterator[list[T]]:
    """
    Generator which yields batches from the iterable.

    Parameters:
    - iterable (Iterable[T]): The iterable to batch.
    - batch_size (int): The size of each batch. If negative, yields the
        batch_size <= 0 means max batch size, which yields the entire
        iterable as a single batch

    Yields:
    - Iterator[list[T]]: An iterator over batches of the iterable.
    """
    if batch_size <= 0:
        yield list(iterable)
    else:
        iterator = iter(iterable)
        while batch := list(islice(iterator, batch_size)):
            yield batch
