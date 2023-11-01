import os
from run import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


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
        'Nome do Aluno',
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