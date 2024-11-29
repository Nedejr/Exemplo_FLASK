from main import app
from flask import render_template


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html', nome_usuario=nome_usuario)