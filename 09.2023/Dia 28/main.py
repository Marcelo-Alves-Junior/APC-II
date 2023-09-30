'''1) Função que recebe três valores e retorna o maior valor.'''

def maior_valor (a,b,c):
    if a > b and a > c :
        aux = a
    elif b > a and b > c :
        aux = b
    else:
        aux = c
    return aux

'''2) Encontre o perímetro de um triângulo, dados os comprimentos de seus três lados. Use uma função para calcular o perímetro. Obs.: P = a + b + c, onde a, b e c são os lados do triângulo')'''

def perimetro (a,b,c):
    return a + b + c

'''3) Crie uma função que retorna qual o conceito dada uma nota. Utilize a tabela a seguir: A >=9, B>=8, C>=7, D.=6, F<6 .'''

def conceito (nota):
    if nota >= 9 and nota<=10:
        conceito = 'A'
    elif nota >=8:
        conceito = 'B'
    elif nota >=7:
        conceito = 'C'
    elif nota >=6:
        conceito = 'D'
    else:
        conceito = 'F'
    return conceito

'''4) Crie uma função que retorna 1 se o aluno for aprovado em uma disciplina e 0 caso contrário, considerando que as seguintes informações são passadas como argumentos:
* o número total de aulas de uma disciplina;
* o número de faltas do aluno (que deve ser ≤ 25% das aulas);
* a nota deste aluno (que deve ser ≥ 6).'''

def passou (aulas,faltas,nota):
    percentual = ((aulas - faltas) / aulas) * 100
    if percentual >=75 and nota >=6:
        return 1
    else:
        return 0
    
'''5) Crie uma função que recebe a idade de uma pessoa e imprime a sua classe eleitoral, de
acordo com a tabela abaixo:'''

def classe_eleitoral (idade):
    if idade < 16:
        classe = 'Não-eleitor'
    elif idade <18 or idade >=66:
        classe = 'Eleitor Facultativo'
    else:
        classe = 'Eleitor obrigatório'
      
    return classe

'''6) Escreva uma função que receba um número e retorne -1 se o número for ímpar ou 1
se for par.'''

def impar_par (numero):
  resto = numero % 2
  if resto > 0:
    aux = -1
  else:
    aux = 1
  return aux

a = int(input('Informe um número: '))

a = int(input('Informe um número')
print(impar_par(a))

'''7) Escreva uma função para calcular o fatorial de um número. Lembre que fatorial de
número negativo não existe.'''



'''8) Séries de Taylor são vistas na disciplina de cálculo e são muito aplicáveis no campo da
informática. Uma série de Taylor pode ser utilizada para calcular o valor de seno de um
número em radianos. A série de Taylor para função seno é:'''