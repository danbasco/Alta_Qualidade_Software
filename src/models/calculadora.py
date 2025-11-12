BASES = {

    "diesel": 3.99,
    "gasolina": 5.19,
    "etanol": 3.59,
    "lubrificante": 25.0,
}

class PrecoCalculadora:

    def __init__(self, tipo: str, quantidade: int):
        self.tipo = tipo
        self.quantidade = quantidade

    def calcular_preco(self) -> float:

        qtd = self.quantidade;

        match(self.tipo):

            case "diesel":

                if qtd > 1000:
                    return (BASES["diesel"] * qtd) * 0.9
                
                if qtd > 500:
                    return (BASES["diesel"] * qtd) * 0.95

                return BASES["diesel"] * qtd

            case "gasolina":

                if qtd > 200:
                    return (BASES["gasolina"] * qtd) - 100

                return BASES["gasolina"] * qtd


            case "etanol":

                preco = BASES["etanol"] * qtd
                if qtd > 80:
                        preco = preco * 0.97
                return preco
            
            case "lubrificante":

                preco = 0
                
                for i in range(qtd):
                    preco += BASES["lubrificante"]

                return preco
            case _:
                return 0

    def calcular_desconto(self, cupom: str, preco: float) -> float:
        
        novo_preco = preco

        if cupom == "MEGA10":
            novo_preco = preco - (preco * 0.1)
        
        if cupom == "NOVO5":
            novo_preco = preco - (preco * 0.05)
            
        if cupom == "LUB2" and self.tipo == "lubrificante":
            novo_preco = preco - 2

        return novo_preco

