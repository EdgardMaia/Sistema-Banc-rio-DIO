import time
import os
import random
from datetime import datetime

qntd_deposito = [(random.randint(0, 1000), 'Depósito Inicial', datetime.now())]
limite_saque = 3

def menu_principal():
  opcoes_validas = [1, 2, 3, 4]
  while True:
    print(30 * "=")
    print("Conta Bancaria".center(30))
    print(30 * "=")

    print('''
[1] Depositar 
[2] Sacar
[3] Extrato
[4] Sair''')

    try:
      opcao_menu = int(input("\nEscolha uma opção: "))
      if opcao_menu not in opcoes_validas:
        limpar_tela()
        print("Opção Inválida! Tente novamente.")
        time.sleep(2)
        limpar_tela()
        continue
      if opcao_menu == 1:
        deposito()
      if opcao_menu == 2:
        saque()
      if opcao_menu == 3:
        extrato()
      if opcao_menu == 4:
        limpar_tela()
        print("Encerrando o serviço...")
        time.sleep(3)
        limpar_tela()
        print("Obrigado :D")
        time.sleep(1)
        break

    except ValueError:
      limpar_tela()
      print("Caractere invalido! Tente novamente.")
      time.sleep(2)
      limpar_tela()

def deposito():
  limpar_tela()
  while True:
    print(30 * "=")
    print("Depósito".center(30))
    print(30 * "=")

    try:
      print(f"Saldo: R${qntd_deposito[-1][0]}")
      valor_deposito = float(input("\nDigite o valor a ser depositado: "))
      resultado = qntd_deposito[-1][0] + valor_deposito
      qntd_deposito.append((resultado, 'Depósito', datetime.now()))
      limpar_tela()
      print(f"Depósito de R${valor_deposito} realizado com sucesso!")
      time.sleep(2)
      limpar_tela()
      break

    except ValueError:
      limpar_tela()
      print("Valor inválido! Por favor, digite um número válido.")
      time.sleep(2)
      limpar_tela()

def saque():
  limpar_tela()
  saques_realizados = 0
  while saques_realizados < limite_saque:
    print(30 * "=")
    print("Saque".center(30))
    print(30 * "=")

    try:
      print(f'''
Saldo:R$ {qntd_deposito[-1][0]}
Limite diário de saque disponível: {limite_saque - saques_realizados}''')
      valor_saque = float(
          input("\nDigite a quantidade que você deseja sacar: "))
      if valor_saque > qntd_deposito[-1][0]:
        limpar_tela()
        print("Saldo insuficiente!")
        time.sleep(2)
        limpar_tela()
        continue
      limpar_tela()
      print(f"Saque no valor de R${valor_saque} realizado com sucesso.")
      time.sleep(2)
      limpar_tela()
      saques_realizados += 1
      qntd_deposito.append(
          (qntd_deposito[-1][0] - valor_saque, 'Saque', datetime.now()))

      opcoes_validas = (1, 2)
      print('''
Realizar um novo saque

[1] Sim
[2] Não ''')
      opcao_menu = int(input("Escolha uma opção: "))
      if opcao_menu not in opcoes_validas:
        limpar_tela()
        print("Opção invalida tente novamente.")
        time.sleep(2)
        limpar_tela()
        continue

      if opcao_menu == 1:
        if saques_realizados >= limite_saque:
          limpar_tela()
          print("Limite diário de saques atingido!")
          time.sleep(2)
          limpar_tela()
          break
        continue

      if opcao_menu == 2:
        limpar_tela()
        print("Retornando...")
        time.sleep(2)
        limpar_tela()
        break

    except ValueError:
      limpar_tela()
      print("Valor inválido! Por favor, digite um número válido.")
      time.sleep(2)
      limpar_tela()
      continue

def extrato():
  print(30 * "=")
  print("Extrato".center(30))
  print(30 * "=")

  for transacoes in qntd_deposito:
    print(f'''
Data: {transacoes[2].strftime('%Y-%m-%d %H:%M:%S')} - {transacoes[1]}: R${transacoes[0]}''')

def limpar_tela():
  if os.name == 'posix':
    os.system('clear')
  elif os.name == 'nt':
    os.system('cls')

menu_principal()
