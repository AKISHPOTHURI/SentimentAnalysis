from flask import request
from flask_restx import Resource, Namespace

from .model import model
ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        a = [
        {
            'name':"Akish",
            'age':25
        },
        {
            'name':"Akshith",
            'age':30
        }
        ]
        b = []
        for obj in a:
            b.append({
                'name':obj['name'],
                'age':obj['age']
            })
        return b
    @ns.expect(model)
    def post(self):
        list_of_names = {}
        try:
                    id = request.json['id']
                    list_of_names[id] = request.json['name']
                    return {
                            "status": "New person added",
				            "name": list_of_names[id]
                    }
        except KeyError as e:
              ns.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
        except KeyError as e:
              ns.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")
