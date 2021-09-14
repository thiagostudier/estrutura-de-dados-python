# --- TUPLAS ---

tupla = ('Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6')
print(tupla[0])
print(tupla.index('Item 3'))
for elemento in tupla:
  print(elemento)

# --- LISTAS ---

lista_1 = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6']
lista_2 = ['Item 7', 'Item 8', 'Item 9', 'Item 10', 'Item 11', 'Item 12']

print(lista_1 + lista_2) #concatenar

print(lista_1 * 2) #multiplicar os dados

print(lista_1[0]) #acessar elementos
print(lista_1[0:3])

lista_1.append('Item extra'); #adicionar novo item
print(lista_1)

lista_1.remove('Item 1') #remover item da lista
print(lista_1)

del(lista_1) #deletar lista

# --- DICIONÁRIOS ---

coleta = {'Item 1': 15, 'Item 2': 20, 'Item 3': 15, 'Item 4': 50, 'Item 5': 10}
coleta_2 = {'Item 1': 100, 'Item 7': 15, 'Item 8': 20}

coleta['Item 1'] #acessar um dado

coleta['Item 6'] = 35 #se o dado não existir, acrescentará no dicionário

print(coleta)

# del(coleta) #deletar dicionário
# del(coleta)['Item 1'] #deletar item do dicionário
# print(coleta)

print(coleta.items()) #apresentar as chaves e os valores
print(coleta.keys()) #apresentar as chaves
print(coleta.values()) #apresentar os valores

coleta.update(coleta_2) #unindo os  e sobrescrevendo
print(coleta)

#percorrendo dicionário
for item, num in coleta.items():
  print(f'{item}, número de resultados: {num}')


# --- CONJUNTOS ---

conjunto = ('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo', 'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')

print(set(conjunto)) #transformar em conjuto com a função set()

c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}

print(c1.intersection(c2)) #intersecção (somente os elementos que estão nos três conjuntos)

print(c1.difference(c2)) #somente os items não repetidos
print(c2.difference(c1)) #somente os items não repetidos

