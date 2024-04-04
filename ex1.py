# Exercício de fixação 1: Crie um programa que solicite ao 
# usuário seis números, calculando a média, e mostre uma lista com os números 
# iguais ou acima da média e uma lista com os números abaixo da média.
numeros = []
listaAcima = []
listaAbaixo = []

for i in range(1,7):
    n = float(input(f"Digite o numero[{i}]: "))
    numeros.append(n)
soma = sum(numeros)
md = soma/6
for n in numeros:
    if(n >= md):
        listaAcima.append(n)
    else:
        listaAbaixo.append(n)
print('A média dos 6 números é: ', md)
print('Lista Acima da média: ', listaAcima)
print('Lista Abaixo da média: ', listaAbaixo)

