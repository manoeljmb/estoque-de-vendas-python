from ..models.produto import Produto
from ..models.venda import Venda
from ..models.item_venda import ItemVenda
from ..extensions import db

def registrar_venda(cliente_id, itens):
    nova_venda = Venda(cliente_id=cliente_id)
    total_geral = 0

    for item in itens:
        produto = Produto.query.get(item["produto_id"])

        if not produto:
            raise Exception("Produto não encontrado")

        if produto.quantidade < item["quantidade"]:
            raise Exception(f"Estoque insuficiente para {produto.nome}")

        subtotal = produto.preco * item["quantidade"]
        total_geral += subtotal

        produto.quantidade -= item["quantidade"]

        item_venda = ItemVenda(
            produto_id=produto.id,
            quantidade=item["quantidade"],
            subtotal=subtotal
        )

        nova_venda.itens.append(item_venda)

    nova_venda.valor_total = total_geral
    db.session.add(nova_venda)
    db.session.commit()

    return nova_venda