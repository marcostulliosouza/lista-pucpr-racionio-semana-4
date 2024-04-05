# A matriz-identidade é uma matriz com a 
# mesma quantidade de linhas e colunas, 
# apresentando todos os elementos da diagonal 
# principal (de cima para baixo, da esquerda 
# para a direita) iguais a 1 e os demais 
# elementos iguais a 0. Crie um programa que 
# solicite o tamanho da matriz desejada, 
# gerando a matriz-identidade. Exemplo:

#             | 1 0 0 |               | 1 2 0 0 |
# Matriz I3:  | 0 1 0 |   matriz I4:  | 0 1 0 0 |
#             | 0 0 1 |               | 0 0 1 0 |
#                                     | 0 0 0 1 |
matrizID = []

tamanho = int(input('Digite o tamanho da matriz: '))

for i in range(tamanho):
    matrizID.append([])
    for j in range(tamanho):
        if(i==j): 
            matrizID[i].append(1)
        else:
            matrizID[i].append(0)
for linha in matrizID:
    print(linha)
