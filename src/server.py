from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name":"ABC",
        "age":23,
        "occupation":"Developer"
    },
    {
        "name":"DEF",
        "age":25,
        "occupation":"Enginner"
    },
    {
        "name":"IJK",
        "age":32,
        "occupation":"Architect"
    }
]

class User(Resource):

    def get(self, name):
        for user in users:
            if name == user['name']:
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')
        args = parser.parse_args()

        for user in users:
            if name == user['name']:
                return "User already exists", 400

        user = {
            "name":name,
            "age":args['age'],
            "occupation":args['occupation']
        }

        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')
        args = parser.parse_args()

        for user in users:
            if name == user['name']:
                user['age'] = args['age']
                user['occupation'] = args['occupation']
                return user, 200

        user = {
            "name":name,
            "age":args['age'],
            "occupation":args['occupation']
        }
        users.append(user)
        return user, 201

    def delete(self, name):

        return "User with the name {} have been deleted".format(name), 200

api.add_resource(User, '/user/<string:name>')

if __name__ == '__main__':
    app.debug = True
    app.run()

