import math

print("1 – Faça um programa que calcula a área de um círculo, tendo como entrada o raio do mesmo.")
print()
pi = 3.14159265359
raio = float (input("Informe o valor do raio do círculo: "))
area = pi * (raio**2)
print(f"A área do circulo tem {area:,.2f}")


print("2	– Faça um programa que multiplique dois números inteiros e mostre o resultado da multiplicação")
print()
numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
print(f"A multiplicação de {numero1} * {numero2} é :  {numero1 * numero2}")


print("Questão 3 - Faça um programa que calcule a área de triângulo equilátero (todos os lados são iguais), tendo como entrada a base e a altura.")
print()
base = float(input("Informe a base do triângulo equilátero: "))
altura = float(input("Informe a altura do triângulo equilátero: "))
area = (base*altura) / 2
print(f"A área de triângulo equilátero é {area}")


print("4 – Faça um programa que calcule e exiba a média de dois números digitados.")
print()
numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))
media = (numero1 + numero2) / 2
print(f"A média entre os números {numero1} e {numero2} é :{media:,.2f}")


print("5 – Faça um programa que leia a temperatura em graus Celsius e apresente convertida em graus Fahrenheit. A fórmula de conversão é: F = (9*C + 160)/5. Sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.")
print()
celsius = float(input("Informe a temperatura em graus Celsius: "))
fahrenheit = ((9*celsius)/5)+(160/5)
print(f"A temperatura em graus Fahrenheit é de: {fahrenheit} ")


print("6 – Efetuar a leitura de um número inteiro e apresentar a raiz quadrada deste número.")
print()
numero = float (input("Informe um número; iremos calcular sua raiz quadrada :"))
raiz = numero**0.5
print(f"O valor da raiz quadrada de {numero:.0f} é {raiz:.0f}")


print("7 – Elaborar um programa que calcule e apresente o volume de uma caixa retangular, \npor meio da fórmula: volume = comprimento * largura * altura")
print()
comprimento = float (input("Informe o comprimento da caixa em centímetros (cm); \niremos calcular o volume da caixa em metros cúbicos (m³) : "))
largura = float (input("Informe a largura da caixa em centímetros (cm); \niremos calcular o volume da caixa em metros cúbicos (m³) : "))
altura = float (input("Informe a altura da caixa em centímetros (cm); \niremos calcular o volume da caixa em metros cúbicos (m³) : "))
volume = (comprimento/100)*(largura/100)*(altura/100)
print(f"Uma caixa com {comprimento:.0f}cm de comprimento, {largura:.0f}cm de altura e {altura:.0f}cm de altura; tem {volume}m³ de volume")


print("8 – Ler dois valores inteiros para as variáveis A e B. \nEfetuar a troca dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B \npasse a possuir o valor da variável A. \nApresentar os valores trocados.\n")
variavelA = float(input("Informe o valor da variável A: "))
variavelB = float(input("Informe o valor da variável B: "))
print(f"O valor variável A é: {variavelA} e da variável B é: {variavelB}")
variaveltemporaria = variavelA
variavelA = variavelB
variavelB = variaveltemporaria
print("Invertendo valores ... ")
print(f"O novo valor variável A é: {variavelA} e da variável B é: {variavelB}")


print("9 - Construa um programa que calcule a quantidade de latas de tinta necessárias e o custo para pintar tanques cilíndricos de combustível, \nonde são fornecidos a altura e o raio desse cilindro. \nSabendo que: \nA lata de tinta custa R$20,00 \nCada lata contém 5 litros \nCada litro de tinta pinta 3 metros quadrados. \nÁrea do cilindro=2*3.14*raio² + 2*3.14*raio*altura e que raio e altura são dados de entrada.\n")
precoDaLata = 20
litrosPorLata = 5
metrosPorLitro = 3
metrosPorLata = litrosPorLata * metrosPorLitro
raio = float(input("Informe o raio do cilindro: "))
altura = float(input("Informe a altura do cilindro: "))
areaCilindro=(2*3.14*(raio**2)) + (2*3.14*raio*altura)
latasPorCilindro = areaCilindro / metrosPorLata
print(f"Será necessário {latasPorCilindro:.3f} latas para pintar o Cilindro de {areaCilindro} m²")
custo = (math.ceil(latasPorCilindro))*precoDaLata
print(f"O custo total será: R${custo:.2f}")


