#!/usr/bin/env python3
"""task 102"""
from typing import Union, List, Any



def zoom_array(lst: List[int], factor: Any = 2) -> List[Any]:
    """a type-annotated function"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
