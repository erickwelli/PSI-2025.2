from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "PSI é a melhor matéria do mundo!"

@app.route('/contato')
def contato():
    return 'erick.w@escolar.ifrn.edu.br'

if __name__ == "__main__":
    app.run()