print("10 - Construa um programa que tendo como entrada dois pontos quaisquer do plano P(x1,y1) e Q(x2,y2), \nimprima a distância entre eles.\n")
x1 = float (input("Digite o valor de x1: "))
y1 = float (input("Digite o valor de y1: "))
x2 = float (input("Digite o valor de x2: "))
y2 = float (input("Digite o valor de y2: "))
print(f"Os valores dos pontos do plano P: (x1= {x1:.2f}, y1= {y1:.2f}) e Q: (x2= {x2:.2f}, y2= {y2:.2f})")
formula = ((((x2-x1)**2)+((y2-y1)**2))*0.5)
print(f"A distancia entre os pontos do plano P e Q é: {formula:.2f}")


print(" 11 – Construir um programa que efetue o cálculo do salário líquido de um funcionário. Para fazer este programa, \nvocê deve possuir alguns dados, tais como: \nvalor da hora, número de horas trabalhadas no mês e percentual de desconto do INSS. \nEm primeiro lugar, deve-se estabelecer qual será o seu salário bruto para efetuar o desconto e ter o valor do salário líquido.\n")
valorDaHora = float (input("Informe o valor da hora trabalhada: "))
horasPorMes = float (input("Informe a quantidade de horas trabalhadas: "))
salario = valorDaHora * horasPorMes
print(f"Salário: {salario}")
aliquota1 = 1320 * 0.075
aliquota2 = (2571.29 - 1320) * 0.09
aliquota3 = (3856.94 - 2571.29) * 0.12
if salario <= 1320 :
  descontoInss = salario * 0.075
elif salario <= 2571.29 :
  descontoInss = ((salario - 1320.00) * 0.09) + aliquota1
elif salario <= 3856.94 :
  descontoInss = ((salario - 2571.29) * 0.12) + aliquota2 + aliquota1
else:
  descontoInss = ((salario - 3856.94) * 0.14) + aliquota3 + aliquota2 + aliquota1
salarioLiquido = salario - descontoInss
print(f"O valor do Salário Líquido é de: {salarioLiquido:.2f}")


print("12 - Faça um algoritmo que leia dois números A e B e mostre o maior deles.\n")
a = float (input("Digite o valor de A: "))
b = float (input("Digite o valor de B: "))
if a>b :
  print(f"O valor de A ({a}) é maior que o valor de B ({b})")
elif a<b :
  print(f"O valor de B ({b}) é maior que o valor de A ({a})")
else:
  print(f"O valor de A ({a}) é IGUAL ao valor de B ({b})")


print("13 -. Faça um algoritmo que leia um número N e mostre “F1”, “F2” ou “F3”, conforme a condição: \n“F1”, se N <= 10 \n“F2”, se N > 10 e N <= 100 \n“F3”, se n > 100")
n = float (input("Digite o valor de N: "))
if n<=10 :
  print("F1")
elif n<=100 :
  print("F2")
else:
  print("F3")


print("14 -  O sistema de avaliação de determinada disciplina, é composto por três provas. A primeira prova tem peso 2, \na segunda tem peso 3 e a terceira tem peso 5. Faça um algoritmo para calcular a média final de um aluno desta disciplina.")
prova1 = float (input("Informe a nota da primeira prova: "))
prova2 = float (input("Informe a nota da segunda prova: "))
prova3 = float (input("Informe a nota da terceira prova: "))
media = ((prova1*2) + (prova2*3) + (prova3*5)) / 10
print(f"A média final do aluno é {media:.2f}")


print("15 - Construa um algoritmo que receba como entrada três valores e os mostre em ordem crescente.")
valor1 = float (input("Informe o primeiro valor: "))
valor2 = float (input("Informe o segundo valor: "))
valor3 = float (input("Informe o terceiro valor: "))

if valor1>=valor2 and valor2>valor3 :
  print (valor3,valor2,valor1)
elif valor1>=valor2 and valor2<valor3 :
  print(valor2,valor1,valor3)
elif valor1<valor2 and valor2<=valor3 :
  print (valor1,valor2,valor3)

#Utilizando Lista e comando Sorted:
lista=[valor1,valor2,valor3]
print(sorted(lista)) #comando para definir ordem crescente
print(lista) #Imprimindo lista conforme definido na linha de lista


