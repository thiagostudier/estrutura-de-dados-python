lista = [1,2,3,4,5]

#FUNÇÃO O(1) (Constante)
# Pois independente do número de elementos, sempre irá retornar o mesmo valor
def constant(n):
  print(n[0])

# constant(lista)

#FUNÇÃO Linear O(n)
# Função aumentará proporcionalmente dependendo do valor de n
# Se percorrer apenas uma vez o "n", é linear
def linear(n):
  for i in n:
    print(i)

# linear(lista)

#FUNÇÃO Quadrática O(n^2) - (polinomial)
# Se percorrer duas vezes o "n", é quadrática
def quadratic(n):
  for i in n: 
    for j in n: 
      print(i, j)

# quadratic(lista)

#FUNÇÃO Combination
# O(1) + O(5) + O(n) + O(n) + O(3)
# O(9) + O(2n)
# O(n) = complexidade final do exercício
def combination(n):
  #função constante - O(1)
  print(n[0])
  #função constante - O(5)
  for i in range(5):
    print('test', i)
  #função linear - O(n)
  for i in n:
    print(i)
  #função linear - O(n)
  for i in n:
    print(i)
  #função constante - O(3)
  print('Python')
  print('Python')
  print('Python')

combination(lista)