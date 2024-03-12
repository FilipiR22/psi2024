from flask import Flask, render_template
from defs import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compras')
def compras():
    return render_template('compras.html', novoitem='cuzscuz',item2='melancia')

@app.route('/mercados')
def mercados():
    return render_template('mercados.html')


# tratamento de exceções

@app.route('/gastos',defaults={'mes':'janeiro','gasto':0})
@app.route('/gastos/<mes>',defaults={'gasto':0})
@app.route('/gastos/<int:gasto>',defaults={'mes':'janeiro'})
@app.route('/gastos/<mes>/<int:gasto>')
def gastos(mes,gasto):
    return render_template('gastos.html',mes=mes,gasto=gasto)

#Definindo um tipo específico de dado que a rota irá aceitar

@app.route('/dobro/<int:n>')
def dobro(n):
    resultado = n*2
    return render_template('/dobro.html',n=n,resultado=resultado)

@app.route('/imagem-dinamica/<name>')
def img(name):
    return render_template('/imagem-dinamica.html',image_name=name)


if __name__ == '__main__':
    app.run(debug=True)