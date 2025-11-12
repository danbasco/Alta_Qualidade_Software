import re

'''
Classe Cliente: Email, nome, CNPJ
'''

REG_EMAIL = "^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$"

class Clientes:

    def __init__(self, email: str, nome: str, cnpj: int) -> None:
        
        self.nome = nome
        self.email = email
        self.cnpj = cnpj


    def cadastrar(self) -> bool:

        if not re.match(REG_EMAIL, self.email):
            return False

        f = open("clientes.txt", "a", encoding="utf-8")

        cliente = {"nome": self.nome, "email": self.email, "cnpj": self.cnpj}
        f.write(str(cliente) + "\n")
        f.close()

        print("enviando email de boas vindas para", self.email)
        return True