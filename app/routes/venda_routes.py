from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..services.venda_service import registrar_venda

venda_bp = Blueprint("venda", __name__)

@venda_bp.route("/", methods=["POST"])
@jwt_required()
def criar_venda():
    data = request.json

    try:
        venda = registrar_venda(
            cliente_id=data["cliente_id"],
            itens=data["itens"]
        )

        return jsonify({
            "mensagem": "Venda realizada",
            "venda_id": venda.id
        }), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 400