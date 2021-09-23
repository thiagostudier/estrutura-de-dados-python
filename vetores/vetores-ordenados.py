import numpy as np

class VetorOrdenado:
  
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
        print(i,' - ',self.valores[i])

  # O(n)
  def insere(self, valor):
    #VERIFICAR SE A CAPACIDADE MÁXIMA FOI ATINGIDA
    if self.ultima_posicao == self.capacidade - 1:
      print('Capacidade máxima atingida')
      return 
    # PEGAR A POSIÇÃO ONDE SERÁ INSERIDO O VALOR
    posicao = 0
    for i in range(self.ultima_posicao + 1):
      posicao = i
      # SE O VALOR É MAIOR QUE O VALOR QUE ESTÁ SENDO INSERIDO, PARAR A FUNÇÃO
      if self.valores[i] > valor:
        break
      # SE O VALOR É MAIOR QUE TODOS OS ELEMENTOS DO VETOR, INSERIR NA ÚLTIMA POSIÇÃO
      if i == self.ultima_posicao:
        posicao = i + 1
    # REPOSICIONAR TODOS OS ELEMENTOS APÓS A POSIÇÃO INSERIDA
    x = self.ultima_posicao 
    while x >= posicao: 
      self.valores[x + 1] = self.valores[x]
      x -= 1
    # INSERIR O VALOR NA NOVA POSIÇÃO DESOCUPADA
    self.valores[posicao] = valor
    # AUMENTAR O NÚMERO DA ÚLTIMA POSIÇÃO
    self.ultima_posicao += 1
  #O (log n)
  def pesquisar(self, valor): 
    # PERCORRER TODOS OS ITENS DO VETOR
    for i in range(self.ultima_posicao + 1):
      # SE O VALOR DO VETOR FOR MAIOR QUE O VALOR SENDO PESQUISADO, PARAR EXECUÇÃO
      if self.valores[i] > valor:
        return -1
      # SE O VALOR FOR ENCONTRADO, RETORNAR POSIÇÃO
      if self.valores[i] == valor:
        return i
      # SE ACABOU OS VALORES DO VETOR, FINALIZAR E RETORNAR FALSO
      if i == self.ultima_posicao:
        return -1
  # O (n)
  def excluir(self, valor):
    # PEGAR A POSIÇÃO DO ITEM A SER REMOVIDO
    posicao = self.pesquisar(valor)
    # SE A POSIÇÃO NÃO FOR VERDADEIRA
    if posicao == -1:
      return -1
    else: 
      # PERCORRER ITENS DO ARRAY A PARTIR DA POSIÇÃO DO ELEMENTO A SER REMOVIDO
      for i in range(posicao, self.ultima_posicao):
        # PEGAR O ITEM DO ARRAY E SOBRESCREVER COM O PRÓXIMO VALOR
        self.valores[i] = self.valores[i + 1]
      # DIMINUIR O NÚMERO DA ÚLTIMA POSIÇÃO DO ARRAY
      self.ultima_posicao -= 1
  #O (log n)
  def pesquisa_binaria(self, valor):
    limite_inferior = 0
    limite_superior = self.ultima_posicao

    while True:
      # PEGAR POSIÇÃO ATUAL, DIVIDINDO POR DOIS
      posicao_atual = int((limite_inferior + limite_superior) / 2)
      # SE ACHOU NA PRIMEIRA TENTATIVA
      if self.valores[posicao_atual] == valor:
        return posicao_atual
      # SE NÃO ACHOU
      elif limite_inferior > limite_superior:
        return -1
      # DIVIDIR LIMITES
      else: 
        # LIMITE INFERIOR
        if self.valores[posicao_atual] < valor: 
          limite_inferior = posicao_atual + 1
        else:
          limite_superior = posicao_atual - 1

# --- DENIFIR OBJETO ---
vetor = VetorOrdenado(10)
# --- IMPRIMIR VALORES ---
vetor.imprime()
# --- INSERIR VALORES ---
vetor.insere(1)
vetor.insere(2)
vetor.insere(3)
vetor.insere(4)
vetor.insere(5)
vetor.insere(6)
vetor.insere(7)
vetor.insere(8)
vetor.insere(9)
vetor.insere(10)
# --- PESQUISAR VALORES ---
vetor.pesquisar(10)
# --- EXCLUIR VALORES ---
vetor.excluir(5)