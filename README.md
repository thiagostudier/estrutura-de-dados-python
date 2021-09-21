# estrutura-    de-dados-python
Curso Estrutura de Dados e Algoritmos em Python: O Guia Completo

### Instalação

- Python: http://python.org/
- Anaconda: https://www.anaconda.com/
- PyCharm

#### Vantagem de trabalhar com o Anaconda

Permite criar vários ambientes Python 

## Python

### Módulos úteis

- Biblioteca math
- Biblioteca datetime
- Biblioteca random
- Biblioteca time

### Tratamento de Erros

- NameError: variável não foi definida
- TypeError: tipos de dados incompatíveis
- RuntimeError: erro de execução
- SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
- ZeroDivisionError: divisão por zero
- IndexError: índice fora da coleção

## Sobre Coleções

#### O que são tuplas?

- Imutáveis (não pode modificar);
- Útil para dados fixos;
- Mais rápido do que as listas;

- `tupla = ('Item 1', 'Item 2', 'Item 3', 'Item 4')`
- `tupla[0] => 'Item 1'`
#### O que são listas?

- Estrutura mais utilizada;
- Pode-se modificar os elementos;
- Aumenta e diminui o tamanho;

- `lista = [1,2,3]`

#### O que são dicionários?

- Pares de chave/valor;
- Array associativo (similar ao HashMap do Java);
- Não ordenado

- `dicionario = {´João´:20, ´Maria´: 30, ´Pedro´: 25}`

#### O que são conjuntos (set)?

- Armazena itens não duplicados;
- Acessa muito mais rápido do que as listas;
- Suporta operações matemáticas (união, intersecção, diferença);
- Não ordenado;

- `conjunto = {1,2,3}`

## Notação Big O

- Como comparar dois algoritmos?
- Comparação objetiva entre algoritmos
- Considera diferenças entre poder de processamento, sistema operacional, linguagem de programação
- O quanto a "complexidade" do algoritmo aumenta de acordo com as entradas

### Funções Bio O

- Constante ` O(1) `
- - É aquela em que não há crescimento do número de operações, pois não depende do volume de dados de entrada (n). Por exemplo: o acesso direto a um elemento de uma matriz.
- Logaritmo ` O(n) `
- - É aquela em que o crescimento do número de operações é menor do que o do número de itens. Exemplo: caso médio do algoritmo de busca em árvores binárias ordenadas.
- Linear ` O(n) `
- - É aquela em que o crescimento no número de operações é diretamente proporcional ao crescimento do número de itens. Por exemplo: o algoritmo de busca em uma lista/vetor.
- Linearitmica ou Quasilinear ` O(n log n) `
- - É aquela em que é resultado das operações (log n) executada n vezes. Exemplo: o caso médio do algoritmo de ordenação Quicksort.
- Quadrática ` O(2^n) `
- - É aquela que ocorre quando os itens de dados são processados aos pares, muitas vezes com repetições dentro da outra. Com dados suficientemente grandes, tendem a se tornar muito ruim. Por exemplo: o processamento de itens de uma matriz bidimensional.
- Exponencial ` O(2^n ) `
- - É aquela em que a medida que n aumenta, o fator analisado (tempo ou espaço) aumenta exponencialmente. Não é executável para valores muito grandes e não são úteis do ponto de vista prático. Exemplo: busca em uma árvore binária não ordenada.
- Fatorial ` O(n!) `
- - É aquela em que o número de instruções executadas cresce muito ra pidamente para um pequeno número de dados. Por exemplo: um algoritmo que gere todas as possíveis permutações de uma lista.