import os
from flask import Flask, request, jsonify, make_response
import db_service
from flasgger import Swagger, swag_from
from dotenv import load_dotenv
from swagger.config import swagger_config
from dateutil import parser

load_dotenv()

app = Flask(__name__)
swagger = Swagger(app, config=swagger_config)

db_service.init()


@app.route('/')
def index():
  return "Welcome to API"

@app.route('/skader', methods=['GET'])
@swag_from('swagger/get_skader.yml')
def get_skader():
    skader = db_service.get_skader()

    if skader is None:
        return make_response({'message': 'Ingen skader fundet'}, 404)

    return make_response(skader, 200)

@app.route('/skader', methods=['POST'])
@swag_from('swagger/post_skader.yml')
def create_skade():
    data = request.json

    skade_type = data.get('skade_type')
    skade_pris = data.get('skade_pris')
    nummerplade = data.get('nummerplade')
    syn_type = data.get('syn_type')
    indberetnings_dato = data.get('indberetnings_dato')


    if skade_type is None or skade_pris is None or nummerplade is None or syn_type is None or indberetnings_dato is None:
        return make_response({'message': 'Alle felter skal udfyldes'}, 400)

    if not isinstance(skade_pris, int) or skade_pris < 0:
        return make_response({'message': 'Prisen skal være et positivt heltal'}, 400)

    if not isinstance(nummerplade, str) or len(nummerplade) != 6:
        return make_response({'message': 'Forkertnummerplade format'}, 400)

    if not isinstance(syn_type, str) or syn_type not in ['Under Aftale', 'Efter Aftale']:
        return make_response({'message': 'Forkert syn type'}, 400)

    ## dato tjek

    if not isinstance(indberetnings_dato, str):
        return make_response({'message': 'Datoen skal være en streng'}, 400)

    # Format: YYYY-MM-DD
    try:
        bool(parser.parse(indberetnings_dato))
    except ValueError:
        return make_response({'message': 'Datoen er ikke i korrekt format; YYYY-MM-DD'}, 400)

    data = db_service.post_skade(skade_type, skade_pris, nummerplade, syn_type, indberetnings_dato)

    return make_response(data, 201)

if __name__ == '__main__':
    app.run()
