# FUNÇÕES

# 1. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

def ler_temperatura():
  celsius = float(input('Informe a temperatura em graus Celsius: '))
  return celsius

def converter(celsius):
  fahrenheit = (9 * celsius + 160) / 5
  return fahrenheit

def mostrar(fahrenheit):
  print(fahrenheit)

celsius = ler_temperatura()
fahrenheit = converter(celsius)
mostrar(fahrenheit)