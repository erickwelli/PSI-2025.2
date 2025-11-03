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

@app.route('/recebedados', methods=['GET'])
def recebedados():
    nome = request.args['nome']
    telefone = request.args['telefone']
    return "{} - {}".format(nome, telefone)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    login = request.form['login']
    senha = request.form['senha']
    if login == 'admin' and senha =='12345':
        return 'Seja bem-vindo, Admin'
    else:
        return 'Você não tem permissão de acessar essa página'
    
@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
	return render_template('verificaridade.html', idade=idade)

@app.route('/usuario/<nome>')
def usuario(nome):
	return render_template('usuario.html', nome=nome)

@app.route('/produtos/<int:qtd>')
def produtos(qtd):
     return render_template('produtos.html', qtd=qtd)

@app.route('/compras')
def compras():
    itens = ["arroz", "feijão", "farinha", "macarrão", "açucar", "abacaxi", "goiaba"]
    return render_template('compras.html', itens=itens)

if __name__ == "__main__":
    app.run()