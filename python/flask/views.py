from flask import render_template, request, redirect, session, flash, url_for
from academia import app, db
from models import Alunos, Usuarios


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
    return render_template('cadastro.html', titulo='Cadastro de alunos')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    telefone = request.form['telefone']

    aluno = Alunos.query.filter_by(cpf=cpf).first()

    if aluno:
        flash('Aluno já cadastrado!')
        return redirect(url_for('alunos'))

    novo_aluno = Alunos(nome=nome, cpf=cpf, telefone=telefone)
    db.session.add(novo_aluno)
    db.session.commit()

    return redirect(url_for('alunos'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('tela_de_login', proxima=url_for('editar')))
    aluno = Alunos.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editando aluno', aluno=aluno)


@app.route('/atualizar', methods=['POST', ])
def atualizar():
    id_aluno = request.form['id']

    aluno = Alunos.query.filter_by(id=id_aluno).first()
    aluno.nome = request.form['nome']
    aluno.cpf = request.form['cpf']
    aluno.telefone = request.form['telefone']

    db.session.add(aluno)
    db.session.commit()

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
