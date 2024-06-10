# Solicita ao usuário que insira uma lista de números inteiros
numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()

# Converte a lista de strings para uma lista de inteiros
numeros = [int(numero) for numero in numeros]

# Encontra o maior número na lista
maior_numero = max(numeros)

# Exibe o resultado
print(f"O maior número na lista é: {maior_numero}")