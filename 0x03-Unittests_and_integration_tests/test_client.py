#!/usr/bin/env python3
"""Unit tests for GithubOrgClient in the client module."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),  # Test case 1: Organization name "google"
        ("abc",),     # Test case 2: Organization name "abc"
    ])
    @patch("client.get_json")  # Mock get_json to ensure no real HTTP call is made
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Arrange: Create an instance of GithubOrgClient with the given org_name
        client = GithubOrgClient(org_name)

        # Act: Call the .org property of the client
        client.org

        # Assert: Check that get_json was called exactly once with the correct URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)


# Run the tests if this script is executed directly
if __name__ == "__main__":
    unittest.main()
