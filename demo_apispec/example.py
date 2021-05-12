import marshmallow as ma

from flask_apispec import ResourceMeta, Ref, doc, marshal_with, use_kwargs


class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type


class PetSchema(ma.Schema):
    name = ma.fields.Str()
    type = ma.fields.Str()



import flask
import flask.views

from flask_apispec import FlaskApiSpec

app = flask.Flask(__name__)
docs = FlaskApiSpec(app)

@app.route('/pets/<pet_id>')
@doc(params={'pet_id': {'description': 'pet id'}})
@marshal_with(PetSchema)
@use_kwargs({'breed': ma.fields.Str()})
def get_pet(pet_id):
    return Pet('haha', 'cat')

docs.register(get_pet)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")