#Pesquisa linear
#Pesquisa: Uma pesquisa no vetor percorre cada elemento, Big O(n) - Linear
#Exclusão: Serão N passos para localizar o item, e mais N passos para mover os outros itens - Big O(2n) = Big O(n)
#Impedir valores duplicados

import numpy as np

class VetorNaoOrdenado:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)

  # O(n)
  def imprime(self):
    if self.ultima_posicao == -1:
      print('O vetor está vazio')
    else:
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ', self.valores[i])

  # O(1) - Função constante
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
    else:
      self.ultima_posicao += 1
      self.valores[self.ultima_posicao] = valor
  # O(n) - Linear
  def pesquisar(self, valor):
    for i in range(self.ultima_posicao + 1):
      if valor == self.valores[i]:
        return i
    return -1 #elemento não existe

  # O(n) - Linear
  def excluir(self, valor):
    posicao = self.pesquisar(valor)
    if posicao == -1: #não existe no vetor
      return -1
    else: 
      # a partir a posicao que encontramos
      # reposicionar os itens da lista
      for i in range(posicao, self.ultima_posicao):
        self.valores[i] = self.valores[i+1]

      self.ultima_posicao -= 1 #diminuir 1 da ultima posicao

# --- CRIANDO INSTANCIA ---

vetor = VetorNaoOrdenado(5)

# --- PREENCHENDO LISTA ---

vetor.insere(10)
vetor.insere(20)
vetor.insere(50)
vetor.insere(30)
vetor.insere(80)

# --- IMPRIMINDO LISTA ---

vetor.imprime()

# --- PESQUISANDO ITEM ---

vetor.pesquisar(80)

# --- EXCLUINDO ITEM ---

vetor.excluir(10)