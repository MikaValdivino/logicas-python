# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa a variável do fatorial
fatorial = 1

# Calcula o fatorial
for i in range(1, numero + 1):
    fatorial *= i

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial}.")