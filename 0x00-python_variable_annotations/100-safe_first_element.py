#!/usr/bin/env python3
"""task 100"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """a type-annotated function"""
    if lst:
        return lst[0]
    else:
        return None
