from flask import Flask, render_template
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

if __name__ == "__main__":
    app.run()