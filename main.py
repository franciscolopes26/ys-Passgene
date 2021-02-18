import random

letras_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_lowercase = letras_uppercase.lower()

digitos = "0123456789"

simblos = "{}[]"'><@#$%^&*();:'

upper, lower, nums, syms = True,True,True,True
palavra_chave = " "


if upper:
    palavra_chave += letras_uppercase
if lower:
    palavra_chave += letras_lowercase
if nums:
    palavra_chave += digitos


    comprimento =10

    quantidade=1

for x in range(quantidade):
    password = "".join(random.sample(palavra_chave,comprimento))

print(password)