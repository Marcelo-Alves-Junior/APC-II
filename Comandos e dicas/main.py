###Formatando variáveis no print:

##Incluindo a variável dentro da String:
#print(f"Seu nome é {nome}, sua idade é {idade} e sua nota do semestre passado foi {semestre1}")

##Definindo que a variavel float terá 2 casas decimais:
#print(f"A área do circulo tem {area:,.2f}")

##Fazendo pequenos calculos dentro da propria String:
#print(f"A multiplicação de {numero1} * {numero2} é :  {numero1 * numero2}")

##Criando e printando uma lista de valores em ordem crescente
#lista=[valor1,valor2,valor3]
#print(sorted(lista))

##Criando variavel de texto para diminuir o código:
#texto = '\nO Funcionário {} recebia R${:.2f} e sua Categoria é ({}) portanto seu novo salário é de R${:.2f}'
#print(texto.format(nome,salario,categoria,newsalario))



###Trabalhando com listas:

##Verificando se string informada está na listagem correta:
#categoria5 = {'U', 'V', 'X', 'Y', 'W', 'Z'}
#...
#categoria = input(f"Informe a Categoria do Funcionário : ")
#if categoria in categoria5:
#...