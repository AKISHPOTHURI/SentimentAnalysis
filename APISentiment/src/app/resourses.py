import os
from flask import request
from flask_restx import Resource, Namespace, reqparse
import pandas as pd
from werkzeug.datastructures import FileStorage

# from .model import model, modelarray
# from .model_load import load_model
# from .Helpers.texttotokens import testToTokens
from .utils import model, texttotokens
from .model_load import load_model
from .utils.model import modelarray

ns = Namespace("api")

@ns.route("/getModelInfo")
class getModelInfo(Resource):
    def get(self):

        # model = load_model.load()
        # print(model.summary())
        # c = "It is too spicy. So, the not reach my expectations."
        # classToken = texttotokens.testToTokens()
        # padded = classToken.Tokens(c)
        # result = model.predict(padded)
        # print(result[0][0])
        a = [
        {
            'name':"Akish",
            'age':25.0
        },
        {
            'name':"Akshith",
            'age':30.0
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
    
@ns.route("/getSentiment")
class getSentiment(Resource):
    @ns.expect(modelarray)
    def post(self):
        try:
                    # texts_parser = reqparse.RequestParser()
                    # model = load_model.load()
                    # print(model.summary())
                    # classToken = texttotokens.testToTokens()
                    abc = []
                    data = request.json['text']
                    for text in data:
                        abc.append(text)
                        # padded = classToken.Tokens(text)
                        # result = model.predict(padded)
                        result = "this is akish"
                        obj = {
                                'text':"Akish",
                                'percentage':round(0.085*100),
                                'sentiment': 1 if round(0.085*100) > 50 else 0
                          }
                    print(obj)
                    print("array:",abc)
                    print(result)
                    # c = "This is good i have ever ate"
                    # padded = classToken.Tokens(c)
                    # result = model.predict(padded)
                    # # print("data",data)
                    # print("result", result)
                    return obj,200
                    # return {
                    #         "status": "New person added",
				    #         "name": c
                    # }
        except KeyError as e:
              ns.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
        except KeyError as e:
              ns.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")

# app = CreateApp()
# # Create a directory for file uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Configuring the upload location for files using Flask's config
# File upload parser
upload_parser = ns.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)


@ns.route('/UploadExcel')
class uploadExcel(Resource):
     @ns.expect(upload_parser)
     def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        result = []
        if uploaded_file:
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            try:
                 model = load_model.load()
                 data = pd.read_excel(file_path)
                 data = data['Reviews'].values
                 classToken = texttotokens.testToTokens()
                 for review in data:
                      prediction = model.predict(classToken.Tokens(review))
                      result.append({                         
                            'text':review,
                            'Prediction':round(prediction[0][0]*100),
                            'sentiment': 1 if round(prediction[0][0]*100) > 50 else 0
                      })
                 return {'message': 'File uploaded successfully.', 'result': result}, 200
            except Exception as e:
                 return {'error': str(e)}, 500
        return {'error': 'No file uploaded.'}, 400