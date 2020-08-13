from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
                "id" : self.id,
                "username" : self.username,
                "password" : self.password,
                }


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, userid):
        return cls.query.filter_by(id=userid).first()

    @classmethod
    def user_info(cls, username):
        return cls.query.filter_by(username=username)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

