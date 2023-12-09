from flask_restx import Resource, Namespace

ns = Namespace("api")

@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"about": "restx"}