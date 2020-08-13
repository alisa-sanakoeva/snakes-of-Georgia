from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help="აუცილებელია ლოკაციის შეყვანა")
    parser.add_argument('date',
                        type=str,
                        required=True,
                        help="აუცილებელია დაფიქსირების თარიღის შეყვანა")
    parser.add_argument('latin_name',
                        type=str,
                        required=True,
                        help="აუცილებელია ლათინური დასახელების შეყვანა")

    def get(self, species):
        item = ItemModel.find_by_name(species)
        if item:
            return item.json()
        return {'message': f'მონაცემი {species} ბაზაში ვერ მოიძებნა'}, 404

    def post(self, species):

        if ItemModel.find_by_name(species):
            return {"message" : f"მონაცემი {species} უკვე არსებობს"}, 400

        data = Item.parser.parse_args()

        item = ItemModel(species, data["latin_name"], data["location"], data["date"])

        try:
            item.save_to_db()
        except Exception as e:
            return {"message" : f'{e}'}
        else:
            return  f'შექმნილი პარამეტრი: {item.json()}', 200


    def put(self, species):

        item = ItemModel.find_by_name(species)
        data = Item.parser.parse_args()
        if item:
            item.latin_name = data["latin_name"]
            item.location = data["location"]
            item.date = data["date"]

        else:
            item = ItemModel(species, data["latin_name"], data["location"], data["date"])

        item.save_to_db()

        return {"message" : f"შენახულია მონაცემი {item.json()}"}

    def delete(self, species):
        item = ItemModel.find_by_name(species)

        if item:
            item.delete_from_db()
            return {"message" : f"{species} წაშლილია ბაზიდან"}
        else:
            return {"message" : f"{species} ბაზაში არც არასდროს გვყოლია"}


class Itemlist(Resource):
    @jwt_required()
    def get(self):
        items = ItemModel.query.filter_by().all()
        snakes = []
        for i in items:
            snakes.append(i.json())
        return {"message" : snakes}
