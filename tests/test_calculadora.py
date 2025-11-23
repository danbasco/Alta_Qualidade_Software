"""Testes para o módulo Calculadora usando pytest e unittest"""

import unittest
import pytest
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.calculadora import (
    PrecoCalculadora,
    DieselStrategy,
    GasolinaStrategy,
    EtanolStrategy,
    LubrificanteStrategy,
    register_strategy,
    get_strategy,
    BASES
)


# ========== Testes com pytest ==========

class TestDieselStrategyPytest:
    """Testes para DieselStrategy usando pytest"""
    
    def test_calculo_diesel_quantidade_pequena(self):
        """Testa cálculo de diesel com quantidade pequena (sem desconto)"""
        strategy = DieselStrategy()
        preco = strategy.calcular_preco(100)
        assert preco == BASES["diesel"] * 100
    
    def test_calculo_diesel_quantidade_media(self):
        """Testa cálculo de diesel com quantidade média (5% desconto)"""
        strategy = DieselStrategy()
        preco = strategy.calcular_preco(600)
        assert preco == BASES["diesel"] * 600 * 0.95
    
    def test_calculo_diesel_quantidade_grande(self):
        """Testa cálculo de diesel com quantidade grande (10% desconto)"""
        strategy = DieselStrategy()
        preco = strategy.calcular_preco(1500)
        assert preco == BASES["diesel"] * 1500 * 0.9


class TestGasolinaStrategyPytest:
    """Testes para GasolinaStrategy usando pytest"""
    
    def test_calculo_gasolina_sem_desconto(self):
        """Testa cálculo de gasolina sem desconto"""
        strategy = GasolinaStrategy()
        preco = strategy.calcular_preco(100)
        assert preco == BASES["gasolina"] * 100
    
    def test_calculo_gasolina_com_desconto(self):
        """Testa cálculo de gasolina com desconto"""
        strategy = GasolinaStrategy()
        preco = strategy.calcular_preco(300)
        assert preco == (BASES["gasolina"] * 300) - 100


class TestEtanolStrategyPytest:
    """Testes para EtanolStrategy usando pytest"""
    
    def test_calculo_etanol_sem_desconto(self):
        """Testa cálculo de etanol sem desconto"""
        strategy = EtanolStrategy()
        preco = strategy.calcular_preco(50)
        assert preco == BASES["etanol"] * 50
    
    def test_calculo_etanol_com_desconto(self):
        """Testa cálculo de etanol com desconto"""
        strategy = EtanolStrategy()
        preco = strategy.calcular_preco(100)
        assert preco == BASES["etanol"] * 100 * 0.97


class TestLubrificanteStrategyPytest:
    """Testes para LubrificanteStrategy usando pytest"""
    
    def test_calculo_lubrificante(self):
        """Testa cálculo de lubrificante"""
        strategy = LubrificanteStrategy()
        preco = strategy.calcular_preco(10)
        assert preco == BASES["lubrificante"] * 10
    
    def test_desconto_lubrificante_cupom_lub2(self):
        """Testa desconto específico LUB2 para lubrificante"""
        strategy = LubrificanteStrategy()
        preco = strategy.aplicar_desconto(100, "LUB2")
        assert preco == 98


class TestPrecoCalculadoraPytest:
    """Testes para PrecoCalculadora usando pytest"""
    
    def test_calculadora_diesel(self):
        """Testa calculadora com diesel"""
        calc = PrecoCalculadora("diesel", 100)
        preco = calc.calcular_preco()
        assert preco == BASES["diesel"] * 100
    
    def test_calculadora_gasolina(self):
        """Testa calculadora com gasolina"""
        calc = PrecoCalculadora("gasolina", 100)
        preco = calc.calcular_preco()
        assert preco == BASES["gasolina"] * 100
    
    def test_calculadora_tipo_invalido(self):
        """Testa calculadora com tipo inválido"""
        calc = PrecoCalculadora("invalido", 100)
        preco = calc.calcular_preco()
        assert preco == 0.0
    
    def test_desconto_mega10(self):
        """Testa desconto MEGA10"""
        calc = PrecoCalculadora("diesel", 100)
        preco = calc.calcular_preco()
        preco_com_desconto = calc.calcular_desconto("MEGA10", preco)
        assert preco_com_desconto == preco * 0.9
    
    def test_desconto_novo5(self):
        """Testa desconto NOVO5"""
        calc = PrecoCalculadora("etanol", 50)
        preco = calc.calcular_preco()
        preco_com_desconto = calc.calcular_desconto("NOVO5", preco)
        assert preco_com_desconto == preco * 0.95


