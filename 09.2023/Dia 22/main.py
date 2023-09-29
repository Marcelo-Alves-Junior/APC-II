#Função

def nome_da_funcao (a,b):
  c = a + b
  return c

def media (x,y,z):
  ab = (x + y + z) / 3
  return ab

a = float(input("Informe um número: "))
b = float(input("Informe um número: "))
c = float(input("Informe um número: "))
print("A média dos tres números é: ", media(a, b, c))


def fatorial (n):
  fat = n
  i = 0
  while i < n:
   fat = fat * (n - i)
   i = i + 1
  return fat

print("Calcularemos o fatorial de um número")
print("Informe o fatorial")