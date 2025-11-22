"""Calculadora Module
Calcula os preços do produto baseado no tipo e quantidade.
"""

BASES = {
    "diesel": 3.99,
    "gasolina": 5.19,
    "etanol": 3.59,
    "lubrificante": 25.0,
}


class PrecoCalculadora:
    """Classe PrecoCalculadora
    Instancia-se uma versao da classe para retornar um objeto com os valores de cálculo
    """

    def __init__(self, tipo: str, quantidade: int):
        self.tipo = tipo
        self.quantidade = quantidade

    def calcular_preco(self) -> float:
        """Funçao calcular preço:
        Calcula o preço a partir do tipo e quantidade
        """

        qtd = self.quantidade
        val = 0.0

        match (self.tipo):

            case "diesel":

                if qtd > 1000:
                    val = (BASES["diesel"] * qtd) * 0.9
                if qtd > 500:
                    val = (BASES["diesel"] * qtd) * 0.95
                else:
                    val = BASES["diesel"] * qtd

            case "gasolina":

                if qtd > 200:
                    val = (BASES["gasolina"] * qtd) - 100
                else:
                    val = BASES["gasolina"] * qtd

            case "etanol":

                val = BASES["etanol"] * qtd
                if qtd > 80:
                    val = val * 0.97

            case "lubrificante":

                val = BASES["lubrificante"] * qtd

            case _:
                return 0

        return val

    def calcular_desconto(self, cupom: str, preco: float) -> float:
        """Calcula o desconto a partir do cupom"""

        novo_preco = preco

        if cupom == "MEGA10":
            novo_preco = preco - (preco * 0.1)

        if cupom == "NOVO5":
            novo_preco = preco - (preco * 0.05)

        if cupom == "LUB2" and self.tipo == "lubrificante":
            novo_preco = preco - 2

        return novo_preco