# ========== Testes com unittest ==========

class TestDieselStrategyUnittest(unittest.TestCase):
    """Testes para DieselStrategy usando unittest"""
    
    def test_calculo_diesel_quantidade_pequena(self):
        """Testa cálculo de diesel com quantidade pequena"""
        strategy = DieselStrategy()
        preco = strategy.calcular_preco(100)
        self.assertEqual(preco, BASES["diesel"] * 100)
    
    def test_calculo_diesel_quantidade_media(self):
        """Testa cálculo de diesel com quantidade média"""
        strategy = DieselStrategy()
        preco = strategy.calcular_preco(600)
        self.assertEqual(preco, BASES["diesel"] * 600 * 0.95)
    
    def test_calculo_diesel_quantidade_grande(self):
        """Testa cálculo de diesel com quantidade grande"""
        strategy = DieselStrategy()
        preco = strategy.calcular_preco(1500)
        self.assertEqual(preco, BASES["diesel"] * 1500 * 0.9)


class TestGasolinaStrategyUnittest(unittest.TestCase):
    """Testes para GasolinaStrategy usando unittest"""
    
    def test_calculo_gasolina_sem_desconto(self):
        """Testa cálculo de gasolina sem desconto"""
        strategy = GasolinaStrategy()
        preco = strategy.calcular_preco(100)
        self.assertEqual(preco, BASES["gasolina"] * 100)
    
    def test_calculo_gasolina_com_desconto(self):
        """Testa cálculo de gasolina com desconto"""
        strategy = GasolinaStrategy()
        preco = strategy.calcular_preco(300)
        self.assertEqual(preco, (BASES["gasolina"] * 300) - 100)


class TestEtanolStrategyUnittest(unittest.TestCase):
    """Testes para EtanolStrategy usando unittest"""
    
    def test_calculo_etanol_sem_desconto(self):
        """Testa cálculo de etanol sem desconto"""
        strategy = EtanolStrategy()
        preco = strategy.calcular_preco(50)
        self.assertEqual(preco, BASES["etanol"] * 50)
    
    def test_calculo_etanol_com_desconto(self):
        """Testa cálculo de etanol com desconto"""
        strategy = EtanolStrategy()
        preco = strategy.calcular_preco(100)
        self.assertEqual(preco, BASES["etanol"] * 100 * 0.97)


class TestPrecoCalculadoraUnittest(unittest.TestCase):
    """Testes para PrecoCalculadora usando unittest"""
    
    def test_calculadora_diesel(self):
        """Testa calculadora com diesel"""
        calc = PrecoCalculadora("diesel", 100)
        preco = calc.calcular_preco()
        self.assertEqual(preco, BASES["diesel"] * 100)
    
    def test_calculadora_tipo_invalido(self):
        """Testa calculadora com tipo inválido"""
        calc = PrecoCalculadora("invalido", 100)
        preco = calc.calcular_preco()
        self.assertEqual(preco, 0.0)
    
    def test_desconto_mega10(self):
        """Testa desconto MEGA10"""
        calc = PrecoCalculadora("diesel", 100)
        preco = calc.calcular_preco()
        preco_com_desconto = calc.calcular_desconto("MEGA10", preco)
        self.assertAlmostEqual(preco_com_desconto, preco * 0.9, places=2)


if __name__ == '__main__':
    unittest.main()
