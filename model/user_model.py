import uuid


class User(object):
    user_id = None
    username = None

    def __init__(self, username: str, age: int):
        self.user_id = str(uuid.uuid4())
        self.username = username
        self.age = age