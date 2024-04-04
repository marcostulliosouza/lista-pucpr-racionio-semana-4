# Exercício de fixação 3: Crie um programa que 
# leia as temperaturas médias de cada 
# mês do ano e as armazene em uma lista; 
# use outro vetor para guardar e exibir, quando 
# necessário, o nome dos meses do ano; calcule a 
# média anual de temperatura e informe 
# quais meses ficaram acima da média anual.

temperaturas = []
meses = []
mes = {
    '1':'Jan',
    '2': 'Fev',
    '3': 'Mar',
    '4': 'Abr',
    '5': 'Mai',
    '6': 'Jun',
    '7': 'Jul',
    '8': 'Ago',
    '9': 'Set',
    '10': 'Out',
    '11': 'Nov',
    '12': 'Dez'
}
listaAcimaMD = []
for _ in mes:
    temperatura = float(input(f'Digite a média de temperatura do mês de {mes[_]}: '))
    temperaturas.append(temperatura)
    meses.append(mes[_])
md = sum(temperaturas)/len(meses)
for i in range(12):
    if(temperaturas[i]>=md):
        print(f'{meses[i]}: ', temperaturas[i], 'graus')