# --- PRIMEIRO EXEMPLO ---

# executa 11 passos - passando o número 10
# BIG O(n) - de acordo com o valor de N que for passado
def soma1(n):
  soma = 0
  for i in range(n+1):
    soma += i

  return soma

%timeit soma1(10)

# --- SEGUNDO EXEMPLO ---

#sempre executará 3 passos
# BIG O(3) - sempre executará 3 ações
def soma2(n):
  return (n * (n + 1) / 2)

%timeit soma2(10)

# CONCLUSÃO: soma2() tem um desempenho melhoe