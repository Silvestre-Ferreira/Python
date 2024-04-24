import os

os.system("cls ||clear")

primeiroNumero: int
segundoNumero: int
soma : int
multiplicacao : int
divisao : float
subtracao : float

primeiroNumero = int (input("Digite o primeiro numero: "))
segundoNumero = int (input("Digite o segundo numero: "))

soma = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero

print (f"Primeiro numero: {primeiroNumero}")
print (f"Segundo Numero: {segundoNumero}")
print (f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")

