from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

import json

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

database_name = 'TestDB1.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, database_name)
db = SQLAlchemy(app)
ma = Marshmallow(app)



# ------------------------ MODELS ------------------------

# Contato

class Contato(db.Model):
    __tablename__ = 'CONTATO'

    co_entidade = db.Column(db.Integer(), primary_key=True)
    nu_ddd = db.Column(db.Integer(), unique=False)
    nu_telefone_publico = db.Column(db.Integer(), unique=False)
    email = db.Column(db.String(80), unique=False)
    url_website = db.Column(db.String(80), unique=False)

    def __init__(self, co_entidade, nu_ddd, nu_telefone_publico, email, url_website):
        self.co_entidade = co_entidade
        self.nu_ddd = nu_ddd
        self.nu_telefone_publico = nu_telefone_publico
        self.email = email
        self.url_website = url_website

class ContatoSchema(ma.Schema):
    class Meta:
        model = Contato
        fields = ('co_entidade', 'nu_ddd', 'nu_telefone_publico', 'email', 'url_website')

contato_schema = ContatoSchema()
contatos_schema = ContatoSchema(many=True)


# Infra

class Infra(db.Model):
    __tablename__ = 'INFRA'

    co_entidade = db.Column(db.Integer(), primary_key=True, unique=True)
    in_laboratorio_informatica = db.Column(db.Integer())
    in_quadra_esportes_coberta = db.Column(db.Integer())
    in_quadra_esportes_descoberta = db.Column(db.Integer())
    in_biblioteca = db.Column(db.Integer())
    in_sala_leitura = db.Column(db.Integer())
    in_parque_infantil = db.Column(db.Integer())
    in_refeitorio = db.Column(db.Integer())
    in_patio_coberto = db.Column(db.Integer())
    in_patio_descoberto = db.Column(db.Integer())
    in_area_verde = db.Column(db.Integer())
    in_internet = db.Column(db.Integer())


    def __init__(self, co_entidade, in_laboratorio_informatica, in_quadra_esportes_coberta, in_quadra_esportes_descoberta, in_biblioteca, in_sala_leitura, in_parque_infantil, in_refeitorio, in_patio_coberto, in_patio_descoberto, in_area_verde, in_internet):
        self.co_entidade = co_entidade
        self.in_laboratorio_informatica = in_laboratorio_informatica
        self.in_quadra_esportes_coberta = in_quadra_esportes_coberta
        self.in_quadra_esportes_descoberta = in_quadra_esportes_descoberta
        self.in_biblioteca = in_biblioteca
        self.in_sala_leitura = in_sala_leitura
        self.in_parque_infantil = in_parque_infantil
        self.in_refeitorio = in_refeitorio
        self.in_patio_coberto = in_patio_coberto
        self.in_patio_descoberto = in_patio_descoberto
        self.in_area_verde = in_area_verde
        self.in_internet = in_internet

class InfraSchema(ma.Schema):
    class Meta:
        model = Infra
        fields = ('co_entidade', 'in_laboratorio_informatica', 'in_quadra_esportes_coberta', 'in_quadra_esportes_descoberta', 'in_biblioteca', 'in_sala_leitura', 'in_parque_infantil', 'in_refeitorio', 'in_patio_coberto', 'in_patio_descoberto', 'in_area_verde', 'in_internet')

infra_schema = InfraSchema()
infras_schema = InfraSchema(many=True)

# Localizacao

class Localizacao(db.Model):
    __tablename__ = 'LOCALIZACAO'

    co_entidade = db.Column(db.Integer(), primary_key=True, unique=True)
    latitude = db.Column(db.Integer())
    longitude = db.Column(db.Integer())
    ds_endereco = db.Column(db.String(80))
    nu_endereco = db.Column(db.Integer())
    ds_complemento = db.Column(db.String(80))
    no_bairro = db.Column(db.String(80))
    co_cep = db.Column(db.Integer())

    def __init__(self, co_entidade, latitude, longitude, ds_endereco, nu_endereco, ds_complemento, no_bairro, co_cep):
        self.co_entidade = co_entidade
        self.latitude = latitude
        self.longitude = longitude
        self.ds_endereco = ds_endereco
        self.nu_endereco = nu_endereco
        self.ds_complemento = ds_complemento
        self.no_bairro = no_bairro
        self.co_cep = co_cep

class LocalizacaoSchema(ma.Schema):
    class Meta:
        model = Localizacao
        fields = ('co_entidade', 'co_entidade', 'latitude', 'longitude', 'ds_endereco', 'nu_endereco', 'ds_complemento', 'no_bairro', 'co_cep')

localizacao_schema = LocalizacaoSchema()
localizacoes_schema = LocalizacaoSchema(many=True)

# ------------------------ ROUTES ------------------------

# endpoint para exibir todos contatos
@app.route("/contatos", methods=["GET"])
def get_contatos():
    all_contatos = Contato.query.all()
    result = contatos_schema.dump(all_contatos)
    return jsonify(result)

# endpoint para exibir todas localizacoes
@app.route("/localizacao", methods=["GET"])
def get_localizacoes():
    all_localizacoes = Localizacao.query.all()
    result = localizacoes_schema.dump(all_localizacoes)
    return jsonify(result)

# endpoint para exibir todas localizacoes
@app.route("/infra", methods=["GET"])
def get_infras():
    all_infras = infra.query.all()
    result = infras_schema.dump(all_infras)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')