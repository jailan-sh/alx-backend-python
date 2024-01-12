#!/usr/bin/env python3
"""task 100"""
from typing import Union, Sequence, Any, Mapping, TypeVar
T = TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """a type-annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
