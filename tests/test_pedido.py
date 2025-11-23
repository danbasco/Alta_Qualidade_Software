"""Testes para o módulo Pedido usando pytest e unittest"""

import unittest
import pytest
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.services.pedido import processar_pedido


# ========== Testes com pytest ==========

class TestProcessarPedidoPytest:
    """Testes para processar_pedido usando pytest"""
    
    def test_pedido_diesel_quantidade_pequena(self):
        """Testa pedido de diesel com quantidade pequena"""
        pedido = {
            "cliente": "Cliente A",
            "produto": "diesel",
            "qtd": 100,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        assert preco == round(3.99 * 100, 0)
    
    def test_pedido_gasolina_quantidade_pequena(self):
        """Testa pedido de gasolina com quantidade pequena"""
        pedido = {
            "cliente": "Cliente B",
            "produto": "gasolina",
            "qtd": 100,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        assert preco == round(5.19 * 100, 2)
    
    def test_pedido_etanol_com_desconto(self):
        """Testa pedido de etanol com desconto por quantidade"""
        pedido = {
            "cliente": "Cliente C",
            "produto": "etanol",
            "qtd": 100,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        expected = float(int((3.59 * 100 * 0.97) * 100) / 100.0)
        assert preco == expected
    
    def test_pedido_lubrificante(self):
        """Testa pedido de lubrificante"""
        pedido = {
            "cliente": "Cliente D",
            "produto": "lubrificante",
            "qtd": 10,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        expected = float(int((25.0 * 10) * 100) / 100.0)
        assert preco == expected
    
    def test_pedido_com_cupom_mega10(self):
        """Testa pedido com cupom MEGA10"""
        pedido = {
            "cliente": "Cliente E",
            "produto": "diesel",
            "qtd": 100,
            "cupom": "MEGA10"
        }
        preco = processar_pedido(pedido)
        preco_base = 3.99 * 100
        preco_esperado = round(preco_base * 0.9, 0)
        assert preco == preco_esperado
    
    def test_pedido_com_cupom_novo5(self):
        """Testa pedido com cupom NOVO5"""
        pedido = {
            "cliente": "Cliente F",
            "produto": "gasolina",
            "qtd": 100,
            "cupom": "NOVO5"
        }
        preco = processar_pedido(pedido)
        preco_base = 5.19 * 100
        preco_esperado = round(preco_base * 0.95, 2)
        assert preco == preco_esperado
    
    def test_pedido_quantidade_zero(self):
        """Testa pedido com quantidade zero"""
        pedido = {
            "cliente": "Cliente G",
            "produto": "diesel",
            "qtd": 0,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        assert preco == 0
    
    def test_pedido_diesel_quantidade_grande(self):
        """Testa pedido de diesel com quantidade grande (desconto 10%)"""
        pedido = {
            "cliente": "Cliente H",
            "produto": "diesel",
            "qtd": 1500,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        preco_esperado = round(3.99 * 1500 * 0.9, 0)
        assert preco == preco_esperado
    
    def test_pedido_gasolina_quantidade_grande(self):
        """Testa pedido de gasolina com quantidade grande (desconto 100)"""
        pedido = {
            "cliente": "Cliente I",
            "produto": "gasolina",
            "qtd": 300,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        preco_esperado = round((5.19 * 300) - 100, 2)
        assert preco == preco_esperado


# ========== Testes com unittest ==========

class TestProcessarPedidoUnittest(unittest.TestCase):
    """Testes para processar_pedido usando unittest"""
    
    def test_pedido_diesel_quantidade_pequena(self):
        """Testa pedido de diesel com quantidade pequena"""
        pedido = {
            "cliente": "Cliente A",
            "produto": "diesel",
            "qtd": 100,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        self.assertEqual(preco, round(3.99 * 100, 0))
    
    def test_pedido_gasolina_quantidade_pequena(self):
        """Testa pedido de gasolina com quantidade pequena"""
        pedido = {
            "cliente": "Cliente B",
            "produto": "gasolina",
            "qtd": 100,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        self.assertEqual(preco, round(5.19 * 100, 2))
    
    def test_pedido_quantidade_zero(self):
        """Testa pedido com quantidade zero"""
        pedido = {
            "cliente": "Cliente G",
            "produto": "diesel",
            "qtd": 0,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        self.assertEqual(preco, 0)
    
    def test_pedido_com_cupom_mega10(self):
        """Testa pedido com cupom MEGA10"""
        pedido = {
            "cliente": "Cliente E",
            "produto": "diesel",
            "qtd": 100,
            "cupom": "MEGA10"
        }
        preco = processar_pedido(pedido)
        preco_base = 3.99 * 100
        preco_esperado = round(preco_base * 0.9, 0)
        self.assertEqual(preco, preco_esperado)
    
    def test_pedido_lubrificante(self):
        """Testa pedido de lubrificante"""
        pedido = {
            "cliente": "Cliente D",
            "produto": "lubrificante",
            "qtd": 10,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        expected = float(int((25.0 * 10) * 100) / 100.0)
        self.assertEqual(preco, expected)
    
    def test_pedido_diesel_quantidade_grande(self):
        """Testa pedido de diesel com quantidade grande"""
        pedido = {
            "cliente": "Cliente H",
            "produto": "diesel",
            "qtd": 1500,
            "cupom": None
        }
        preco = processar_pedido(pedido)
        preco_esperado = round(3.99 * 1500 * 0.9, 0)
        self.assertEqual(preco, preco_esperado)


if __name__ == '__main__':
    unittest.main()
