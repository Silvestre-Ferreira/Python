import os

os.system ("cls || clear")

nome : str
idade : int
primeiraNota : float
segundaNota: float
media : float


nome = str(input ("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
primeiraNota = float (input("Digite sua primeira nota: "))
segundaNota = float (input("Digite sua segunda nota: "))

media = (primeiraNota+segundaNota)/2
os.system ("cls || clear")

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {primeiraNota}")
print(f"Segunda Nota: {segundaNota}")
print(f"Media: {media}")