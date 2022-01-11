from flask import Flask
from flask_migrate import Migrate


def register_api():
    from apis.user_api import ns as user_api
    from apis import api
    api.add_namespace(user_api)


app = Flask("Flask-Web-Demo")
# config
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///D:/ceshi_sqlite/ceshi.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# register api namespace
register_api()

# register blueprint
from apis import api_blueprint, db
db.init_app(app)
# db.drop_all()
# db.create_all()
app.register_blueprint(api_blueprint)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True, port=40000)
