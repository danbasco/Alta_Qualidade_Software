"""Module Clientes.py"""

import re

# REG Para validação do Email
REG_EMAIL = "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"


class Clientes:
    """
    Classe Cliente: Email, nome, CNPJ
    """

    def __init__(self, email: str, nome: str, cnpj: int) -> None:

        self.nome = nome
        self.email = email
        self.cnpj = cnpj

    def cadastrar(self) -> bool:
        """
        Função para validar o email e cadastrar no banco de dados (txt)
        """

        if not re.match(REG_EMAIL, self.email):
            return False

        with open("clientes.txt", "a", encoding="utf-8") as f:

            cliente = {"nome": self.nome, "email": self.email, "cnpj": self.cnpj}
            f.write(str(cliente) + "\n")

            f.close()

        return True

    def enviar_email(self) -> None:
        """ Função para enviar o email para o usuário. Pode ser implementada futuramente.
        """
        print("enviando email de boas vindas para", self.email)
