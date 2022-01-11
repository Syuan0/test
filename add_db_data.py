from apis import db
from app_run import app
from model import UserConfigs

configs = []
for num in range(1, 101):
    try:
        config = UserConfigs()
        config.key = "%d_key" % num
        config.value = "%d_value" % num
        configs.append(config)
        print(config.value)
    except Exception as e:
        print(e)
# 手动开启一个app的上下文
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all(configs)
    db.session.commit()
