"""# Estrutura de repetição"""

for numero in range(1, 6):
  print(numero)


for numero in range(5, 0, -1):
  print(numero)


soma = 0
for numero in range(1, 6):
  soma = soma + numero
print(soma)


palavra = 'sorvete'
for letra in palavra:
  # print(letra)
  if letra == 'v':
    print('Achamos letra "v"')


numero = 1
while numero < 6:
  print(numero)
  numero += 1