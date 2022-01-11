import json
import unittest
from datetime import datetime

from app_run import app


class TestClass(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_get_wrong_user_key(self):
        response = self.client.get("/config/ceshi_key")
        resp_dict = json.loads(response.data)
        code = resp_dict.get('code')
        self.assertIn("msg", resp_dict, "wrong data format")
        self.assertEqual(code, 404, "wrong return_status_code")

    def test_get_exist_user_key(self):
        arg = "16_key"
        response = self.client.get(f"/config/{arg}")
        resp_dict = json.loads(response.data)
        code = resp_dict.get('code')
        self.assertIn(arg, resp_dict.get("msg"), "wrong message")
        self.assertEqual(code, 200, "wrong return_status_code")

    def test_put_without_args(self):
        arg = "17_key"
        response = self.client.put(f"/config/{arg}")
        resp_dict = json.loads(response.data)
        code = resp_dict.get('code')
        self.assertIn("wrong request arg format", resp_dict.get("msg"), "wrong message")
        self.assertEqual(code, 400, "wrong return_status_code")

    def test_put_wrong_key_args(self):
        arg = "18_key"
        data = {"ceshi_key": "ceshi_value"}
        response = self.client.put(f"/config/{arg}", data=json.dumps(data))
        resp_dict = json.loads(response.data)
        code = resp_dict.get('code')
        self.assertIn("msg", resp_dict, "wrong data format")
        self.assertEqual(code, 400, "wrong return_status_code")
        self.assertIn("request args error", resp_dict.get("msg"), "wrong message")

    def test_put_modify_info(self):
        modify_value = datetime.now().strftime("%Y%m%d%H%M")
        response = self.client.put(f"/config/19_key", data=json.dumps({"19_key": f"{modify_value}"}))
        resp_dict = json.loads(response.data)
        code = resp_dict.get('code')
        self.assertIn("msg", resp_dict, "wrong data format")
        self.assertEqual(code, 200, "wrong return_status_code")
        self.assertIn("modify 19_key detail successfully", resp_dict.get("msg"), "wrong message")

    def test_put_add_info(self):
        t = datetime.now().strftime("%Y%m%d%H%M")
        arg = f"{t}_key"
        response = self.client.put(f"/config/{arg}", data=json.dumps({arg: "add_value"}))
        resp_dict = json.loads(response.data)
        code = resp_dict.get('code')
        self.assertIn("msg", resp_dict, "wrong data format")
        self.assertEqual(code, 200, "wrong return_status_code")
        self.assertIn(f"add {arg} detail successfully", resp_dict.get("msg"), "wrong message")

