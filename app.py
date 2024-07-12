from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Evento
import os

app = Flask(__name__)
db_path = os.path.join(os.getcwd(), 'instance', 'database.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# Endpoint para obter a lista de eventos
@app.route('/eventos', methods=['GET'])
def get_eventos():
    eventos = Evento.query.all()
    return jsonify([evento.serialize() for evento in eventos]), 200

# Endpoint para obter um evento específico pelo ID
@app.route('/evento/<int:id>', methods=['GET'])
def get_evento(id):
    evento = Evento.query.get(id)
    if not evento:
        return jsonify({"message": "Evento não encontrado"}), 404
    return jsonify(evento.serialize()), 200

# Endpoint para criar um novo evento
@app.route('/eventos', methods=['POST'])
def criar_evento():
    data = request.get_json()
    evento = Evento(
        nome=data['nome'],
        cidade=data['cidade'],
        data_evento=data['data_evento']
    )
    db.session.add(evento)
    db.session.commit()
    return jsonify(evento.serialize()), 201

# Endpoint para atualizar um evento existente
@app.route('/eventos/<int:id>', methods=['PUT'])
def atualizar_evento(id):
    data = request.get_json()
    evento = Evento.query.get(id)
    if not evento:
        return jsonify({"message": "Evento não encontrado"}), 404

    evento.nome = data['nome']
    evento.cidade = data['cidade']
    evento.data_evento = data['data_evento']
    db.session.commit()
    return jsonify(evento.serialize()), 200

# Endpoint para deletar um evento
@app.route('/eventos/<int:id>', methods=['DELETE'])
def deletar_evento(id):
    evento = Evento.query.get(id)
    if not evento:
        return jsonify({"message": "Evento não encontrado"}), 404

    db.session.delete(evento)
    db.session.commit()
    return jsonify({"message": "Evento removido com sucesso"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
