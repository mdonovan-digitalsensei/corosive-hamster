from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from item import Item, ItemsList
from security import authenticate, identity
from user import UserRegister

app = Flask(__name__)
app.secret_key = "dave"
api = Api(app)

jwt = JWT(app, authenticate, identity)

if __name__ == "__main__":
    api.add_resource(Item, "/item/<string:name>")
    api.add_resource(ItemsList, "/items")
    api.add_resource(UserRegister, "/register")
    app.run(port=5000, debug=True)
