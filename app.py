from types import ClassMethodDescriptorType

from flask import Flask, abort, session, flash, render_template, request, redirect, url_for, \
    make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate


from shared.models import db
from models.barbe import Barbe
from models.servico import Servico

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/barbearia"
db.init_app(app)
migrate = Migrate(app, db)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/') # http://localhost:5000
def index():
    # redireciona para o login se não estiver logado
    if 'username' not in session:
        return redirect(url_for('login'))
    
    barbes = Barbe.query.all()
    
    response = make_response(
        render_template(    
            'index.html',
            title = 'Barbearia',
            barbes = barbes
        )
    )
    # response.set_cookie('language', 'pt-BR')

    return response

@app.route('/set_language/<language>')
def set_language(language):
    response = make_response(redirect(url_for('index')))
    response.set_cookie('language', language)
    
    return response

@app.route('/barbes/<int:barbe_id>', methods=['GET', 'POST'])
def barbes(barbe_id):
    language = request.cookies.get('language')

    barbe = Barbe.query.get_or_404(barbe_id)
    
    if request.method == 'POST':
        barbe.name = request.form.get('name')
        barbe.status = request.form.get('status')
        db.session.add(barbe)
        db.session.commit()

    return render_template('barbe.html', barbe=barbe, language=language)

@app.route('/barbes', methods=['POST'])
def create_barbe():
    name = request.form.get('name')
    status = request.form.get('status')

    barbe = Barbe(name=name, status=status)

    db.session.add(barbe)
    db.session.commit()

    return redirect(url_for('barbes',barbe_id=barbe.id))

@app.route('/barbes/<int:barbe_id>/delete', methods=['POST'])
def delete_barbe(barbe_id):
    barbe = Barbe.query.get_or_404(barbe_id)
    db.session.delete(barbe)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/valor_barba')
def valor_barba():
    return render_template('valor_barba.html')

@app.route('/sobre')
def sobre():
    return render_template('barbelist.html')

@app.route('/corte_barba')
def corte_barba():
    return render_template('corte_barba.html')

@app.route('/valor_corte')
def valor_corte():
    return render_template('valor_corte.html')

@app.route('/meia_barba')
def meia_barba():
    return render_template('meia_barba.html')

@app.route('/infantil')
def infantil():
    return render_template('infantil.html')

#http://localhost:5000/contato/julio
@app.route('/contato/<nome>')
def contato(nome):
    return f"Nome do contato {nome}!"

#### LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'Jonatan' and password == '123':
            session['username'] = username
            flash('Usuário autenticado com sucesso.', 'info')
            return redirect(url_for('index'))
        else:
            # abort(403)
            flash('Nome de usuário e/ou senha incorreto(s)', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/api/barbes')
def api_barbes():
    barbes = Barbe.query.all()

    barbe_list = []
    for barbe in barbes:
        barbe_list.append(
            {
                "id": barbe.id,
                "name": barbe.name,
                "status": barbe.status

            }
        )

    return jsonify(barbe_list)

     
    
