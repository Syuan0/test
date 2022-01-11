import json

from flask import request, render_template
from flask_restx import Resource, fields, Namespace
from apis import db

from model import UserConfigs

ns = Namespace("usersconfig", description="Users config CURD api.", path="/")


@ns.route("/config/<user_key>")
class UserConfig(Resource):
    def get(self, user_key):
        config = UserConfigs.query.filter(UserConfigs.key == user_key).first()
        if config:
            code = 200
            msg = f"request succeed. details {user_key}:{config.value}"
        else:
            code = 404
            msg = f"No details about {user_key}"
        return {"code": code, "msg": msg}

    def put(self, user_key):
        # data :{user_key:user_value} eg:{"yuanshuai": 'yuan'}
        if not request.data:
            return {"code": 400, "msg": "wrong request arg format"}
        data = json.loads(request.data.decode("utf-8"))
        value = data.get(user_key, None)
        if value is not None:
            target_key = UserConfigs.query.filter(UserConfigs.key == user_key).first()
            if target_key:
                target_key.value = data.get(user_key)
                msg = f"modify {user_key} detail successfully"
            else:
                userconfig = UserConfigs(key=user_key, value=data.get(user_key))
                db.session.add(userconfig)
                msg = f"add {user_key} detail successfully"
            code = 200
            db.session.commit()
        else:
            code = 400
            msg = "request args error"
        return {"code": code, "msg": msg}

# from model import User
# ns = Namespace("users",description="Users CURD api.",path="/")
#
# user_model = ns.model('UserModel', {
#     'user_id': fields.String(readOnly=True, description='The user unique identifier'),
#     'username': fields.String(required=True, description='The user nickname'),
#     'age': fields.Integer(),
#     'msg':fields.String(),
#
# })
# user_list_model = ns.model('UserListModel', {
#     # 'users': fields.List(fields.Nested(user_model)),
#     # 'total': fields.Integer,
#     'code':fields.Integer(),
#     'msg':fields.String(),
# })
#
#
# @ns.route("/ceshi")
# class UserListApi(Resource):
#     # 初始化数据
#     users = [User("HanMeiMei",17), User("LiLei",19)]
#
#     @ns.doc('get_user_list')
#     @ns.marshal_with(user_list_model)
#     def get(self):
#         return {
#             # "users": self.users,
#             # "total": len(self.users),
#             'code':200,
#             'msg':'success'
#         }
#
#     @ns.doc('create_user')
#     # @ns.expect(user_model)
#     @ns.marshal_with(user_model, code=201)
#     def post(self):
#         # user = User(api.payload['username'])
#         data=json.loads(request.get_data())
#         name=data.get("username")
#         ages=data.get('age')
#         user=User(name,ages)
#         return {'msg':'success',
#                 'user_id':user.user_id,
#                 'username':user.username,
#                 'age':user.age
#                 }
