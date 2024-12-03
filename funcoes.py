def vetoriano (tamanho):
  vetor = []
  for i in range (tamanho):
    vetor.append(int(input()))
  print(vetor)



def teste (numero):
  resto = numero % 2 # A função % retorna sempre o que restou 
  #da divisão do número, se restou -1 significa que o numero é 
  # impar.
  if resto > 0:
    aux = -1
  else:
    aux = 1
  return aux