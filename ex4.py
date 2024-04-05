# Listas com comportamento de matriz

# Exercício de fixação 4: Crie um programa 
# que efetue a soma de duas matrizes 3x3, 
# sabendo que a soma desse tipo de matriz é 
# uma nova matriz 3x3, sendo cada elemento 
# resultado da soma dos elementos das matrizes 
# na mesma posição. Exemplo:

# | 1 2 3 |   | 3 2 3 |   | 4 4  6  |
# | 4 5 6 | + | 1 3 3 | = | 5 8  9  |
# | 7 8 9 |   | 0 2 2 |   | 7 10 11 |

# #ParaTodosVerem Abre colchetes linha 
# com 1 2 3, linha abaixo com 4 5 6, 
# linha abaixo com 7 8 9, fecha colchetes. 
# Sinal de adição e abre novo colchetes. 
# Linha com 3 2 3, linha abaixo com 1 3 3, 
# linha abaixo com 0 2 2, fecha colchetes.  
# Sinal de igual e abre novo colchetes 
# com linha  com 4 4 6, linha abaixo 
# com  5 8 9, linha abaixo com 7 10 11, 
# fecha colchetes.
matrizA = []
matrizB = []
matrizC = []

for i in range(3):
    matrizA.append([])
    for j in range(3):
        v = int(input(f'Insira o valor da L[{i+1}] x C[{j+1}] da Matriz A: '))
        matrizA[i].append(v)
for i in range(3):
    matrizB.append([])
    for j in range(3):
        v = int(input(f'Insira o valor da L[{i+1}] x C[{j+1}] da Matriz B: '))
        matrizB[i].append(v)
for i in range(3):
    matrizC.append([])
    for j in range(3):
        soma = matrizA[i][j] + matrizB[i][j]
        matrizC[i].append(soma)
for linha in matrizA:
    print(linha)
print(' + ')
for linha in matrizB:
    print(linha)
print(' = ')
for linha in matrizC:
    print(linha)
