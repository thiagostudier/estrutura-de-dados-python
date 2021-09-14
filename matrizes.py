import numpy as np

matriz = np.array([[2,3,1],[4,5,7]])

print(matriz.shape) #formato da matriz (linhas, colunas)

print(matriz[0]) #pegar primeiro array
print(matriz[1]) #pegar segundo array

print(matriz[1][0]) #pegar primeiro item do segundo array

#percorrer arrays
for i in range(matriz.shape[0]): 
  print(matriz[i])
  #percorrer itens do array
  for j in range(matriz.shape[1]):
    print(matriz[i][j])