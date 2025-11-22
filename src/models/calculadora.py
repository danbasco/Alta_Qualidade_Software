"""Calculadora Module
Refatorado para atender OCP: cada tipo de produto é uma estratégia de preço
e pode ser estendida sem modificar código existente.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Type, Optional

BASES = {
    "diesel": 3.99,
    "gasolina": 5.19,
    "etanol": 3.59,
    "lubrificante": 25.0,
}


class PrecoStrategy(ABC):
    """Interface para estratégias de cálculo de preço."""

    @abstractmethod
    def calcular_preco(self, quantidade: int) -> float:
        """Calcula o preço com base na quantidade."""

    def aplicar_desconto(self, preco: float, cupom: Optional[str]) -> float:
        """Descontos globais aplicáveis a vários produtos.

        Estratégias específicas podem sobrescrever para regras próprias.
        """
        if not cupom:
            return preco

        if cupom == "MEGA10":
            return preco - (preco * 0.10)

        if cupom == "NOVO5":
            return preco - (preco * 0.05)

        return preco


class DieselStrategy(PrecoStrategy):
    """Estratégia de preço para Diesel."""

    def calcular_preco(self, quantidade: int) -> float:
        """Calcula o preço do diesel com base na quantidade."""
        if quantidade > 1000:
            return BASES["diesel"] * quantidade * 0.9
        if quantidade > 500:
            return BASES["diesel"] * quantidade * 0.95
        return BASES["diesel"] * quantidade


class GasolinaStrategy(PrecoStrategy):
    """Estratégia de preço para Gasolina."""

    def calcular_preco(self, quantidade: int) -> float:
        """Calcula o preço da gasolina com base na quantidade."""
        if quantidade > 200:
            return (BASES["gasolina"] * quantidade) - 100
        return BASES["gasolina"] * quantidade


class EtanolStrategy(PrecoStrategy):
    """Estratégia de preço para Etanol."""

    def calcular_preco(self, quantidade: int) -> float:
        """Calcula o preço do etanol com base na quantidade."""
        preco = BASES["etanol"] * quantidade
        if quantidade > 80:
            preco = preco * 0.97
        return preco


class LubrificanteStrategy(PrecoStrategy):
    """Estratégia de preço para Lubrificante."""

    def calcular_preco(self, quantidade: int) -> float:
        """Calcula o preço do lubrificante com base na quantidade."""
        return BASES["lubrificante"] * quantidade

    def aplicar_desconto(self, preco: float, cupom: Optional[str]) -> float:
        """Desconto específico para lubrificantes."""
        if cupom == "LUB2":
            return preco - 2
        return super().aplicar_desconto(preco, cupom)


# Registry para permitir extensão sem alterar código interno
STRATEGY_REGISTRY: Dict[str, Type[PrecoStrategy]] = {}


def register_strategy(nome: str, cls: Type[PrecoStrategy]) -> None:
    """Registra uma nova estratégia de preço."""
    STRATEGY_REGISTRY[nome] = cls


def get_strategy(tipo: str) -> Optional[PrecoStrategy]:
    """Obtém a estratégia de preço registrada para um tipo de produto."""
    cls = STRATEGY_REGISTRY.get(tipo)
    if cls:
        return cls()
    return None


# Registrar estratégias padrão
register_strategy("diesel", DieselStrategy)
register_strategy("gasolina", GasolinaStrategy)
register_strategy("etanol", EtanolStrategy)
register_strategy("lubrificante", LubrificanteStrategy)


class PrecoCalculadora:
    """Fachada que usa uma PrecoStrategy para cálculos.

    Mantém compatibilidade com a API anterior (`calcular_preco`,
    `calcular_desconto`) enquanto permite extensão via registro de
    novas estratégias (OCP).
    """

    def __init__(self, tipo: str, quantidade: int):
        self.tipo = tipo
        self.quantidade = quantidade
        self._strategy = get_strategy(tipo)

    def calcular_preco(self) -> float:
        """Calcula o preço usando a estratégia selecionada."""
        if not self._strategy:
            return 0.0
        return self._strategy.calcular_preco(self.quantidade)

    def calcular_desconto(self, cupom: Optional[str], preco: float) -> float:
        """Calcula o desconto usando a estratégia selecionada."""
        if not self._strategy:
            return preco
        return self._strategy.aplicar_desconto(preco, cupom)
