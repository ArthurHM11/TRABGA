# Trabaga GB

# Entrega e apresentação:  Os trabalhos  deverão ser entregues até as  19h30  e  apresentados
# pelos grupos ao professor na aula do dia 17/11/2022. O tempo máximo para apresentação por
# grupo será de até 15 minutos. A ordem de apresentação será definida no dia da apresentação. Os
# grupos   devem   ser   formados   por  até 4  integrantes.  Importante:  postagens   após   o   horário
# limite terão desconto de 2 pontos na nota.
# Sistema para Gerenciamento de Logística
# O trabalho do Grau  B  consiste em desenvolver  em Python  um sistema  simplificado de logística
# para   uma   transportadora,   analisando   as   distâncias   percorridas   pelos   caminhões   e   os   gastos
# destas viagens. As distâncias entre as cidades devem ser carregadas em uma matriz a partir do
# arquivo anexo. A matriz deverá ser utilizada como base de dados para consulta. O programa deve
# ser todo estruturado com funções e menus.
# Menu:
# O programa deverá conter um menu com as seguintes funcionalidades:

# 1. Custo por km rodado: Solicitar que o usuário informe o custo por km rodado, em reais. O
# programa deverá garantir que o valor seja numérico e maior que zero, e memorizá-lo para uso
# futuro. Não deve permitir acessar os itens 2, 3 e 4 sem essa informação;

# 2. Consultar trecho: Solicitar ao usuário que digite o nome de uma cidade “origem” e outra
# “destino”. Caso algum nome não exista no cadastro, ou “origem” for igual a “destino”, deve
# mostrar uma mensagem informativa e solicitar as cidades novamente. Tendo duas cidades
# válidas, o programa deverá calcular e mostrar na tela a distância rodoviária entre elas e o
# custo   total   do   trecho.   Também   deve   salvar   essas   informações   em   um   arquivo   de   “log”,
# mantendo o histórico das consultas;

# 3. Melhor rota: Solicitar que o usuário digite o nome de três cidades separadas por vírgulas.
# Caso alguma cidade não exista no cadastro ou tenham sido informadas cidades duplicadas,
# deve mostrar uma mensagem e retornar  para o menu principal. Do contrário, o programa
# deve   avaliar  uma  rota   que   parte  da   primeira  cidade   informada   e  passa   pelas   demais   em
# qualquer   ordem,   no   menor   percurso   possível.   Na  sequência,   o   programa   deverá   exibir   os
# nomes   das   cidades   e a  distância  entre  elas  para  cada   trecho  da  rota,   e  a distância   total
# percorrida;

# 4. Rota completa: Solicitar que o usuário digite o nome de no mínimo três cidades válidas, uma
# de   cada   vez,   até   que   seja   digitada   a   palavra   “fim”.   Caso   não   tenham   sido   informadas   3
# cidades válidas, mostrar uma mensagem, recusar o comando “fim”, e continuar solicitando os
# nomes. Caso todas as cidades existam e sejam no mínimo 3, o programa deve avaliar a rota
# que parte  da primeira cidade informada e passa pelas demais, na mesma ordem em que
# foram digitadas pelo usuário. Em seguida, o programa deverá exibir:
# •Para cada trecho, os nomes das cidades “de” e “para”, e a distância entre elas;
# •A distância total percorrida na rota;
# •O custo total da viagem, considerando o custo por km informado no item 1;
# •A quantidade total de litros de combustível consumidos ao final da viagem, supondo
# que o veículo consome 2,57 litros a cada km rodado;
# •O número de dias para finalizar a viagem, supondo que são percorridos em média 583
# km por dia;

# 5. Sair: Permite que o usuário saia do programa.


# Bagulho 1
CustoPorKMrodado = float(input('Digite o custo por KM rodado em R$: '))

if CustoPorKMrodado >= 0:
  print('Valor aceito!')
elif CustoPorKMrodado < 0:
  print('O valor deverá ser maior ou igual a zero!')
elif CustoPorKMrodado >= 'A' and 'Z':
  print('Não pode ser letras, apenas números maiores que zero')

else: print('Algo está errado!')
