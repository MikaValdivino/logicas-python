# Solicita ao usuário que insira uma string
texto = input("Digite uma string: ").lower()

# Define as vogais
vogais = "aeiou"

# Conta as vogais na string
contador_vogais = sum(1 for letra in texto if letra in vogais)

# Exibe o resultado
print(f"A string contém {contador_vogais} vogais.")