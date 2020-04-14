import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.itemmodel import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "price", type=float, required=True, help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return (
                {"message": "An item with name '{}' already exists.".format(name)},
                400,
            )

        data = Item.parser.parse_args()
        item = ItemModel(name, data["price"])
        # try:
        item.insert()
        # except:
        #    return {"message": "An error occured"}, 500
        return item.json(), 201

        return item, 201

    def delete(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE item=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {"message": "Item deleted"}

    def put(self, name):

        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data["price"])

        if item is None:
            updated_item.insert()
        else:
            updated_item.update()
        return updated_item.json()


class ItemsList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = result.fetchall()
        connection.close()
        return {"items": items}