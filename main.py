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

def impar_par (numero):
  resto = numero % 2
  if resto > 0:
    aux = -1
  else:
    aux = 1
  return aux

a = int(input('Informe um número: '))
        
print("o numero é", impar_par(a))