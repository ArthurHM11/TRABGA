# Menu:
# O programa deverá conter um menu com as seguintes funcionalidades:
# 1. Registrar venda:  Inicia   uma   venda,   solicitando   o   nome   do   cliente   e   depois,   em   uma
# estrutura de repetição, pede para o usuário informar  o código  do  produto  e a quantidade
# desejada.   Caso   não   exista   o   código   do   produto   ou   não   tenha   quantidade   suficiente   em
# estoque,   deve   exibir   uma   mensagem   e   não   registrar   a   compra   do   item.   Do   contrário,   o
# sistema calcula e exibe o valor total do item, perguntando se quer confirmar a compra. O
# usuário pode confirmar ou cancelar o item. Se confirmar, deve dar baixa no estoque conforme
# quantidade comprada. Se o usuário digitar zero como código do produto, significa o fim da
# compra. Nesse instante, o sistema mostra o valor total dos itens comprados e retorna para o
# menu principal.
# 2. Repor estoque: Pede para o usuário informar um código de produto e uma quantidade. Caso
# o   produto   não   exista,   exibir   uma   mensagem.   Caso   exista,   deve   adicionar   a   quantidade
# informada do produto no estoque.
# 3. Mostrar  estoque:  Mostra   uma   tabela   com   os   produtos   em   estoque,   suas   quantidades,
# valores unitários e totais.
# 4. Mostrar compras: Mostra uma tabela com todos os produtos comprados, suas quantidades,
# valores unitários e totais por produto e o valor total das compras.
# 5. Maior compra: Mostra o nome do cliente, o valor total da compra e uma tabela com os itens
# comprados, exibindo quantidade comprada de cada produto e valor total por item.
# 6. Sair: Encerra o programa.


# Código Descrição Estoque Valor
# 1 Calça 20 R$ 112,00
# 2 Camisa 18 R$ 95,00
# 3 Bermuda 23 R$ 49,90
# 4 Saia 12 R$ 169,00
# 5 Blusa 9 R$ 120,00
# 6 Moletom 4 R$ 135,00
# 7 Meia 17 R$ 12,99
# 8 Tênis 8 R$ 183,00
# 9 Bota 3 R$ 219,90


import os

valorvenda = 0

# cod1 = ('Calça')
# cod2 = ('Camisa')
# cod3 = ('Bermuda')
# cod4 = ('Saia')
# cod5 = ('Blusa')
# cod6 = ('Moletom')
# cod7 = ('Meia')
# cod8 = ('Tênis')
# cod9 = ('Bota')

cod1p = 112.00
cod2p = 95.00
cod3p = 49.00
cod4p = 169.00
cod5p = 120.00
cod6p = 135.00
cod7p = 12.99
cod8p = 183.00
cod9p = 219.00

# global cod1
# global cod2
# global cod3
# global cod4
# global cod5
# global cod6
# global cod7
# global cod8
# global cod9

# global cod1p
# global cod2p
# global cod3p
# global cod4p
# global cod5p
# global cod6p
# global cod7p
# global cod8p
# global cod9p

est1 = 20
est2 = 18
est3 = 23
est4 = 12
est5 = 9
est6 = 4
est7 = 17
est8 = 8
est9 = 3

# global est1
# global est2
# global est3
# global est4
# global est5
# global est6
# global est7
# global est8
# global est9

print('inicializando sistema...')
nome = input('Boa noite.\nPor favor, insira seu nome: ')

def menu():
  os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux
  print('\n..:: Sistema de Compras ::..\n')
  print('1 - Registrar Venda')
  print('2 - Repor estoque')
  print('3 - Mostrar estoque')
  print('4 - Mostrar compras')
  print('5 - Maior compra')
  print('9 - Sair\n')
  item = input('Escolha uma opção: ')
  return item

# Uma função para cada item do menu
def opcao_1(est1,est2,est3,est4,est5,est6,est7,est8,est9):
  print('\nOpção escolhida: 1\n')
  nomec = input('Nome do Cliente: ')
  print('O que será comprado?')
  print('Código Produto Estoque Valor\n1 Calça 20 R$ 112,00\n2 Camisa 18 R$ 95,00\n3 Bermuda 23 R$ 49,90\n4 Saia 12 R$ 169,00\n5 Blusa 9 R$ 120,00\n6 Moletom 4 R$ 135,00\n7 Meia 17 R$ 12,99\n8 Tênis 8 R$ 183,00\n9 Bota 3 R$ 219,90\n')
  codv1 = 0
  codv2 = 0
  codv3 = 0
  codv4 = 0
  codv5 = 0
  codv6 = 0
  codv7 = 0
  codv8 = 0
  codv9 = 0
  vvenda = 0
  codp = input('Insira o código do produto: ')
  while(codp != '10'):
    if codp == '1':
      vvenda += cod1p
      codv1 += 1
      est1 -= 1
    elif codp == '2':
      vvenda += cod2p
      codv2 += 1
      est2 -= 1
    elif codp == '3':
      vvenda += cod3p
      codv3 += 1
      est3 -= 1
    elif codp == '4':
      vvenda += cod4p
      codv4 += 1
      est4 -= 1
    elif codp == '5':
      vvenda += cod5p
      codv5 += 1
      est5 -= 1
    elif codp == '6':
      vvenda += cod6p
      codv6 += 1
      est6 -= 1
    elif codp == '7':
      vvenda += cod7p
      codv7 += 1
      est7 -= 1
    elif codp == '8':
      vvenda += cod8p
      codv8 += 1
      est8 -= 1
    elif codp == '9':
      vvenda += cod9p
      codv9 += 1
      est9 -= 1
    elif codp == '10':
      print('\nSaindo...\n')
    else:
      print('\nOpção desconhecida!\n')
  compratotal = print('Total da venda:\nCliente: {}\nValor Total R${:.2f}'.format(nomec,vvenda))
  return compratotal


def opcao_2():
  print('\nOpção escolhida: 2\n')
def opcao_3():
  print('\nOpção escolhida: 3\n')
def opcao_4():
  print('\nOpção escolhida: 4\n')
def opcao_5():
  print('\nOpção escolhida: 5\n')



  # Processamento do menu e chamada das funções
escolha = '0'
while(escolha != '9'):
  escolha = menu()
  if escolha == '1':
    opcao_1(est1,est2,est3,est4,est5,est6,est7,est8,est9)
  elif escolha == '2':
    opcao_2()
  elif escolha == '3':
    opcao_3()
  elif escolha == '3':
    opcao_4()
  elif escolha == '3':
    opcao_5()
  elif escolha == '9':
    print('\nSaindo...\n')
  else:
    print('\nOpção desconhecida!\n')
  input('Pressione ENTER para continuar')
