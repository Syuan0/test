from apis import db


class UserConfigs(db.Model):
    __tablename__ = "userconfigs"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64))
    value = db.Column(db.String(64))

    def __str__(self):
        return f"id:{self.id}, key:{self.key}, value {self.value}."
