from flask import render_template, request, redirect, session, flash, url_for
from run import app
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash


@app.route('/login')
def tela_de_login():
    if 'usuario_logado' in session and session['usuario_logado'] is not None:
        return redirect(url_for('alunos'))
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', titulo='Login', proxima=proxima, form=form)


@app.route('/autenticar', methods=['POST', ])
def autenticar_usuario():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nome=form.usuario.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
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
