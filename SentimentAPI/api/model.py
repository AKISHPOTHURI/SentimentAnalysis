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
modelarray = api.model('model',
    {
        # 'text': fields.List((fields.String(required = True)))
        'text': (fields.String(required = True))
	}
)

# Model for file upload response
upload_response = api.model('UploadResponse', {
    'message': fields.String(description='Upload status message'),
    'data': fields.Raw(description='Processed data from uploaded file')
})