#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient class methods
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test TestGithubOrgClient's org method
        """
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """
        mocking property
        """
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as mock_pro:
            mock_pro.return_value = {"repos_url": "89"}
            test_org = GithubOrgClient('holberton')
            test_repo_url = test_org._public_repos_url
            self.assertEqual(test_repo_url, mock_pro.return_value.get('repos_url'))
            mock_pro.assert_called_once()

    @patch('client.get_json', return_value=[{'name': 'jil'},
                                            {'name': 'fw'},
                                            {'name': 'sher'}])
    def test_public_repos(self, mock_repo):
        """
        Test GithubOrgClient's public_repos method
        """
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as mock_pro:
            test_client = GithubOrgClient('jil')
            test_repo = test_client.public_repos()
            for idx in range(3):
                self.assertIn(mock_repo.return_value[idx]['name'], test_repo)
            mock_repo.assert_called_once()
            mock_pro.assert_called_once()
