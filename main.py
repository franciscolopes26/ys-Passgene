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
if syms:
    palavra_chave += simblos

    length =15
    ammount=10

for x in range(ammount):
    password="".join(random.sample(palavra_chave,length))
    print(password)