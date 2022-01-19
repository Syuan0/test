import unittest

from apis import db
from app_run import app
from model import UserConfigs


class TestClass(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////home/yuanshuai/developer/ceshi/ceshi.db"
        db.app = app
        db.create_all()

    def test_add_detail(self):
        add_user_key = "add_key"
        add_value = "add_value"
        u = UserConfigs(key=add_user_key, value=add_value)
        db.session.add(u)
        db.session.commit()
        user = UserConfigs.query.filter_by(key=add_user_key).first()
        self.assertIsNotNone(user)

    def test_modify_value(self):
        add_user_key = "modify_key"
        add_value = "add_value"
        u = UserConfigs(key=add_user_key, value=add_value)
        db.session.add(u)
        db.session.commit()
        u.value="modify_value"
        db.session.commit()
        user = UserConfigs.query.filter_by(key=add_user_key).first()
        self.assertEqual("modify_value",user.value)

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
