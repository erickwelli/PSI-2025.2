from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perfil', defaults = {'nome': 'Fulano'})

@app.route('/perfil/<nome>')
def perfil(nome):
    return render_template('perfil.html', nome = nome)

@app.route('/contato')
def contato():
    return render_template('contato.html', tel='(84) 914561249')

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('recebedados', methods=['GET'])
def recebedados():
    nome = request.args['nome']
    telefone = request.args['telefone']
    return "{} - {}".format(nome, telefone)

if __name__ == "__main__":
    app.run()