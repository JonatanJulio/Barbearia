from shared.models import db


class Servico(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), nullable=False, default='active')
    barbe_id = db.Column(db.Integer, db.ForeignKey('barbe.id'))

    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def __repr__(self):
        return f"<Servico {self.name}>"

