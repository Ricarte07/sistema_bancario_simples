# Sistema Bancário v2 em Python

Este projeto é uma simulação de um sistema bancário, focado na refatoração do código para utilizar funções, permitindo um sistema mais organizado e escalável. Esta é a segunda versão do projeto, evoluindo de um script simples para uma estrutura modular.

## Funcionalidades

O sistema oferece um menu com as seguintes operações:

* **[1] Depositar:** Permite ao usuário depositar valores positivos em sua conta.
* **[2] Sacar:** Permite ao usuário sacar valores, respeitando um limite por saque (R$ 500) e um limite diário de 3 saques.
* **[3] Extrato:** Mostra todas as transações realizadas e o saldo atual da conta.
* **[4] Nova Conta:** Cria uma nova conta corrente, vinculando-a a um usuário já existente.
* **[5] Listar Contas:** Exibe todas as contas correntes cadastradas no sistema.
* **[6] Novo Usuário:** Cadastra um novo usuário no sistema com nome, data de nascimento, CPF e endereço.
* **[0] Sair:** Encerra a execução do programa.

## Estrutura do Código

O código foi modularizado em funções para separar as responsabilidades:

- `main()`: Função principal que gerencia o loop do programa e o menu.
- `depositar()`, `sacar()`, `exibir_extrato()`: Funções que cuidam das operações bancárias.
- `criar_usuario()`, `criar_conta()`, `listar_contas()`: Funções para o gerenciamento de usuários e contas.
- `filtrar_usuario()`: Função utilitária para buscar um usuário pelo CPF.

