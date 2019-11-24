from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
import os

import json

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

database_name = 'TestDB2.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, database_name)
db = SQLAlchemy(app)
ma = Marshmallow(app)



# ------------------------ MODELS ------------------------

# Escola

class Escola(db.Model):
    __tablename__ = 'ESCOLA'

    co_entidade = db.Column(db.Integer(), primary_key=True)
    no_entidade = db.Column(db.String(80), unique=False)
    tp_dependencia = db.Column(db.Integer(), unique=False)
    tipo = db.Column(db.String(80), unique=False)
    tp_atividade_complementar = db.Column(db.Integer(), unique=False)
    atividade_complementar = db.Column(db.String(80), unique=False)
    in_alimentacao = db.Column(db.Integer, unique=False)
    alimentacao = db.Column(db.String(80), unique=False)
    creche = db.Column(db.String(80), unique=False)
    pre_escola = db.Column(db.String(80), unique=False)
    fundamental_anos_iniciais = db.Column(db.String(80), unique=False)
    fundamental_anos_finais = db.Column(db.String(80), unique=False)
    medio = db.Column(db.String(80), unique=False)

    def __init__(self, co_entidade, no_entidade,tipo,atividade_complementar,alimentacao,creche,pre_escola,fundamental_anos_iniciais,fundamental_anos_finais,medio):
        self.co_entidade = co_entidade
        self.no_entidade = no_entidade
        self.tipo = tipo
        self.atividade_complementar = atividade_complementar
        self.alimentacao = alimentacao
        self.creche = creche
        self.pre_escola = pre_escola
        self.fundamental_anos_iniciais = fundamental_anos_iniciais
        self.fundamental_anos_finais = fundamental_anos_finais
        self.medio = medio

class EscolaSchema(ma.Schema):
    class Meta:
        model = Escola
        fields = ('co_entidade', 'no_entidade', 'tp_dependencia', 'tipo', 'tp_atividade_complementar','atividade_complementar', 'in_alimentacao','alimentacao','creche','pre_escola','fundamental_anos_iniciais','fundamental_anos_finais','medio')

escola_schema = EscolaSchema()
escolas_schema = EscolaSchema(many=True)


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


# Avaliacao

class Avaliacao(db.Model):
    __tablename__ = 'Avaliacao'

    co_entidade = db.Column(db.Integer(), primary_key=True, unique=True)
    no_entidade = db.Column(db.String(80))
    tp_dependencia = db.Column(db.Integer())
    tp_atividade_complementar = db.Column(db.Integer())
    in_alimentacao = db.Column(db.Integer())
    ideb_anos_iniciais = db.Column(db.Float())
    ideb_anos_finais = db.Column(db.Float()) 

    def __init__(self, co_entidade, no_entidade, tp_dependencia, tp_atividade_complementar, in_alimentacao, ideb_anos_iniciais, ideb_anos_finais):
        self.co_entidade = co_entidade
        self.no_entidade = no_entidade
        self.tp_dependencia = tp_dependencia
        self.tp_atividade_complementar = in_dependencias_pne
        self.in_alimentacao = in_alimentacao
        self.ideb_anos_iniciais = ideb_anos_iniciais
        self.ideb_anos_finais = ideb_anos_finais

class AvaliacaoSchema(ma.Schema):
    class Meta:
        model = Avaliacao
        fields = ('co_entidade', 'no_entidade', 'tp_dependencia', 'tp_atividade_complementar', 'in_alimentacao', 'ideb_anos_iniciais', 'ideb_anos_finais')

avaliacao_schema = AvaliacaoSchema()
avaliacoes_schema = AvaliacaoSchema(many=True)


# Acessibilidade

class Acessibilidade(db.Model):
    __tablename__ = 'ACESSIBILIDADE'

    co_entidade = db.Column(db.Integer(), primary_key=True, unique=True)
    in_sala_atendimento_especial = db.Column(db.Integer())
    in_banheiro_pne = db.Column(db.Integer())
    in_dependencias_pne = db.Column(db.Integer())
    tp_aee = db.Column(db.Integer())
    in_especial_exclusiva = db.Column(db.Integer())

    def __init__(self, co_entidade, in_sala_atendimento_especial, in_banheiro_pne, in_dependencias_pne, tp_aee, in_especial_exclusiva):
        self.co_entidade = co_entidade
        self.in_sala_atendimento_especial = in_sala_atendimento_especial
        self.in_banheiro_pne = in_banheiro_pne
        self.in_dependencias_pne = in_dependencias_pne
        self.tp_aee = tp_aee
        self.in_especial_exclusiva = in_especial_exclusiva

