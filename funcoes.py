# funções

def mensagem():
  print('Texto da função')

mensagem()



def mensagem(texto):
  print(texto)

mensagem('thiago')



def soma(a, b):
  return a+b

print(soma(5, 6))



def calcula_energia_potencial_gravitacional(m, h, g = 10):
  return g * m * h

print(calcula_energia_potencial_gravitacional(30, 12))

print(calcula_energia_potencial_gravitacional(30, 12, 9.8))

