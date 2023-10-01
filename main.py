import math
'''print("10 - Escrever um algoritmo que lê um valor N inteiro e positivo e que calcula e escreve o valor de E. E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + 1 / N!")

n = int (input("Informe um número:"))

i = 1
fat = n
e = 0
for _ in range(n):
  e = i 
  while i < n:
    fat = fat * (n - i)
    i = i + 1
print (fat)'''

'''def impar_par (numero):
  resto = numero % 2
  if resto > 0:
    aux = -1
  else:
    aux = 1
  return aux

a = int(input('Informe um número: '))
        
print("o numero é", impar_par(a))'''

def fatorial (numero):
  fat = numero # Salva o numero para executar as multiplicações
  i = 1
  while i < numero:
    fat = fat * (numero - i)
    i = i + 1
  return fat

'''8) Séries de Taylor são vistas na disciplina de cálculo e são muito aplicáveis no campo da
informática. Uma série de Taylor pode ser utilizada para calcular o valor de seno de um número em radianos. A série de Taylor para função seno é:'''

def taylor (numero):
  acomuladora = 0.00
  i = 0
  while i < numero:
    elemento = ((-1)**i) / fatorial(2*i+1)
    acomuladora = acomuladora + elemento
    i = i + 1
  return acomuladora


print(taylor(math.pi()/2))