class AcessibilidadeSchema(ma.Schema):
    class Meta:
        model = Acessibilidade
        fields = ('co_entidade', 'in_sala_atendimento_especial', 'in_banheiro_pne', 'in_dependencias_pne', 'tp_aee', 'in_especial_exclusiva')

acessibilidade_schema = AcessibilidadeSchema()
acessibilidades_schema = AcessibilidadeSchema(many=True)




# ------------------------ ROUTES ------------------------

# endpoint para exibir todas escolas
@app.route("/escolas/", methods=["GET"])
@cross_origin(supports_credentials=True)
@cross_origin(origin="172.22.238.220")
def get_escolas():
    all_escolas = Escola.query.all()
    result = escolas_schema.dump(all_escolas)
    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

# endpoint para exibir todas escolas
@app.route("/escola/bairro/<bairro>", methods=["GET"])
def get_escolas_por_bairro(bairro):
    all_escolas = Escola.query.join(Localizacao, Localizacao.co_entidade == Escola.co_entidade).filter(Localizacao.no_bairro == bairro).all()
    result = escolas_schema.dump(all_escolas)
    return jsonify(result)

# endpoint para exibir a escola com id == <id>
@app.route("/escola/id/<id>", methods=["GET"])
def get_escola_by_id(id):
    #escola, contato, acessibilidade, avaliacao, infra, localizacao = db.session.query(Escola, Contato, Acessibilidade, Avaliacao, Infra, Localizacao).filter(Escola.co_entidade == id).filter(Contato.co_entidade == id).first()
    escola = Escola.query.filter(Escola.co_entidade == id).first()
    escola = escola_schema.jsonify(escola).get_json()
    contato = Contato.query.filter(Contato.co_entidade == id).first()
    contato = contato_schema.jsonify(contato).get_json()
    acessibilidade = Acessibilidade.query.filter(Acessibilidade.co_entidade == id).first()
    acessibilidade = acessibilidade_schema.jsonify(acessibilidade).get_json()
    avaliacao = Avaliacao.query.filter(Avaliacao.co_entidade == id).first()
    avaliacao = avaliacao_schema.jsonify(avaliacao).get_json()
    infra = Infra.query.filter(Infra.co_entidade == id).first()
    infra = infra_schema.jsonify(infra).get_json()
    localizacao = Localizacao.query.filter(Localizacao.co_entidade == id).first()
    localizacao = localizacao_schema.jsonify(localizacao).get_json()

    escola.update(contato)
    escola.update(acessibilidade)
    escola.update(avaliacao)
    escola.update(infra)
    escola.update(localizacao)
    return escola

# # endpoint para exibir todas as escolas dados os filtros
@app.route('/filter', methods=["GET"])
def get_escola_by_filter():
    # exemplo:
    # http://0.0.0.0:5000/filter?alimentacao=false&atividade_complementar=false&acessibilidade=false&bairro=AZENHA
    
    query = Escola.query.join(Acessibilidade, Escola.co_entidade == Acessibilidade.co_entidade)
    alimentacao = request.args['alimentacao']
    atividade_complementar = request.args['atividade_complementar']
    acessibilidade = request.args['acessibilidade']
    bairro = request.args['bairro']

    if(alimentacao=='true'):
        query = query.filter(Escola.in_alimentacao == 1.0)
    if(atividade_complementar=='true'):
        query = query.filter(Escola.tp_atividade_complementar == 1.0)
    if(acessibilidade=='true'):
        query = query.filter((Acessibilidade.in_sala_atendimento_especial == 1.0) | (Acessibilidade.in_banheiro_pne == 1.0) | (Acessibilidade.in_dependencias_pne == 1.0) | (Acessibilidade.tp_aee == 1.0) | (Acessibilidade.in_especial_exclusiva == 1.0))
    if(bairro != None):
        query = query.join(Localizacao,Localizacao.co_entidade==Escola.co_entidade).filter(Localizacao.no_bairro==bairro)
    
    escolas = query.all()
    escolas_out = escolas_schema.dump(escolas)

    saida = []
    for escola in escolas_out:
        l = Localizacao.query.filter(Localizacao.co_entidade == escola['co_entidade']).first()
        l = localizacao_schema.dump(l)
        e = jsonify(escola).get_json()
        e.update(jsonify(l).get_json())
        saida.append(e)

    return json.dumps(saida)

# endpoint para exibir todas localizacoes
@app.route("/localizacao", methods=["GET"])
def get_localizacoes():
    all_localizacoes = Localizacao.query.all()
    result = localizacoes_schema.dump(all_localizacoes)
    return jsonify(result)

# endpoint para exibir a localizacao em determinado <end>
@app.route("/localizacao/<end>", methods=["GET"])
def get_localizacao(end):
    localizacao = Localizacao.query.filter(Localizacao.ds_endereco == end).first()
    return localizacao_schema.jsonify(localizacao)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
