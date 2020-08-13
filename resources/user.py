from flask_restful import Resource, reqparse
from models.user import UserModel

class Registration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="შეიყვანეთ მომხმარებლის სახელი")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="შეიყვანეთ პაროლი")


    def post(self):

        data = Registration.parser.parse_args()
        user = UserModel(data["username"], data["password"])

        if UserModel.find_by_username(data["username"]):
            return {"message" : f"მომხმარებლის სახელი {data['username']} უკვე არსებობს"}, 400

        try:
            user.save_user()
        except Exception as e:
            return {"message" : f'{e}'}
        else:
            return  f'შექმნილია მომხმარებელი: {user.json()}', 200


    def delete(self):
        data = Registration.parser.parse_args()
        item = UserModel.find_by_username(data["username"])
        if item:
            if data['password'] == item.json()["password"]:
                item.delete_user()
                return {"message" : f"მომხმარებელი {data['username']} წაშლილია"}
            else:
                return {"message" : "პაროლი არასწორადაა შეყვანილი"}
        else:
            return {"message" : f"მომხმარებელი {data['username']} არ არსებობს"}
