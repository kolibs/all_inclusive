from flask import Flask, Response, render_template # Basic Flask
from flask_restful import Resource, Api # Api for restful
from data import Dict

app = Flask(__name__)
api = Api(app)
dico = Dict()

# Respond for terminal
class Rest(Resource):
    def get(self, name):
        respond = dico.get_inclusive(name) + "\n"
        return Response(respond, mimetype='text/html')

# Respond for web resource
class Web(Resource):
    def get(self, name):
        inclusive = dico.get_inclusive(name)
        html = "<p>{0} en écriture inclusive donne {1}  </p>".format(name, inclusive)
        return Response(html, mimetype='text/html')

# Index page
class Index(Resource):
    def get(self):
      sorted_dico = dico.sort()
      return Response(render_template("index.html", sorted_dico = sorted_dico), mimetype='text/html')
        


# Main function 
if __name__ == "__main__":
    api.add_resource(Rest,'/api/<string:name>')
    api.add_resource(Web,'/web/<string:name>')
    api.add_resource(Index, '/')
    app.run(port=5002)
