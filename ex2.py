# Exercício de fixação 2: Crie um programa que solicite ao usuário 
# duas listas com cinco elementos cada e, como resultado, 
# crie uma terceira lista que intercale os elementos das anteriores.

listaIntercalada = []
listaA = []
listaB = []
for _ in range(1,6):
    valor_1 = int(input(f'Digite um valor[{_}] para lista 1: '))
    listaA.append(valor_1)

for _ in range(1,6):
    valor_2 = int(input(f'Digite um valor[{_}] para lista 2: '))
    listaB.append(valor_2)

for i in range(5):
    listaIntercalada.append(listaA[i])
    listaIntercalada.append(listaB[i])
print('Elementos intercalados: ',listaIntercalada)