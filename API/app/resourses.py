from flask import request
from flask_restx import Resource, Namespace

from .model import model
from .model_load import load_model
from .Helpers.texttotokens import testToTokens 

ns = Namespace("api")

@ns.route("/getdata")
class Sentiment(Resource):
    def get(self):

        model = load_model.load()
        print(model.summary())
        c = "This is good i have ever ate"
        classToken = testToTokens()
        padded = classToken.Tokens(c)
        result = model.predict(padded)
        print(result[0][0])
        a = [
        {
            'name':"Akish",
            'age':25.0
        },
        {
            'name':"Akshith",
            'age':30.0
        },{
              'name': c,
              'age': round(result[0][0]*100)
        }
        ]
        # print("model loaded")
        b = []
        for obj in a:
            b.append({
                'name':obj['name'],
                'age':obj['age']
            })
        return b
    
@ns.route("/update")
class senti(Resource):
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

# class model(Resource):
#     def get(self):
#         try:
#             model = load_model.load()
#             print(model.summary())
#             return "model loaded"
#         except KeyError as e:
#              ns.abort(500, e.__doc__, status = "Could not load model", statusCode = "500")