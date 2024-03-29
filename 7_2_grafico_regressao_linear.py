# -*- coding: utf-8 -*-
"""7.2-grafico-regressao-linear.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qW6rCsRxwJ5y3VvvX9dBNtamDTm-27VZ
"""

# Commented out IPython magic to ensure Python compatibility.

# Neste exercício, você irá ler um arquivo CSV com dados históricos do preço de ações, e deverá gerar um gráfico baseado no arquivo. Um arquivo de entrada de
# exemplo está disponível para download.

# Escreva um código que faça as seguintes operações:

# Peça para o usuário fazer o upload de um arquivo CSV;
# Peça o nome do arquivo CSV submetido para o usuário;
# Faça um gráfico com o campo "Último" do CSV no eixo Y. O eixo X deve ser o índice daquele valor. Os valores devem ser apresentados em ordem cronológica. Esta
# linha do gráfico deve estar em azul;
# No mesmo gráfico, coloque uma reta, em vermelho, representando a regressão linear dos dados acima;
# O título do gráfico deve ser "Valor da ação", o rótulo do eixo X deve ser "Data" e o rótulo do eixo Y deve ser "Valor".
# Observações:

# Note que os dados no arquivo estão em ordem decrescente de data. Você pode inver a ordem de dados lidos no CSV numa variável df usando df[::-1] ao invés 
# de df;
# Para gerar os valores de X, você pode usar a função range passando tamanho dos seus dados;
# O separador decimal dos números no arquivo CSV é a vírgula. Atenção para esse fato no momento de leitura do arquivo.

#exercicio 2

from google.colab import files
import io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

print('Faça upload de um arquivo CSV: ')
arquivo = files.upload()

nomedoarquivo = input('Digite o nome do arquivo (com a extensão .csv): ')

f =  pd.read_csv(io.BytesIO(arquivo[nomedoarquivo]), decimal = ',')
#a funçao decimal corrige as vírgulas utilizadas na tabela como separadores decimais, e as transforma em ponto

g = f[::-1]
#inverte a tabela
numerolinhas = len(g)
#conta o numero de linhas da tabela
x = np.arange(0,numerolinhas)
#faz um grupo dos valores para colocar na escala do eixo x do plano cartesiano
y = g['Último']
#torna os valores da coluna 'último' da tabela como a escala do eixo y


(a,b) = np.polyfit(x= np.arange(0,numerolinhas), y= g["Último"], deg=1)
#criamos os coeficientes lineares a e b para fazer a linha de regressão linear no gráfico
v = a*x + b
#criamos uma função para a linha de regressão linear do gráfico, sendo v = f(x)


plt.plot(x,v,'r')
#exibe a linha de regressao linear do valor das ações pela data e o r faz a linha ser vermelha
plt.plot(x,y,'b')
#exibe o gráfico do valor das ações pela data e o b faz a linha ser azul
plt.title("Valor da ação")
#da nome ao gráfico
plt.xlabel("Data")
#da nome ao eixo x   
plt.ylabel("Valor")
#da nome ao eixo y
plt.grid()
#coloca grade no gráfico
