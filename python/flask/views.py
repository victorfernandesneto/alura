from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from run import app, db
from models import Alunos, Usuarios
from helpers import recupera_imagem, deleta_arquivo, FormularioAluno
import time


@app.route('/')
def index():
    return redirect(url_for('alunos'))


@app.route('/alunos')
def alunos():
    lista_de_alunos = Alunos.query.order_by('id')
    return render_template(
        'alunos.html',
        titulo='Alunos',
        lista_de_alunos=lista_de_alunos,
        session=session)


@app.route('/cadastro')
def cadastro():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('tela_de_login', proxima=url_for('cadastro')))
    form = FormularioAluno()
    return render_template('cadastro.html', titulo='Cadastro de alunos', form=form)


@app.route('/criar', methods=['POST', ])
def criar():
    form = FormularioAluno(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('/cadastro'))

    nome = form.nome.data()
    cpf = form.cpf.data()
    telefone = form.telefone.data()

    aluno = Alunos.query.filter_by(cpf=cpf).first()

    if aluno:
        flash('Aluno já cadastrado!')
        return redirect(url_for('alunos'))

    novo_aluno = Alunos(nome=nome, cpf=cpf, telefone=telefone)
    db.session.add(novo_aluno)
    db.session.commit()

    foto = request.files['foto']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    foto.save(f'{upload_path}/foto{novo_aluno.id}-{timestamp}.jpg')

    return redirect(url_for('alunos'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('tela_de_login', proxima=url_for('editar')))
    aluno = Alunos.query.filter_by(id=id).first()
    foto_aluno = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando aluno', aluno=aluno, foto_aluno=foto_aluno)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    id_aluno = request.form['id']

    aluno = Alunos.query.filter_by(id=id_aluno).first()
    aluno.nome = request.form['nome']
    aluno.cpf = request.form['cpf']
    aluno.telefone = request.form['telefone']

    db.session.add(aluno)
    db.session.commit()

    foto = request.files['foto']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    deleta_arquivo(aluno.id)
    foto.save(f'{upload_path}/foto{aluno.id}-{timestamp}.jpg')

    return redirect(url_for('alunos'))


@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('tela_de_login', proxima=url_for('deletar')))

    Alunos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')

    return redirect(url_for('alunos'))


@app.route('/login')
def tela_de_login():
    if 'usuario_logado' in session and session['usuario_logado'] is not None:
        return redirect(url_for('alunos'))
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar_usuario():
    usuario = Usuarios.query.filter_by(nome=request.form['usuario']).first()
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario
            flash(f'{usuario.nome} logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(url_for(proxima_pagina.replace('/', '')))
    flash('Credenciais incorretas.')
    return redirect(url_for('tela_de_login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('alunos'))

@app.route('/uploads/<nome_arquivo>')
def foto(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
