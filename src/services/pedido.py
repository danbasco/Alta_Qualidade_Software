"""
Module Pedido.py
"""

from models.calculadora import PrecoCalculadora


def processar_pedido(p):
    """Processar_pedido: processa o pedido e calcula o preço a partir de PrecoCalculadora"""

    prod = p.get("produto")
    qtd = p.get("qtd")
    cupom = p.get("cupom")

    if qtd == 0:
        print("qtd zero, retornando 0")
        return 0

    calculadora = PrecoCalculadora(prod, qtd)
    preco = calculadora.calcular_preco()

    if preco < 0:
        print("algo deu errado, preco negativo")
        preco = 0

    preco = calculadora.calcular_desconto(cupom, preco)

    if prod == "diesel":
        preco = round(preco, 0)

    elif prod == "gasolina":
        preco = round(preco, 2)

    else:
        preco = float(int(preco * 100) / 100.0)

    print("pedido ok:", p["cliente"], prod, qtd, "=>", preco)

    return preco
