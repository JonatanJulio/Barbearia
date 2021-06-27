
from repositories.servicos_repository import ServicosRepository
from shared.models import db



class Barbe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')
    servicos = db.relationship('Servico', backref='barbe', lazy=True)

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __repr__(self) -> str:
        return f"<Barbe {self.name}>"

    


