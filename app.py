from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource

from PIL import Image
from pytesseract import pytesseract

app = Flask(__name__)
api = Api(app)

class Extract(Resource):
    def post(self):
        file_=request.files['img']
        img=Image.open(file_)
        text=pytesseract.image_to_string(img)
        return {'text':text}, 201

## Actually setup the Api resource routing here
api.add_resource(Extract, '/')


if __name__ == '__main__':
    app.run(debug=True)
