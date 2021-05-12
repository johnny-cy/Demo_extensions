from marshmallow import fields, Schema
from flask_apispec import ResourceMeta, Ref, doc, marshal_with, use_kwargs

class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type



class PetSchema(Schema):
    name = fields.Str()
    type = fields.Str()

pet_schema = PetSchema( only=['name', 'type'])

from flask import Flask, views
from flask_apispec import FlaskApiSpec


app = Flask(__name__)
docs = FlaskApiSpec(app)


@app.route("/pets/<pet_id>")
@doc(params={'pet_id': {'description': 'pet_id'}}) # swagger 
@marshal_with(pet_schema)
def get_pet(pet_id):
    return Pet('hehe', 'cat')

docs.register(get_pet) # register method get_pet to swagger

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
