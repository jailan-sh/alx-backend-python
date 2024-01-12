#!/usr/bin/env python3
"""task 102"""
from typing import Tuple, List, Any



def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """a type-annotated function"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
