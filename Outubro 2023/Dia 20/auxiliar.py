import sys
sys.path.insert(0, 'C:/Users/Dev/Desktop/Projetos Pessoais/Aula_Algoritmo_Univille/APC_II')

from funcoes import *


numero = int(input())

if teste(numero) == -1:
    print("É Impar")
else:
    print("É Par")

    
numero = int(input())

vetoriano(numero)