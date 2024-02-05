#!/usr/bin/env python3
"""
unittest for access_nested_map
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    test access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: int) -> None:
        """
        test access_nested_map method
        """
        respose = access_nested_map(nested_map, path)
        self.assertEqual(respose, expected)

    @parameterized.expand([
        ({}, ('a',), ),
        ({'a: 1'}, ('a', 'b'), )
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        test raise error
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
