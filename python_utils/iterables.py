from itertools import islice
from typing import Iterable, Iterator, TypeVar


T = TypeVar("T")


def batched(iterable: Iterable[T], batch_size: int) -> Iterator[list[T]]:
    """
    Generator which yields batched iterable.
    """

    iterator = iter(iterable)
    while batch := list(islice(iterator, batch_size)):
        yield batch
