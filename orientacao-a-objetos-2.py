class Aluno:
  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.media = 0.0

  def calcula_media(self):
    self.media = (self.nota1 + self.nota2) / 2
    return self.media
  
  def mostra_dados(self):
    print('Nome:', self.nome)
    print('Nota 1:', self.nota1)
    print('Nota 2:', self.nota2)
    print('Média:', self.media)

  def resultado(self):
    if self.media >= 6:
      print('Aprovado')
    else:
      print('Reprovado')




aluno1 = Aluno('Pedro', 7,9)

print(aluno1.calcula_media())
print(aluno1.mostra_dados())
print(aluno1.resultado())