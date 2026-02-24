from ..extensions import db

class Produto(db.Model):
    __tablename__ = "produto"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50))
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, default=0)