import unittest
from unittest import mock

import requests


class Demo2(unittest.TestCase):

    def request_post(self):
        url = "https://www.baidu.com"
        data = {
            "username": "wuhengyu"
        }

        self.res = requests.post(url=url, data=data)
        return self.res

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    def test01(self):
        data = {
            "username": "wuhengyu"
        }
        request_post = mock.Mock(return_value=data)
        res = self.request_post
        self.assertEqual({"username": "wuhengyu"}, res)
