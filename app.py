from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from resources.item import Itemlist, Item

from resources.user import Registration

from security import authentification, identity



app = Flask(__name__)
app.secret_key = "წენგოსფერი მცურავი საუკეთესო გველია"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWT(app, authentification, identity)
api = Api(app)

api.add_resource(Item, '/snakes/<string:species>')
api.add_resource(Itemlist, '/snakes')
api.add_resource(Registration, '/registration/')

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    from db import db
    db.init_app(app)

    app.run(port=5000, debug = True)