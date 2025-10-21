"""
CP5 - Python: CRUD de Arquivos - Lista de compras com pré pagamento
Grupo: Arthur Albertini - RM 565459, Kauã Veloso Lima - RM561954"""

"""
CP5 – Python (dupla ou trio): CRUD de Arquivos
Lista de compras com pré pagamento - Versão Média

Autores: NOME1 - RM___, NOME2 - RM___

Arquivos utilizados:
- produtos.txt → lista de produtos e preços
- conta.txt → dados da conta (nome, nasc., agência, conta, saldo, senha)
- historico.txt → histórico das compras

"""

import os
from datetime import datetime

# Arquivos
ARQ_PRODUTOS = "produtos.txt"
ARQ_CONTA = "conta.txt"
ARQ_HIST = "historico.txt"

# -------- Funções de Arquivo -------- #
def inicializar_arquivos():
    for arq in [ARQ_PRODUTOS, ARQ_CONTA, ARQ_HIST]:
        if not os.path.exists(arq):
            with open(arq, "w", encoding="utf-8") as f:
                pass

# -------- Produtos -------- #
def adicionar_produto():
    nome = input("Nome do produto: ").strip()
    preco = input("Preço (use ponto como separador): ").strip()
    try:
        preco = float(preco)
    except ValueError:
        print("Preço inválido!")
        return
    with open(ARQ_PRODUTOS, "a", encoding="utf-8") as f:
        f.write(f"{nome};{preco}\n")
    print("Produto adicionado!")


def listar_produtos():
    if not os.path.getsize(ARQ_PRODUTOS):
        print("Nenhum produto cadastrado.")
        return []
    produtos = []
    total = 0
    print("\nLista de produtos:")
    with open(ARQ_PRODUTOS, "r", encoding="utf-8") as f:
        for linha in f:
            nome, preco = linha.strip().split(";")
            preco = float(preco)
            produtos.append((nome, preco))
            total += preco
    for i, (nome, preco) in enumerate(produtos, 1):
        print(f"{i}. {nome} - R$ {preco:.2f}")
    print(f"Total de itens: {len(produtos)} | Preço total: R$ {total:.2f}\n")
    return produtos

# -------- Conta -------- #
def criar_conta():
    nome = input("Nome completo: ").strip()
    nasc = input("Data de nascimento: ").strip()
    agencia = input("Agência: ").strip()
    conta = input("Conta: ").strip()
    saldo = "0.0"
    senha = input("Senha: ").strip()
    with open(ARQ_CONTA, "w", encoding="utf-8") as f:
        f.write(f"{nome};{nasc};{agencia};{conta};{saldo};{senha}\n")
    print("Conta criada com sucesso!\n")


def login():
    if not os.path.getsize(ARQ_CONTA):
        print("Nenhuma conta cadastrada.")
        return None
    agencia = input("Agência: ").strip()
    conta = input("Conta: ").strip()
    senha = input("Senha: ").strip()
    with open(ARQ_CONTA, "r", encoding="utf-8") as f:
        linha = f.readline().strip()
        nome, nasc, ag, co, saldo, se = linha.split(";")
        if ag == agencia and co == conta and se == senha:
            print(f"Bem-vindo(a), {nome}!\n")
            return {
                "nome": nome,
                "nasc": nasc,
                "ag": ag,
                "conta": co,
                "saldo": float(saldo),
                "senha": se
            }
    print("Login inválido.")
    return None


def salvar_conta(conta):
    with open(ARQ_CONTA, "w", encoding="utf-8") as f:
        f.write(f"{conta['nome']};{conta['nasc']};{conta['ag']};{conta['conta']};{conta['saldo']};{conta['senha']}\n")


def consultar_saldo(conta):
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")


def depositar(conta):
    try:
        valor = float(input("Valor do depósito: ").strip())
    except ValueError:
        print("Valor inválido!")
        return conta
    conta["saldo"] += valor
    salvar_conta(conta)
    print("Depósito realizado com sucesso!")
    return conta

# -------- Compra -------- #
def comprar(conta):
    produtos = listar_produtos()
    if not produtos:
        return conta
    total = sum(p[1] for p in produtos)
    print(f"Total da compra: R$ {total:.2f}")
    if conta["saldo"] < total:
        print("Saldo insuficiente!")
        return conta
    confirma = input("Confirmar compra? (s/n): ").lower()
    if confirma == "s":
        conta["saldo"] -= total
        salvar_conta(conta)
        with open(ARQ_HIST, "a", encoding="utf-8") as f:
            data = datetime.now().strftime("%d/%m/%Y %H:%M")
            f.write(f"{data};{total}\n")
        print("Compra realizada com sucesso!")
    else:
        print("Compra cancelada.")
    return conta

# -------- Histórico -------- #
def ver_historico():
    if not os.path.getsize(ARQ_HIST):
        print("Nenhuma compra registrada.")
        return
    print("\nHistórico de compras:")
    with open(ARQ_HIST, "r", encoding="utf-8") as f:
        for linha in f:
            data, valor = linha.strip().split(";")
            print(f"{data} - R$ {valor}")
    print()

# -------- Menu -------- #
def menu():
    inicializar_arquivos()
    conta_logada = None
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Criar conta")
        print("4. Login")
        print("5. Sair")
        if conta_logada:
            print("6. Consultar saldo")
            print("7. Depositar")
            print("8. Comprar (todos os produtos)")
            print("9. Ver histórico")
            print("10. Logout")
        opc = input("Opção: ").strip()
        if opc == "1":
            adicionar_produto()
        elif opc == "2":
            listar_produtos()
        elif opc == "3":
            criar_conta()
        elif opc == "4":
            conta_logada = login()
        elif opc == "5":
            print("Saindo...")
            break
        elif conta_logada and opc == "6":
            consultar_saldo(conta_logada)
        elif conta_logada and opc == "7":
            conta_logada = depositar(conta_logada)
        elif conta_logada and opc == "8":
            conta_logada = comprar(conta_logada)
        elif conta_logada and opc == "9":
            ver_historico()
        elif conta_logada and opc == "10":
            conta_logada = None
            print("Logout realizado.")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
