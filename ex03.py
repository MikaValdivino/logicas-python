# Solicita ao usuário que insira uma lista de números inteiros
numeros = input("Digite uma lista de números inteiros separados por espaço: ").split()

# Converte a lista de strings para uma lista de inteiros
numeros = [int(numero) for numero in numeros]

# Calcula a soma dos números na lista
soma = sum(numeros)

# Exibe o resultado
print(f"A soma dos números na lista é: {soma}")