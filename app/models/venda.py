from ..extensions import db
from datetime import datetime

class Venda(db.Model):
    __tablename__ = "venda"

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"), nullable=False)
    valor_total = db.Column(db.Float, default=0.0)

    itens = db.relationship("ItemVenda", backref="venda", lazy=True)