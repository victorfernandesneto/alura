import os
from run import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from validate_docbr import CPF
from models import Alunos
import re


class FormularioAluno(FlaskForm):
    nome = StringField(
        'Nome do Aluno',
        [
            validators.DataRequired(),
            validators.Length(min=1, max=50)
        ]
    )
    cpf = StringField(
        'CPF',
        [
            validators.DataRequired(),
            validators.Length(min=11, max=11)
        ]
    )
    telefone = StringField(
        'Telefone',
        [
            validators.DataRequired(),
            validators.Length(min=10, max=11)
        ]
    )
    salvar = SubmitField('Salvar')


def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'foto{id}' in nome_arquivo:
            return nome_arquivo

    return 'foto_exemplo.jpg'

def deleta_arquivo(id):
    foto = recupera_imagem(id)
    if foto != 'foto_exemplo.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], foto))

class Telefone:
    def formata_telefone(self, numero):
        padrao_telefone = '([0-9]{2})?([0-9]{4,5})([0-9]{4})'
        mascarado = re.match(padrao_telefone, numero)
        if len(mascarado.group()) >= 10:
            return '({}){}-{}'.format(
                mascarado.group(1), mascarado.group(2), mascarado.group(3)
            )
        else:
            return '{}-{}'.format(
                mascarado.group(2), mascarado.group(3)
            )


def query_alunos():
    cpf = CPF()
    lista_de_alunos = Alunos.query.order_by('id')
    return lista_de_alunos