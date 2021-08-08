# -*- coding: utf-8 -*-
from flask import Flask, render_template
import datetime
from config import bd
from controller.usuario import usuario_blueprint

TEMPLATES = './view'
STATIC = './static'

app = Flask(__name__, static_url_path='', template_folder=TEMPLATES, static_folder=STATIC)
app.register_blueprint(usuario_blueprint)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./dados.db'
bd.init_app(app)

with app.app_context():
    bd.create_all()

@app.route('/')
def helloWorld():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('index2.html')

@app.route('/home')
def home():
    data = datetime.datetime.now()
    usuarios = ['Karla', 'Fernanda', 'Sarah', 'Failesmen', 'Junior']
    mostrarUsuarios = True
    return render_template('home.html', dataAtual=data, usuarios=usuarios, mostrarUsuarios=mostrarUsuarios)

# DESCOMENTAR A LINHA ABAIXO PARA RODAR LOCALMENTE NA PORTA 5000
#app.run(host='0.0.0.0', port=5000)
