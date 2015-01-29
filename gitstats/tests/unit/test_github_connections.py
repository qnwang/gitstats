# -*- coding: utf-8 -*-

from datetime import date
from unittest import TestCase

from gitstats.lib.github_connection import GithubConnection

class GithubConnectionTests(TestCase):

    def setUp(self):
        self.uri = "https://api.github.com/users/"

    def tearDown(self):
        pass

    def test_method_add_params_with_no_param(self):
        """Test the method _add_params with no param, the method adds by default the param per_page=100"""

        github_connection = GithubConnection("Dogild")
        uri = github_connection._add_params(self.uri, dict())

        assert uri == "https://api.github.com/users?per_page=100"

    def test_method_add_params_with_param(self):
        """Test the method _add_params with params, the method adds by default the param per_page=100"""

        github_connection = GithubConnection("Dogild")
        params = dict()
        params["test"] = "32"
        uri = github_connection._add_params(self.uri, params)

        assert uri == "https://api.github.com/users?test=32&per_page=100"