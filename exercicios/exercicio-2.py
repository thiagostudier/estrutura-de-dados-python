""" 1. Ler 5 notas e informar a média """

nota = media = soma = 0

for i in range(1, 6):
  nota = float(input(f'Digite a nota {i}: '))
  soma += nota 

media = soma / 5
print('A média é: ', media)

""" 2. Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30) """

i = 1

while i <= 10:
    print(f'3 x {i}= ', i*3)
    i += 1