from flask import request
from flask_restx import Resource, Namespace, reqparse

from .model import model, modelarray
from .model_load import load_model
from .Helpers.texttotokens import testToTokens 

ns = Namespace("api")

@ns.route("/getdata")
class Sentiment(Resource):
    def get(self):

        model = load_model.load()
        print(model.summary())
        c = "It is too spicy. So, the not reach my expectations."
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
    @ns.expect(modelarray)
    def post(self):
        try:
                    # texts_parser = reqparse.RequestParser()
                    model = load_model.load()
                    print(model.summary())
                    classToken = testToTokens()
                    abc = []
                    data = request.json['text']
                    for text in data:
                        abc.append(text)
                        padded = classToken.Tokens(text)
                        result = model.predict(padded)
                        obj = {
                                'text':text,
                                'percentage':round(result[0][0]*100),
                                'sentiment': 1 if round(result[0][0]*100) > 50 else 0
                          }
                    print(obj)
                    print("array:",abc)
                    print(result)
                    # c = "This is good i have ever ate"
                    # padded = classToken.Tokens(c)
                    # result = model.predict(padded)
                    # # print("data",data)
                    # print("result", result)
                    return obj
                    # return {
                    #         "status": "New person added",
				    #         "name": c
                    # }
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