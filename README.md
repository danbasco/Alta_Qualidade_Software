# PetroBahia S.A.

A **PetroBahia S.A.** é uma empresa fictícia do setor de óleo e gás. Seu sistema interno calcula preços de combustíveis, valida clientes e gera relatórios. 
O código está **mal estruturado** e **difícil de manter**. O objetivo é **refatorar** aplicando **PEP8**, **Clean Code** e **princípios SOLID** (SRP e OCP).

## Objetivos
- Melhorar legibilidade e clareza do código
- Extrair funções e classes coesas
- Eliminar duplicações e efeitos colaterais
- Melhorar nomes e modularidade

## Estrutura
```
.
├── pytest.ini
├── requirements.txt
├── report.html
├── README.md
├── src/
│   ├── main.py
│   ├── models/
│   │   ├── calculadora.py
│   │   └── clientes.py
│   └── services/
│       └── pedido.py
└── tests/
    ├── __init__.py
    ├── test_calculadora.py
    ├── test_clientes.py
    ├── test_pedido.py
    ├── tests_calculadora.py
    └── tests_clientes.py
```

## Instruções
1. Leia o código legado.
2. Liste os problemas encontrados.
3. Refatore sem mudar o comportamento principal.
4. Documente suas **decisões de design** neste README.

---

## DECISÕES DE DESIGN

O código foi refatorado para aplicar os princípios **SRP (Princípio da Responsabilidade Única)** e **OCP (Princípio Aberto/Fechado)**. Abaixo estão as principais decisões e justificativas.

### 1. `models/clientes.py` - Aplicação do SRP

**Solução:** A classe foi dividida em três componentes, cada um com uma única responsabilidade:
- **`Clientes`**: Mantém apenas os dados do cliente. A API `cadastrar()` foi mantida por compatibilidade, mas agora delega as tarefas de validação e persistência.
- **`ValidadorCliente`**: Uma classe estática responsável por todas as validações relacionadas a clientes (e-mail, CNPJ, etc.). Isso centraliza as regras de negócio e permite sua reutilização.
- **`ClienteRepositorio`**: Classe estática dedicada a salvar os dados do cliente. Atualmente, salva em um arquivo de texto, mas pode ser facilmente modificada para usar um banco de dados sem impactar o resto do sistema.

**Benefício:** O código tornou-se mais coeso, modular e fácil de testar. A lógica de validação e persistência pode ser alterada de forma independente.

### 2. `models/calculadora.py` - Aplicação do OCP

**Solução:** Foi implementado o **padrão de projeto Strategy**.
- **`PrecoStrategy` (Interface)**: Uma classe base abstrata que define a interface para todas as estratégias de cálculo de preço.
- **Estratégias Concretas**: Para cada tipo de produto (`diesel`, `gasolina`, etc.), foi criada uma classe que herda de `PrecoStrategy` e implementa sua própria lógica de `calcular_preco` e `aplicar_desconto`.
- **Registry (`STRATEGY_REGISTRY`)**: Um dicionário que mapeia o nome de um produto à sua classe de estratégia. Isso permite que novas estratégias sejam "registradas" dinamicamente, sem alterar o código da calculadora.
- **`PrecoCalculadora` (Fachada)**: A classe foi mantida como uma fachada (`Facade`) para preservar a compatibilidade com o resto do sistema. Internamente, ela consulta o *registry* para obter a estratégia correta e delega o cálculo a ela.

**Benefício:** O sistema agora é **aberto para extensão, mas fechado para modificação**. Para adicionar um novo produto (ex: "querosene"), basta criar uma nova classe `QueroseneStrategy` e registrá-la. Nenhuma alteração é necessária em `PrecoCalculadora` ou `services/pedido.py`.

### 3. `services/pedido.py` - Redução de Acoplamento

**Solução:**
- O serviço continua usando `PrecoCalculadora`, mas como esta agora atua como uma fachada, o acoplamento é com uma abstração estável, não com detalhes de implementação.
- A lógica de arredondamento foi mantida no serviço por simplicidade, mas em uma evolução futura, poderia ser movida para dentro de cada estratégia de preço para aumentar a coesão.

**Benefício:** O serviço tornou-se mais limpo e focado em sua responsabilidade principal: orquestrar o processamento de um pedido.

