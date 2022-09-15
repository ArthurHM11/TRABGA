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
'oi'

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

cod1 = 0
cod2 = 0
cod3 = 0
cod4 = 0
cod5 = 0
cod6 = 0
cod7 = 0
cod8 = 0
cod9 = 0
print('inicializando sistema...')

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
def opcao_1():
  print('\nOpção escolhida: 1\n')
  print('O que será comprado?')
  print('# Código Produto Estoque Valor\n1 Calça 20 R$ 112,00\n2 Camisa 18 R$ 95,00\n3 Bermuda 23 R$ 49,90\n4 Saia 12 R$ 169,00\n5 Blusa 9 R$ 120,00\n6 Moletom 4 R$ 135,00\n7 Meia 17 R$ 12,99\n8 Tênis 8 R$ 183,00\n9 Bota 3 R$ 219,90\n')
def opcao_2():
  print('\nOpção escolhida: 2\n')
def opcao_3():
  print('\nOpção escolhida: 3\n')
def opcao_4():
  print('\nOpção escolhida: 3\n')
def opcao_5():
  print('\nOpção escolhida: 3\n')



  # Processamento do menu e chamada das funções
escolha = '0'
while(escolha != '9'):
  escolha = menu()
  if escolha == '1':
    opcao_1()
  elif escolha == '2':
    opcao_2()
  elif escolha == '3':
    opcao_3()
  elif escolha == '9':
    print('\nSaindo...\n')
  else:
    print('\nOpção desconhecida!\n')
  input('Pressione ENTER para continuar')
