# -*- coding: utf-8 -*-
"""00-idade.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HtPBY6-D8Iwjx-dj00J-xDuO_5BPl1jR
"""

x = input()
y = 2022 - int(x)

if int(y) <= 12:
  print("Voce tem",y,"anos e, portanto, e crianca.")

if int(y) <= 17 and int(y) > 12:
  print("Voce tem",y,"anos e, portanto, e adolescente.")

if int(y) <= 64 and int(y) >= 18:
  print("Voce tem",y,"anos e, portanto, e adulto.")

if int(y) >= 65:
    print("Voce tem",y,"anos e, portanto, e experiente.")