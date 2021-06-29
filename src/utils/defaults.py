# pylint: disable=invalid-name
from typing import Optional, Type, TypeVar, Union

T = TypeVar("T")
U = TypeVar("U")


def default(a: Optional[T], b: Optional[U], error: Type[Exception]) -> Union[T, U]:
    if a is not None:
        return a

    if b is not None:
        return b

    raise error
