from flask import Flask, render_template

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

@app.route('/gastos',defaults={'mes':'janeiro','gasto':0})
@app.route('/gastos/<mes>',defaults={'gasto':0})
@app.route('/gastos/<gasto>',defaults={'mes':'janeiro'})
@app.route('/gastos/<mes>/<gasto>')
def gastos(mes,gasto):
    return render_template('gastos.html',mes=mes,gasto=gasto)

@app.route('/dobro/<int:n>')
def dobro(n):
    resultado = n*2
    return render_template('/dobro.html',n=n,resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)