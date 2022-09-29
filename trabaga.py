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


vvenda = 0

code1=0
code2=0
code3=0
code4=0
code5=0
code6=0
code7=0
code8=0
code9=0

codv1 = 0
codv2 = 0
codv3 = 0
codv4 = 0
codv5 = 0
codv6 = 0
codv7 = 0
codv8 = 0
codv9 = 0


cod1p = 112.00
cod2p = 95.00
cod3p = 49.00
cod4p = 169.00
cod5p = 120.00
cod6p = 135.00
cod7p = 12.99
cod8p = 183.00
cod9p = 219.00


est1 = 20
est2 = 18
est3 = 23
est4 = 12
est5 = 9
est6 = 4
est7 = 17
est8 = 8
est9 = 3

maiorcomprat = str('')
maiorcompra = int(0)

vtotal = 0

print('Inicializando sistema...')
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
def opcao_1():
  global cod1p
  global cod2p
  global cod3p
  global cod4p
  global cod5p
  global cod6p
  global cod7p
  global cod8p
  global cod9p
  global est1
  global est2
  global est3
  global est4
  global est5
  global est6
  global est7
  global est8
  global est9
  global codv1 
  global codv2 
  global codv3 
  global codv4 
  global codv5 
  global codv6 
  global codv7 
  global codv8 
  global codv9 
  global maiorcompra
  global maiorcomprat
  global vvenda
  global vtotal
  vvenda = 0
  print('\nOpção escolhida: 1\n')
  nomec = input('insira o nome do cliente: ')
  print('O que será comprado?')
  print('Código Produto Estoque Valor\n1 - Calça {} R$ 112,00\n2 - Camisa {} R$ 95,00\n3 - Bermuda {} R$ 49,90\n4 - Saia {} R$ 169,00\n5 - Blusa {} R$ 120,00\n6 - Moletom {} R$ 135,00\n7 - Meia {} R$ 12,99\n8 - Tênis {} R$ 183,00\n9 - Bota {} R$ 219,90\n10 - Terminar compra.'.format(est1,est2,est3,est4,est5,est6,est7,est8,est9))
  codp = '0'
  while(codp != '10'):
    codp = input('Insira o código do produto: ')
    if codp == '1':
      if est1 > 0:
        vvenda += cod1p
        codv1 += 1
        est1 -= 1
        print('Uma Calça de R$112,00 foi comprada.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '2':
      if est2 > 0:
        vvenda += cod2p
        codv2 += 1
        est2 -= 1
        print('Uma Camisa de R$95,00 foi comprada.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '3':
      if est3 > 0:
        vvenda += cod3p
        codv3 += 1
        est3 -= 1
        print('Uma Bermuda de R$49,90 foi comprada.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '4':
      if est4 > 0:
        vvenda += cod4p
        codv4 += 1
        est4 -= 1
        print('Uma Saia de R$169,00 foi comprada.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '5':
      if est5 > 0:
        vvenda += cod5p
        codv5 += 1
        est5 -= 1
        print('Uma Blusa de R$120,00 foi comprada.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '6':
      if est6 > 0:
        vvenda += cod6p
        codv6 += 1
        est6 -= 1
        print('Um Moletom de R$135,00 foi comprado.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '7':
      if est7 > 0:
        vvenda += cod7p
        codv7 += 1
        est7 -= 1
        print('Uma Meia de R$12,99 foi comprada.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '8':
      if est8 > 0:
        vvenda += cod8p
        codv8 += 1
        est8 -= 1
        print('Um Tenis de R$183,00 foi comprado.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '9':
      if est9 > 0:
        vvenda += cod9p
        codv9 += 1
        est9 -= 1
        print('Uma Bota de R$219,00 foi comprada.')
      else:
        print('Não há produtos em estoque o suficiente.')
    elif codp == '10':
      print('\nFinalizando Compra...\n')
    else:
      print('\nOpção desconhecida!\n')
  compratotal = str('Total da venda:\nCliente: {}\nValor Total R${:.2f}'.format(nomec,vvenda))
  print(compratotal)
  if maiorcompra < int(vvenda):
    maiorcompra = vvenda
    maiorcomprat = compratotal
  vtotal += vvenda

  print('Calças em Estoque: {}'.format(est1))
  print('Camisa em Estoque: {}'.format(est2))
  print('Bermudas em Estoque: {}'.format(est3))
  print('Saias em Estoque: {}'.format(est4))
  print('Blusas em Estoque: {}'.format(est5))
  print('Moletons em Estoque: {}'.format(est6))
  print('Meias em Estoque: {}'.format(est7))
  print('Tenis em Estoque: {}'.format(est8))
  print('Botas em Estoque: {}'.format(est9))
  return compratotal


def opcao_2():
  global est1
  global est2
  global est3
  global est4
  global est5
  global est6
  global est7
  global est8
  global est9
  global code1
  global code2
  global code3
  global code4
  global code5
  global code6
  global code7
  global code8
  global code9
  print('\nOpção escolhida: 2\n')
  print('\nO que será reposto?\n')
  print('Código Produto Estoque Valor\n1 - Calça {} R$ 112,00\n2 - Camisa {} R$ 95,00\n3 - Bermuda {} R$ 49,90\n4 - Saia {} R$ 169,00\n5 - Blusa {} R$ 120,00\n6 - Moletom {} R$ 135,00\n7 - Meia {} R$ 12,99\n8 - Tênis {} R$ 183,00\n9 - Bota {} R$ 219,90\n10 - Terminar compra.'.format(est1,est2,est3,est4,est5,est6,est7,est8,est9))
  codr='0'
  while(codr!='10'):
    codr= input('\nInsira o código de produto :\n')
    if codr=='1':
      n1=int(input('Informe a quantidade a ser reposta: '))
      code1+=n1
      print('{} calças foram repostas.'.format(n1))
      est1+=n1
    elif(codr=='2'):
      n2=int(input('Informe a quantidade a ser reposta: '))
      code2+=n2
      print('{} camisas foram repostas.'.format(n2))
      est2+=n2
    elif(codr=='3'):
      n3=int(input('Informe a quantidade a ser reposta:'))
      code3+=n3
      print('{} bermudas foram repostas.'.format(n3))
      est3+=n3
    elif(codr=='4'):
      n4=int(input('Informe a quantidade a ser reposta:'))
      code4+=n4
      print('{} saias foram repostas.'.format(n4))
      est4+=n4
    elif(codr=='5'):
      n5=int(input('Informe a quantidade a ser reposta:'))
      code5+=n5
      print('{} blusas foram repostas.'.format(n5))
      est5+=n5
    elif(codr=='6'):
      n6=int(input('Informe a quantia a ser reposta:'))
      code6+=n6
      print('{} moletons foram repostos.'.format(n6))
      est6+=n6
    elif(codr=='7'):
      n7=int(input('Informe a quantia a ser reposta:'))
      code7+=n7
      print('{} meias foram repostas.'.format(n7))
      est7+=n7
    elif(codr=='8'):
      n8=int(input('Informe a quantidade a ser reposta:'))
      code8+=n8
      print('{} tênis foram repostos.'.format(n8))
      est8+=n8
    elif(codr=='9'):
      n9=int(input('Informe a quantia a ser reposta:'))
      code9+n9
      print('{} botas foram repostas.'.format(n9))
      est9+=n9
    elif(codr=='10'):
      print('Finalizando estoque...')  
    else:
      print('O código de produto não existe.')
  estoquetotal=print('O estoque foi resposto com sucesso.')
  return estoquetotal
    





def opcao_3():
  global est1
  global est2
  global est3
  global est4
  global est5
  global est6
  global est7
  global est9
  print('\nOpção escolhida: 3\n')
  print('\nCódigo   Produto   Estoque   Valor unitário   Valor total\n')
  print('\n1 -      Calça       {}       R$ 112,00          R${:.2f}   \n'.format(est1, float(est1*112)))
  print('\n2 -      Camisa      {}       R$ 95,00           R${:.2f}   \n'.format(est2, float(est2*95))) 
  print('\n3 -      Bermuda     {}       R$49,90            R${:.2f}   \n'.format(est3, float(est3*49.90)))
  print('\n4 -      Saia        {}       R$169,00           R${:.2f}   \n'.format(est4, float(est4*169)))
  print('\n5 -      Blusa       {}       R$129,00           R${:.2f}   \n'.format(est5, float(est5*129)))
  print('\n6 -      Moletom     {}       R$135,00           R${:.2f}   \n'.format(est6, float(est6*135)))
  print('\n7 -      Meia        {}       R$12,99            R${:.2f}   \n'.format(est7, float(est7*12.99)))
  print('\n8 -      Tênis       {}       R$183,00           R${:.2f}   \n'.format(est8, float(est8*183)))
  print('\n9 -      Bota        {}       R$219,90           R${:.2f}   \n'.format(est9, float(est9*219.90)))
  obrigado=print('Obrigado!')
  return obrigado
  



def opcao_4():
  global cod1p
  global cod2p
  global cod3p
  global cod4p
  global cod5p
  global cod6p
  global cod7p
  global cod8p
  global cod9p
  global est1
  global est2
  global est3
  global est4
  global est5
  global est6
  global est7
  global est8
  global est9
  global vvenda
  global codv1 
  global codv2 
  global codv3 
  global codv4 
  global codv5 
  global codv6 
  global codv7 
  global codv8 
  global codv9 
  global vtotal
  print('\nOpção escolhida: 4\n')
  print('\nItens comprados:\n')
  if vtotal != 0:
    comp1=int(codv1)
    print('\n{} calças foram compradas.'.format(comp1))
    print('Valor unitário R$112,00')
    print('Valor total de calças compradas: R${}'.format(float(112*comp1)))
    comp2=int(codv2)
    print('\n{} camisas foram compradas.'.format(comp2))
    print('Valor unitário R$95,00')
    print('Valor total de camisas compradas: R${}'.format(float(95*comp2)))
    comp3=int(codv3)
    print('\n{} bermudas foram compradas.'.format(comp3))
    print('Valor unitário R$49.90')
    print('Valor total de bermudas compradas: R${}'.format(float(49.90*comp3)))
    comp4=int(codv4)
    print('\n{} saias foram compradas.'.format(comp4))
    print('Valor unitário R$169,00')
    print('Valor total de saias compradas: R${}'.format(float(169*comp4)))
    comp5=int(codv5)
    print('\n{} blusas foram compradas.'.format(comp5))
    print('Valor unitário R$129,00')
    print('Valor total de blusas compradas: R${}'.format(float(129*comp5)))
    comp6=int(codv6)
    print('\n{} moletons foram comprados.'.format(comp6))
    print('Valor unitário R$135,00')
    print('Valor total de moletons compradas: R${}'.format(float(135*comp6)))
    comp7=int(codv7)
    print('\n{} meias foram compradas.'.format(comp7))
    print('Valor unitário R$12.99')
    print('Valor total de meias compradas: R${}'.format(float(12.99*comp7)))
    comp8=int(codv8)
    print('\n{} tênis foram comprados.'.format(comp8))
    print('Valor unitário R$183,00')
    print('Valor total de tênis compradas: R${}'.format(float(183*comp8)))
    comp9=int(codv9)
    print('\n{} botas foram compradas.'.format(comp9))
    print('Valor unitário R$219.90')
    print('Valor total de botas compradas: R${}'.format(float(219.90*comp9)))
    print('\nValor total comprado: R${}\n '.format(vtotal))
  else:
    print('Nenhuma compra foi realizada.')
    obrigado=print('Obrigado!')
    return obrigado
  

  
  
def opcao_5():
  print('\nOpção escolhida: 5\n')
  if maiorcompra != 0:
    print(maiorcomprat)
  else:
    print('Nenhuma compra foi realizada.')
    print('Obrigado!')




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
  elif escolha == '4':
    opcao_4()
  elif escolha == '5':
    opcao_5()
  elif escolha == '9':
    print('\nSaindo...\n')
  else:
    print('\nOpção desconhecida!\n')
  input('Pressione ENTER para continuar')
