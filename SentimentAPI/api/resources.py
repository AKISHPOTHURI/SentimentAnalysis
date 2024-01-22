import os
import pathlib
import emoji
from flask import request
from flask_restx import Resource, Namespace, reqparse
import pandas as pd
from werkzeug.datastructures import FileStorage
from flask.views import MethodView
from api.model import model, modelarray
from api.model_load import load_model
from api.textToTokens import testToTokens

from transformers import AutoTokenizer,AutoModelForSequenceClassification
import torch

from Sentiment.config.configuration import ConfigurationManager
from Sentiment.pipeline.prediction import PredictionPipeline
from transformers import AutoTokenizer
from transformers import pipeline


ns = Namespace("api")

@ns.route("/getModelInfo")
class getModelInfo(Resource):
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

@ns.route("/getSentiment")
class getSentiment(Resource):
    @ns.expect(modelarray)
    def post(self):
        try:
                    # texts_parser = reqparse.RequestParser()
                    data = request.json['text']
                    model = load_model.load()
                    # result = PredictionPipeline.prediction("The food is too spicy. Unable to eat this food.")
                    print(model.summary())
                    classToken = testToTokens()
                    abc = []
                    # for text in data:
                    abc.append(data)
                    padded = classToken.Tokens(data)
                    result = model.predict(padded)
                    obj = {
                            'text':data,
                            'percentage':round(result[0][0]*100),
                            'sentiment': 1 if round(result[0][0]*100) > 50 else 0
                        }
                    print(obj)
                    print("array:",abc)
                    print(result)
                    # c = "This is good i have ever ate"
                    # padded = classToken.Tokens(c)
                    result = model.predict(padded)
                    # print("data",data)
                    print("result", result)
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
                 classToken = testToTokens()
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

@ns.route('/Custompredict')
class PredictionPipeline(Resource):
    @ns.expect(modelarray)
    def post(self):
        self.modelname = 'DistilBertModel'
        text = request.json['text']
        text = emoji.demojize(text).replace(":",'').replace("_"," ")
        tok = AutoTokenizer.from_pretrained(self.modelname)
        mod = AutoModelForSequenceClassification.from_pretrained(self.modelname)
        input_ids = tok.encode(text, return_tensors='pt')
        output = mod(input_ids)
        preds = torch.nn.functional.softmax(output.logits, dim=-1)
        prob = torch.max(preds).item()
        idx = torch.argmax(preds).item()
        # sentiment = id2label[idx]

        return {'text':text,'sentiment':idx, 'prob':round(prob,3)}
    
@ns.route('/customUploadExcel')
class customUploadExcel(Resource):
     @ns.expect(upload_parser)
     def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        result = []
        self.modelname = 'DistilBertModel'
        tok = AutoTokenizer.from_pretrained(self.modelname)
        mod = AutoModelForSequenceClassification.from_pretrained(self.modelname)
        if uploaded_file:
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            try:
                 data = pd.read_excel(file_path)
                 dataValues = data['Reviews'].values
                 for review in dataValues:
                      review = emoji.demojize(review).replace(":",'').replace("_"," ")
                      input_ids = tok.encode(review, return_tensors='pt')
                      output = mod(input_ids)
                      preds = torch.nn.functional.softmax(output.logits, dim=-1)
                      prob = torch.max(preds).item()
                      idx = torch.argmax(preds).item()
                      result.append({
                            'text':review,
                            'sentiment':idx,
                            'percentage': round(prob*100)
                      })
                 return {'message': 'File uploaded successfully.', 'result': result}, 200
            except Exception as e:
                 return {'error': str(e)}, 500
        return {'error': 'No file uploaded.'}, 400

@ns.route('/trainModel')
class trainModel(Resource):
     def post(self):
          try:
            os.system("python main.py")
            return {'message':'Training Done Successfully.'},200
          except Exception as e:
               return {'error': 'Training Failed.'}, 400

         
@ns.route('/trainDVC')
class trainDVC(Resource):
     def post(self):
          try:
            os.system("dvc repro")
            return {'message':'Data and pipelines are up to date.'},200
          except Exception as e:
               return {'error': 'Data and pipelines Failed.'}, 400
 