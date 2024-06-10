# Solicita ao usuário que insira uma string
texto = input("Digite uma string: ").replace(" ", "").lower()

# Verifica se a string é um palíndromo
if texto == texto[::-1]:
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")