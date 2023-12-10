from flask import app,Flask
from flask_restx import Api, fields
from .extensions import api

model = api.model('Name Model', 
		  {'name': fields.String(required = True, 
					 description="Name of the person", 
					 help="Name cannot be blank."),
            'id': fields.Integer(required = True,
                                 description = "Id of the name",
                                 help="Id cannot be black.")       
        	})