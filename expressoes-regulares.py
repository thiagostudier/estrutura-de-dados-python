import re

# --- SEARCH ---

frase = 'Olá, meu número é (51)99236-5609'

# \(\d{2}\) - mapeamento do DDD

numero_telefone = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase) #procurar o número de telefone dentro da string
print(numero_telefone)

frase = 'A placa do carro que anotei é FRT-1998'

placa = re.search('[A-Z]{3}-\d{4}', frase)
print(placa)

email = 'Entre em contato, meu e-mail é thiagostudier9@gmail.com'
email = re.search('\w+@\w+\.com', email)
print(email)


# --- MATCH ---


frase = 'A placa do carro que anotei é FRT-1998'

placa = re.match('[A-Z]{3}-\d{4}', frase)
print(placa)

frase2 = 'FRT-1998 A placa do carro que anotei é'

placa = re.match('[A-Z]{3}-\d{4}', frase2) #encontra se estiver no início da string
print(placa)


# --- FINDALL ---

frase = 'Olá, meu número é (51)99236-5609. O número antigo é (51)99964-5348'

numero_telefone = re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase) #trazer todos os resultados
print(numero_telefone)