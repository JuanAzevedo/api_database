from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Evento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    data_evento = db.Column(db.String(10), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cidade': self.cidade,
            'data_evento': self.data_evento
        }
