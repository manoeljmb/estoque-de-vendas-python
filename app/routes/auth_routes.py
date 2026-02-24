from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from ..models.usuario import Usuario

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["POST"])
def login():
    data = request.json

    usuario = Usuario.query.filter_by(login=data["login"]).first()

    if usuario and check_password_hash(usuario.senha, data["senha"]):
        token = create_access_token(
            identity=usuario.login,
            additional_claims={"perfil": usuario.perfil}
        )
        return jsonify(access_token=token), 200

    return jsonify({"erro": "Credenciais inválidas"}), 401