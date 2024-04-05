# Exercício de fixação 7:Dado o vetor 
# nums = [3, 11, 6, 32, 15, 22, 4, 10, 5], 
# crie uma matriz 3x3 com os três maiores 
# elementos na primeira linha, os três elementos 
# intermediários na segunda linha e 
# os elementos menores na terceira linha.

nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]
matriz = []
for i in range(3):
    matriz.append([])
    for j in range(3):
        maior = max(nums)
        matriz[i].append(maior)
        nums.remove(maior)
    matriz[i].sort()
for linha in matriz:
    print(linha)