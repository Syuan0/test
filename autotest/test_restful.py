import json
import os
import unittest
from app_run import a


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.app = a
        a.config['TESTING'] = True
        self.client = a.test_client()

    def test_app_exists(self):
        # test get_method
        response = self.client.get('/ceshi')
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        code = resp_dict.get('code')
        self.assertEqual(code, 200)

        # test post_method
        response = self.client.post('/ceshi', data=json.dumps({"username": "zhangsan", "age": 18}))
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        user_name = resp_dict.get('username')
        msg = resp_dict.get('msg')
        self.assertIsInstance(user_name, str)
        self.assertEqual(msg, 'success')

    def tearDown(self) -> None:
        pass
