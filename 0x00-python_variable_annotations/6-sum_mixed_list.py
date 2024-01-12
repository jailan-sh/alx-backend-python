#!/usr/bin/env python3
"""task 6"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """a type-annotated function"""
    return float(sum(mxd_lst))
