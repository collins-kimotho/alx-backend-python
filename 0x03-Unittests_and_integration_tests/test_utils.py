#!/usr/bin/env python3
"""
Unit test module for utils.access_nested_map function.

This module contains a test case for the access_nested_map function
that retrieves values from a nested dictionary using a specified path.
"""

import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from utils import access_nested_map, get_json, memoize # Import the function we are testing


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
    """Test cases for the get_json function."""

    @patch("utils.requests.get")  # Mock requests.get to prevent actual HTTP calls
    def test_get_json(self, mock_get: Mock) -> None:
        """Test that get_json returns the expected result with mocked requests."""

        # Define test cases with URLs and the expected JSON payloads
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        # Iterate over each test case
        for test_url, test_payload in test_cases:
            # Create a Mock object for the response and set its json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload  # Mock the JSON response
            mock_get.return_value = mock_response  # Set mock_get to return this response

            # Call the get_json function with the test URL
            result = get_json(test_url)

            # Check that the mocked get method was called once with the correct URL
            mock_get.assert_called_once_with(test_url)
            # Verify that the result is as expected
            self.assertEqual(result, test_payload)

            # Reset the mock for the next iteration
            mock_get.reset_mock()

class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches the result of a method."""

        # Define a class to test memoization
        class TestClass:
            """A simple class with a memoized property."""

            def a_method(self):
                """A method that returns a fixed value."""
                return 42

            @memoize
            def a_property(self):
                """A memoized property that calls a_method."""
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Use unittest.mock.patch to mock a_method
        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Check that a_method was called only once
            mock_method.assert_called_once()

            # Verify that both results are the same and as expected
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == "__main__":
    # Execute the tests when the script is run directly
    unittest.main()
