

class Escola(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), unique=True)
    localizacao = db.Column(db.String(120), unique=False)
    tipo = db.Column(db.String(80), unique=False)
    nivel = db.Column(db.String(80), unique=False)
    outros_detalhes = db.Column(db.String(160), unique=False)

    def __init__(self, nome, localizacao, tipo, nivel, outros_detalhes):
        self.nome = nome
        self.localizacao = localizacao
        self.tipo = tipo
        self.nivel = nivel
        self.outros_detalhes = outros_detalhes


class EscolaSchema(ma.Schema):
    class Meta:
        fields = ('nome', 'localizacao', 'tipo', 'nivel', 'outros_detalhes')




# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')



class Contato(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    ddd = db.Column(db.Integer(), unique=False)
    numero = db.Column(db.Integer(), unique=False)
    email = db.Column(db.String(80), unique=False)

    def __init__(self, id, ddd, numero, email):
        self.id = id
        self.ddd = ddd
        self.numero = numero
        self.email = email


class ContatoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'ddd', 'numero', 'email')

