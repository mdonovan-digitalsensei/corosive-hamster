from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resource.item import Item, ItemsList
from security import authenticate, identity
from resource.user import UserRegister
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
app.secret_key = "dave"
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemsList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
