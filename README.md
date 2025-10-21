# CP5-Python

CP5 - Lista de Compras com Pré-Pagamento

Descrição do Projeto

Este projeto Python implementa um sistema de lista de compras com funcionalidades de pré-pagamento, utilizando operações CRUD (Create, Read, Update, Delete) em arquivos de texto para armazenar os dados. O sistema permite gerenciar produtos, contas de usuário e registrar o histórico de compras.

Funcionalidades

O sistema oferece as seguintes opções através de um menu interativo:

1.
Adicionar Produto: Permite cadastrar novos produtos com nome e preço.

2.
Listar Produtos: Exibe todos os produtos cadastrados com seus respectivos preços e o total geral.

3.
Criar Conta: Permite que um novo usuário crie uma conta, fornecendo nome completo, data de nascimento, agência, conta, saldo inicial (0.0) e senha.

4.
Login: Permite que um usuário existente faça login com agência, conta e senha.

5.
Consultar Saldo: (Disponível após login) Exibe o saldo atual da conta logada.

6.
Depositar: (Disponível após login) Permite adicionar fundos à conta do usuário.

7.
Comprar (todos os produtos): (Disponível após login) Realiza a compra de todos os produtos listados, debitando o valor total do saldo da conta, se houver saldo suficiente.

8.
Ver Histórico: (Disponível após login) Exibe o histórico de todas as compras realizadas.

9.
Logout: Encerra a sessão do usuário logado.

10.
Sair: Encerra o programa.

Arquivos Utilizados

O projeto utiliza os seguintes arquivos para persistência de dados:

•
produtos.txt: Armazena a lista de produtos disponíveis e seus preços.

•
conta.txt: Armazena os dados da conta do usuário (nome, data de nascimento, agência, conta, saldo e senha).

•
historico.txt: Registra o histórico de todas as compras realizadas, com data, hora e valor.

Como Executar

1.
Pré-requisitos: Certifique-se de ter o Python 3 instalado em seu sistema.

2.
Clonar o repositório (ou baixar os arquivos):

3.
Executar o programa:

Autores

•
Kauã Veloso Lima - RM561954
Arthur Albertini - RM 565459



