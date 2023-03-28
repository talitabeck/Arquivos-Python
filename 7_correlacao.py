# -*- coding: utf-8 -*-
"""7-correlacao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UmiXsiKJHgO2S2CBiOXUbzP3Xn7u4932
"""

import pandas as pd

numeroarquivos = int(input())
listaArquivos = []

for i in range(0,numeroarquivos):
 entrada = input()
 arquivo = pd.read_csv(entrada)
 listaArquivos.append(arquivo)

entrada = " "

while entrada != "sair":
  entrada = input()

  if entrada != 'sair':
    listadecomandos = entrada.split(' ')
    comando = listadecomandos[0]
    
    if comando.startswith('correlacaoInter'):
      colunaz = input()
      x = int(listadecomandos[1])
      y = int(listadecomandos[2])

      arquivox = listaArquivos[x-1]
      arquivoy = listaArquivos[y-1]
      relacao = arquivox[colunaz].corr(arquivoy[colunaz])
      print('%.5f'% relacao)

      if relacao > 0.9 or relacao < -0.9:
        print('Correlacao alta')

        
    elif comando.startswith('menorCorrelacao'):
        x = int(listadecomandos[1])
        arquivodacorrelacao = listaArquivos[x-1]
        correl = [arquivodacorrelacao.corr().min()]
        print('%.5f'% correl.sort())
        

    elif comando.startswith('maiorCorrelacaoPositiva'):
        x = int(listadecomandos[1])
        arquivodacorrelacao = listaArquivos[x-1]
        correl = arquivodacorrelacao.corr()
        if correl > 0:
            print(correl.max())
        
    elif comando.startswith('maiorCorrelacaoNegativa'):
        x = int(listadecomandos[1])
        arquivodacorrelacao = listaArquivos[x-1]
        correl = arquivodacorrelacao.corr()
        
        if correl < 0:
            print(correl.max())
        print(correl.min())