#!/usr/bin/env python3
"""
Unit test module for utils.access_nested_map function.

This module contains a test case for the access_nested_map function
that retrieves values from a nested dictionary using a specified path.
"""

import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from utils import access_nested_map  # Import the function we are testing


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap defines unit tests for the access_nested_map function.

    Methods:
        - test_access_nested_map: Tests access_nested_map with various inputs
          to ensure correct values are returned.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Case 1: Simple dictionary with one key-value pair
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Case 2: Nested dictionary, access top-level key
        ({"a": {"b": 2}}, ("a", "b"), 2)  # Case 3: Nested dictionary, full path to value
    ])
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str, ...], expected: Any
    ) -> None:
        """
        Test that access_nested_map returns the expected value for given nested_map and path.

        Args:
            nested_map (Dict[str, Any]): The nested dictionary to search.
            path (Tuple[str, ...]): The path tuple indicating the keys to follow.
            expected (Any): The expected value from the access_nested_map function.

        Asserts:
            - The return value of access_nested_map is equal to the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    # Execute the tests when the script is run directly
    unittest.main()
