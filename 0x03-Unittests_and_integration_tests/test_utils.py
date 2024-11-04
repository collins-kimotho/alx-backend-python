#!/usr/bin/env python3
"""
Unit test module for utils.access_nested_map function.

This module contains a test case for the access_nested_map function
that retrieves values from a nested dictionary using a specified path.
"""

import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from utils import access_nested_map, get_json # Import the function we are testing


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap defines unit tests for the access_nested_map function.

    Methods:
        - test_access_nested_map: Tests access_nested_map with various inputs
          to ensure correct values are returned.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  # Case 1: Simple dictionary with one key-value pair
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  # Case 2: Nested dictionary, access top-level keyclass TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function"""

    @parameterized.expand([
        ({}, ("a",)),                     # Test case 1: Empty dictionary and non-existent key
        ({"a": 1}, ("a", "b")),           # Test case 2: Dictionary with a key that doesn't have a nested key
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        # Check that the exception message matches the expected key
        self.assertEqual(str(context.exception), repr(path[-1]))

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

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function"""

    @parameterized.expand([
        ({}, ("a",)),                     # Test case 1: Empty dictionary and non-existent key
        ({"a": 1}, ("a", "b")),           # Test case 2: Dictionary with a key that doesn't have a nested key
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        # Check that the exception message matches the expected key
        self.assertEqual(str(context.exception), repr(path[-1]))

class TestGetJson(unittest.TestCase):
    """
    Test the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """
        Test the get_json method to ensure it returns the expected output.
        Args:
            url: url to send http request to
            payload: expected json response
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    # Execute the tests when the script is run directly
    unittest.main()
