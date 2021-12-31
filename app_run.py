from flask import Flask


def create_app():
    app = Flask("Flask-Web-Demo")
    # register api namespace
    register_api()
    # register blueprint
    from apis import api_blueprint
    app.register_blueprint(api_blueprint)
    return app


def register_api():
    from apis.user_api import ns as user_api
    from apis import api
    api.add_namespace(user_api)


a = create_app()

if __name__ == '__main__':
    a.run(debug=True, port=40000)
