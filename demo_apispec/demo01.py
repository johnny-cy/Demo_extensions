import marshmallow as ma
from flask_apispec import ResourceMeta, Ref, doc, marshal_with, use_kwargs


class Pet:
    def __init__(self, name, type):
        self.name = name
        self.type = type



from flask import Flask, views
from flask_apispec import FlaskApiSpec


app = Flask(__name__)
docs = FlaskApiSpec(app)

@app.route("/pets/<pet_id>")
@doc(params={'pet_id': {'description': 'pet_id'}}) # swagger 
def get_pet(pet_id):
    return Pet('calici', 'cat')

docs.register(get_pet) # register method get_pet to swagger

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


"""
TypeError: Object of type Pet is not JSON serializable
"""