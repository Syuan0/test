import json

from flask import request
from flask_restplus import Resource, fields, Namespace

from model import User
from apis import api

ns = Namespace("users",description="Users CURD api.",path="/")


user_model = ns.model('UserModel', {
    'user_id': fields.String(readOnly=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user nickname'),
    'age': fields.Integer(),
    'msg':fields.String(),

})
user_list_model = ns.model('UserListModel', {
    # 'users': fields.List(fields.Nested(user_model)),
    # 'total': fields.Integer,
    'code':fields.Integer(),
    'msg':fields.String(),
})


@ns.route("/ceshi")
class UserListApi(Resource):
    # 初始化数据
    users = [User("HanMeiMei",17), User("LiLei",19)]

    @ns.doc('get_user_list')
    @ns.marshal_with(user_list_model)
    def get(self):
        return {
            # "users": self.users,
            # "total": len(self.users),
            'code':200,
            'msg':'success'
        }

    @ns.doc('create_user')
    # @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        # user = User(api.payload['username'])
        data=json.loads(request.get_data())
        name=data.get("username")
        ages=data.get('age')
        user=User(name,ages)
        return {'msg':'success',
                'user_id':user.user_id,
                'username':user.username,
                'age':user.age
                }