print("16 - Considere que o último concurso vestibular apresentou três provas: Português, Matemática e Conhecimentos Gerais. \nConsiderando que para cada candidato tem-se um registro contendo o seu nome e as notas obtidas em cada uma das provas, \nconstrua um algoritmo que forneça:\na) o nome e as notas em cada prova do candidato\nb) a média do candidato\nc) uma informação dizendo se o candidato foi aprovado ou não.\nConsidere que um candidato é aprovado se sua média for maior que 7.0 e se não apresentou nenhuma nota abaixo de 5.0")

turma= []
alunos = int (input("Informe a quantidade de Alunos : "))
for i in range(alunos):
  nome = input("Informe o Nome do Aluno: ")
  pt = input(f"Informe a nota de Portugues do {nome}: ")
  mat = input(f"Informe a nota de Matemática do {nome}: ")
  con = input(f"Informe a nota de Conhecimentos Gerais do {nome}: ")
  turma.append(nome)
  turma.append(pt)
  turma.append(mat)
  turma.append(con)
print(turma)


print("17 - Uma empresa irá dar um aumento de salário aos seus funcionários de acordo com a categoria de cada empregado. \nO aumento seguirá a seguinte regra: \nFuncionários das categorias A, C, F, e H ganharão 10% de aumento sobre o salário; \nFuncionários das categorias B, D, E, I, J e T ganharão 15% de aumento sobre o salário; \nFuncionários das categorias K e R ganharão 25% de aumento sobre o salário; \nFuncionários das categorias L, M, N, O, P, Q e S ganharão 35% de aumento sobre o salário; \nFuncionários das categorias U, V, X, Y, W e Z ganharão 50% de aumento sobre o salário. \nFaça um algoritmo que mostre nome, categoria e salário reajustado de cada empregado.\n")

nome = input("Informe o nome do Funcionário: ")
salario = float (input(f"Informe o salário do Funcionário : "))
'''
#versão utilizando número de categoria (Não Finalizada)
categoria = int (input(f"Informe o número da Categoria do Funcionário {nome} .\nSendo: \n1 - (A, C, F, e H) \n2- (B, D, E, I, J e T) \n3 - (K e R)\n4 - (L, M, N, O, P, Q e S) \n5 - (U, V, X, Y, W e Z) \n"))
if categoria == 1 :
  newsalario = salario + (salario * 0.1)
elif categoria == 2 :
  newsalario = salario + (salario * 0.15)
elif categoria == 3 :
  newsalario = salario + (salario * 0.25)
elif categoria == 4 :
  newsalario = salario + (salario * 0.35)
elif categoria == 5 :
  newsalario = salario + (salario * 0.50)
else:
  print("Número da Categoria informada não existe")

print (f"O Funcionário {nome} recebia R${salario} e sua Categoria é ({categoria}) portanto seu novo salário é de R${newsalario}")'''

'''
#Versão utilizando operador lógico "OU" (não finalizada)
categoria = input(f"Informe a Categoria do Funcionário : ")
if categoria == "A" or categoria == "C" or categoria == "F" or categoria == "H" :
  newsalario = salario + (salario * 0.1)
elif categoria == "B" or categoria == "D" or categoria == "E" or categoria == "I" or categoria == "J" or categoria == "T" :
  newsalario = salario + (salario * 0.15)
else:
  newsalario = salario + (salario * 0.3)
'''

categoria = input(f"Informe a Categoria do Funcionário : ")
categoria1 = {'A', 'C', 'F','H'}
categoria2 = {'B', 'D', 'E', 'I', 'J', 'T'}
categoria3 = {'K','R'}
categoria4 = {'L', 'M', 'N', 'O', 'P', 'Q', 'S'}
categoria5 = {'U', 'V', 'X', 'Y', 'W', 'Z'}
texto = '\nO Funcionário {} recebia R${:.2f} e sua Categoria é ({}) portanto seu novo salário é de R${:.2f}'
if categoria in categoria1:
  newsalario = salario + (salario * 0.1)
  print(texto.format(nome,salario,categoria,newsalario))
elif categoria in categoria2:
  newsalario = salario + (salario * 0.15)
  print(texto.format(nome,salario,categoria,newsalario))
elif categoria in categoria3:
  newsalario = salario + (salario * 0.25)
  print(texto.format(nome,salario,categoria,newsalario))
elif categoria in categoria4:
  newsalario = salario + (salario * 0.35)
  print(texto.format(nome,salario,categoria,newsalario))
elif categoria in categoria5:
  newsalario = salario + (salario * 0.5)
  print(texto.format(nome,salario,categoria,newsalario))
else:
  print("Categoria informada não existe")