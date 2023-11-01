from run import db
from dataclasses import dataclass

@dataclass
class Alunos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    telefone = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return '<Nome %r>' % self.nome

@dataclass
class Usuarios(db.Model):
    nome = db.Column(db.String(20), primary_key=True)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Usuario %r>' % self.nome