"""Testes para o módulo Clientes usando pytest e unittest"""

import unittest
import pytest
import sys
import os
import tempfile

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.clientes import Clientes, ValidadorCliente, ClienteRepositorio


# ========== Testes com pytest ==========

class TestValidadorClientePytest:
    """Testes para ValidadorCliente usando pytest"""
    
    def test_email_valido(self):
        """Testa validação de email válido"""
        assert ValidadorCliente.validar_email("teste@email.com") is True
    
    def test_email_invalido_sem_arroba(self):
        """Testa validação de email sem @"""
        assert ValidadorCliente.validar_email("testeemail.com") is False
    
    def test_email_invalido_sem_dominio(self):
        """Testa validação de email sem domínio"""
        assert ValidadorCliente.validar_email("teste@") is False
    
    def test_cnpj_valido(self):
        """Testa validação de CNPJ válido"""
        assert ValidadorCliente.validar_cnpj(12345678901234) is True
    
    def test_cnpj_invalido_negativo(self):
        """Testa validação de CNPJ negativo"""
        assert ValidadorCliente.validar_cnpj(-123) is False
    
    def test_cnpj_invalido_string(self):
        """Testa validação de CNPJ como string inválida"""
        assert ValidadorCliente.validar_cnpj("abc") is False


class TestClienteRepositorioPytest:
    """Testes para ClienteRepositorio usando pytest"""
    
    def test_salvar_e_carregar_cliente(self):
        """Testa salvar e carregar cliente"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
        
        try:
            cliente = {"nome": "Teste", "email": "teste@email.com", "cnpj": 12345}
            ClienteRepositorio.salvar(cliente, temp_path)
            
            clientes = ClienteRepositorio.carregar(temp_path)
            assert 12345 in clientes
            assert clientes[12345]["nome"] == "Teste"
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    def test_carregar_arquivo_inexistente(self):
        """Testa carregar de arquivo inexistente"""
        clientes = ClienteRepositorio.carregar("arquivo_que_nao_existe.txt")
        assert clientes == {}


class TestClientesPytest:
    """Testes para classe Clientes usando pytest"""
    
    def test_cadastrar_cliente_valido(self):
        """Testa cadastro de cliente válido"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
        
        try:
            # Monkey patch para usar arquivo temporário
            original_salvar = ClienteRepositorio.salvar
            ClienteRepositorio.salvar = lambda c, path="clientes.txt": original_salvar(c, temp_path)
            
            cliente = Clientes("valido@email.com", "Cliente Teste", 12345)
            resultado = cliente.cadastrar()
            
            assert resultado is True
            
            ClienteRepositorio.salvar = original_salvar
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    def test_cadastrar_cliente_email_invalido(self):
        """Testa cadastro com email inválido"""
        cliente = Clientes("emailinvalido", "Cliente Teste", 12345)
        resultado = cliente.cadastrar()
        assert resultado is False
    
    def test_cadastrar_cliente_cnpj_invalido(self):
        """Testa cadastro com CNPJ inválido"""
        cliente = Clientes("valido@email.com", "Cliente Teste", -123)
        resultado = cliente.cadastrar()
        assert resultado is False


# ========== Testes com unittest ==========

class TestValidadorClienteUnittest(unittest.TestCase):
    """Testes para ValidadorCliente usando unittest"""
    
    def test_email_valido(self):
        """Testa validação de email válido"""
        self.assertTrue(ValidadorCliente.validar_email("teste@email.com"))
    
    def test_email_invalido(self):
        """Testa validação de email inválido"""
        self.assertFalse(ValidadorCliente.validar_email("emailinvalido"))
    
    def test_cnpj_valido(self):
        """Testa validação de CNPJ válido"""
        self.assertTrue(ValidadorCliente.validar_cnpj(12345678901234))
    
    def test_cnpj_invalido(self):
        """Testa validação de CNPJ inválido"""
        self.assertFalse(ValidadorCliente.validar_cnpj(-123))


class TestClienteRepositorioUnittest(unittest.TestCase):
    """Testes para ClienteRepositorio usando unittest"""
    
    def test_salvar_e_carregar_cliente(self):
        """Testa salvar e carregar cliente"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
        
        try:
            cliente = {"nome": "Teste", "email": "teste@email.com", "cnpj": 12345}
            ClienteRepositorio.salvar(cliente, temp_path)
            
            clientes = ClienteRepositorio.carregar(temp_path)
            self.assertIn(12345, clientes)
            self.assertEqual(clientes[12345]["nome"], "Teste")
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


class TestClientesUnittest(unittest.TestCase):
    """Testes para classe Clientes usando unittest"""
    
    def test_cadastrar_cliente_valido(self):
        """Testa cadastro de cliente válido"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            temp_path = f.name
        
        try:
            original_salvar = ClienteRepositorio.salvar
            ClienteRepositorio.salvar = lambda c, path="clientes.txt": original_salvar(c, temp_path)
            
            cliente = Clientes("valido@email.com", "Cliente Teste", 12345)
            resultado = cliente.cadastrar()
            
            self.assertTrue(resultado)
            
            ClienteRepositorio.salvar = original_salvar
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
    
    def test_cadastrar_cliente_email_invalido(self):
        """Testa cadastro com email inválido"""
        cliente = Clientes("emailinvalido", "Cliente Teste", 12345)
        self.assertFalse(cliente.cadastrar())


if __name__ == '__main__':
    unittest.main()
