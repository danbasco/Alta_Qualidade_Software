"""Main Module"""

from models.clientes import Clientes
from services.pedido import processar_pedido

pedidos = [
    {"cliente": "TransLog", "produto": "diesel", "qtd": 1200, "cupom": "MEGA10"},
    {"cliente": "MoveMais", "produto": "gasolina", "qtd": 300, "cupom": None},
    {"cliente": "EcoFrota", "produto": "etanol", "qtd": 50, "cupom": "NOVO5"},
    {"cliente": "PetroPark", "produto": "lubrificante", "qtd": 12, "cupom": "LUB2"},
]

clientes = [
    Clientes(nome="Carlos", email="carlos@petrobahia.com", cnpj=12345),
    Clientes(nome="Ana Paula", email="ana@@petrobahia", cnpj=123),
]


def main():
    """Function main"""
    print("==== Início processamento PetroBahia ====")

    for c in clientes:
        ok = c.cadastrar()
        if ok:
            print(f"cliente ok: {c.nome}")
        else:
            print(f"cliente com problema: {c.nome}")

    valores = []

    for p in pedidos:
        v = processar_pedido(p)
        valores.append(v)
        print("pedido:", p, "-- valor final:", v)

    print("TOTAL =", sum(valores))
    print("==== Fim processamento PetroBahia ====")


if __name__ == "__main__":
    main()
