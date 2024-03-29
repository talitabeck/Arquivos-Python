# -*- coding: utf-8 -*-
"""2-funcoes-numpy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IbIYS37_O3i5cP0pZdNouLdnspJUu-fa
"""

# Faça um programa que leia os seguintes dados da entrada:
# Uma cadeia de caracteres F;
# Um número decimal A representando o início de uma sequência;
# Um número decimal B representando o fim de uma sequência;
# Um número decimal C representando um incremento.
# Use os valores A, B, e C como parâmetros da função arange da biblioteca numpy e guarde o resultado em uma variável L. Depois, faça uma das operações seguintes:

# Se F="seno", use a biblioteca numpy para calcular o seno de todos os números de L, e armazene esse resultado em uma lista R;
# Se F="cosseno", use a biblioteca numpy para calcular o cosseno de todos os números de L, e armazene esse resultado em uma lista R;
# Se F="log10", use a biblioteca numpy para calcular o logaritmo na base 10 de todos os números de L, e armazene esse resultado em uma lista R;
# Se F="log2", use a biblioteca numpy para calcular o logaritmo na base 2 de todos os números de L, e armazene esse resultado em uma lista R;
# Por fim, use a função print para escrever os valores na lista R na saída. Os valores devem ser impressos separados por espaço, na mesma ordem em que estão na lista.
# Se o valor de F for inválido, escreva "funcao desconhecida" e termine o programa.

# Exemplo de entrada 1:
# seno
# 0
# 1
# 0.1
# Exemplo de saída 1:
# 0.0 0.09983341664682815 0.19866933079506122 0.2955202066613396 0.3894183423086505 0.479425538604203 0.5646424733950355 0.6442176872376911 0.71735

f = input()
a = float(input())
b = float(input())
c = float(input())

r = np.arange(a, b, c)

if f == 'seno':
  g = np.sin(r)
  print(*g, sep = ' ')

elif f == 'log2':
  g = np.log2(r)
  print(*g, sep = ' ')

elif f == 'log10':
  g = np.log10(r)
  print(*g, sep = ' ')

elif f == 'cosseno':
  g = np.cos(r)
  print(*g, sep = ' ')

else:
 print("Função desconhecida.")
