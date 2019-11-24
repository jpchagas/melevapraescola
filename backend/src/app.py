from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

from models.escola import *

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
database_name = 'crud.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, database_name)
db = SQLAlchemy(app)
ma = Marshmallow(app)

escolas_schema = EscolaSchema(many=True)
escola_schema = EscolaSchema()
contato_schema = ContatoSchema()


# endpoint para exibir todas escolas
@app.route("/escola", methods=["GET"])
def get_escola():
    all_escolas = Escola.query.with_entities(Escola.nome, Escola.localizacao).all()
    result = escolas_schema.dump(all_escolas)
    return jsonify(result)

# endpoint para pegar os detalhes da escola pelo id
@app.route("/escola/<id>", methods=["GET"])
def escola_details(id):
    escola = Escola.query.get(id)
    return escola_schema.jsonify(escola)

# endpoint para pegar os detalhes da escola pelo id
@app.route("/contato/<id>", methods=["GET"])
def contato_details(id):
    s = db.session.query(Escola, Contato)\
        .filter(Contato.id == id).filter(Escola.id == id)\
            .first()
    print(s)
    return escola_schema.jsonify(s)
#.with_entities(Escola.nome, Contato.numero)\


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0') 