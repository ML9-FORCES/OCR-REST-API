from flask import Flask
from flask_restful import Api

#Modules
from common.util import Format
from resources.extract import Extract
from resources.validate import Validate

#initiate
app = Flask(__name__)
api = Api(app)

#Routes
api.add_resource(Extract, '/')
api.add_resource(Validate, '/gps')

#Run
if __name__ == '__main__':
    app.run(debug=True)
