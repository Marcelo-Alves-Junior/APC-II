'''Questão 1) Crie um programa que peça 10 números, armazene eles em um vetor e diga qual elemento é o maior, e seu valor e a posição do vetor na qual ele foi armazenado. Para localizar o maior utilize estrutura de decisão. Utilize também uma função do Python para localizar o maior elemento
'''


vetor = []
maior = 0
posicao = 0

for i in range (10) :
  vetor.append(int(input(f"Informe o número da posição {i} do vetor : ")))

for i in range (10) :
  if maior < vetor[i] :
    maior = vetor[i]
    posicao = i

print("\nO maior elemento do vetor é o que está na posição {} e seu valor é {} .".format(posicao,maior))


'''Questão 2)  Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida'''

matriz = []

for i in range (5) :
  matriz.append([])
  for j in range (5) :
    if i == j :
      matriz[i].append(1)
    else :
      matriz[i].append(0)

print(matriz)

'''matriz = [[i,x,0,0,0,0],
          [0,1,0,0,0],
          [0,0,1,0,0],
          [0,0,0,1,0],
          [0,0,0,0,1]]'''

''

'''Questão 3) 5. Escreva um algoritmo que preencher uma matriz M(5,5) e calcule as somas:'''

'''a) da linha 4 de M;'''



'''b) da coluna 2 de M;'''

'''c) da diagonal principal;

d) da diagonal secundária;

e) de todos os elementos da matriz;'''



'''Questão 4) Escrever um algoritmo que lê um vetor N(20) e o escreve. Troque, a seguir, o 1º elemento com o último, o 2º com o penúltimo etc. até o 10º com o 11º e escreva o vetor N assim modificado.'''