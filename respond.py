from flask import Flask, Response # Basic Flask
from flask_restful import Resource, Api # Api for restful
from data import Dict

app = Flask(__name__)
api = Api(app)
dico = Dict()

class Rest(Resource):
    def get(self, name):
        return Response(dico.get_inclusive(name) + "\n", mimetype='text/html')

class Web(Resource):
    def get(self, name):
        inclusive = dico.get_inclusive(name)
        html = "<p>{0} en écriture inclusive donne {1}  </p>".format(name, inclusive)
        return Response(html, mimetype='text/html')

class Index(Resource):
    def get(self):
        html = "<h1> Index </h1>" + dico.generate_html_dict()
        return Response(html, mimetype='text/html')

    
api.add_resource(Rest,'/api/<string:name>')
api.add_resource(Web,'/web/<string:name>')
api.add_resource(Index, '/')

if __name__ == "__main__":
    app.run(port=5002)
