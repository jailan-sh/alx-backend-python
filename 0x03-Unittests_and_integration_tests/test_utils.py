#!/usr/bin/env python3
"""
unittest for access_nested_map
"""
import requests
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json
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


class TestGetJson(unittest.TestCase):
    """ mock HTTp calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_pyload, mock_requests_get):
        """ test get_json"""
        mock_requests_get.return_value.json.return_value = test_pyload
        result = get_json(test_url)
        self.assertEqual(result, test_pyload)
        mock_requests_get.assert_called_once_with(test_url)
