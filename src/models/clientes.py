"""Module Clientes.py

Refatorado para aplicar SRP: validação e persistência foram extraídas
para classes dedicadas (`ValidadorCliente`, `ClienteRepositorio`).
"""

import re
from typing import Any, Dict
from ast import literal_eval

# REG Para validação do Email
REG_EMAIL = "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"


class ValidadorCliente:
    """Responsável por validações de dados do cliente."""

    @staticmethod
    def validar_email(email: str) -> bool:
        """Valida o email do cliente."""
        return bool(re.match(REG_EMAIL, email))

    @staticmethod
    def validar_cnpj(cnpj: Any) -> bool:
        """Valida o CNPJ do cliente."""

        try:
            # Validação simples: deve ser inteiro positivo. Regras reais
            # de CNPJ podem ser adicionadas sem alterar a classe Cliente.
            return int(cnpj) > 0
        except Exception:
            return False


class ClienteRepositorio:
    """Responsável por persistir clientes (atualmente em arquivo)."""

    @staticmethod
    def salvar(cliente: Dict[str, Any], path: str = "clientes.txt") -> None:
        """Salva o cliente em um arquivo."""
        with open(path, "a", encoding="utf-8") as f:
            f.write(str(cliente) + "\n")

    @staticmethod
    def carregar(path: str = "clientes.txt") -> Dict[int, Dict[str, Any]]:
        """Carrega os clientes de um arquivo."""
        clientes = {}
        try:
            with open(path, "r", encoding="utf-8") as f:
                for linha in f:
                    cliente = literal_eval(linha.strip())
                    clientes[cliente["cnpj"]] = cliente
        except FileNotFoundError:
            pass
        return clientes


class Clientes:
    """
    Classe Cliente: Email, nome, CNPJ
    Mantém API compatível com a versão anterior, mas delega validação
    e persistência para classes separadas (SRP).
    """

    def __init__(self, email: str, nome: str, cnpj: int) -> None:
        self.nome = nome
        self.email = email
        self.cnpj = cnpj

    def cadastrar(self) -> bool:
        """Valida os dados e delega a persistência ao repositório."""
        if not ValidadorCliente.validar_email(self.email):
            return False

        if not ValidadorCliente.validar_cnpj(self.cnpj):
            return False

        cliente = {"nome": self.nome, "email": self.email, "cnpj": self.cnpj}
        ClienteRepositorio.salvar(cliente)

        return True

    def enviar_email(self) -> None:
        """Função para enviar o email para o usuário. Pode ser implementada futuramente."""
        print("enviando email de boas vindas para", self.email)
