# Solicita ao usuário que insira um número inteiro
numero = int(input("Digite um número inteiro: "))

# Inicializa a variável de verificação
eh_primo = True

# Verifica se o número é menor que 2 (não são primos)
if numero < 2:
    eh_primo = False
else:
    # Verifica se o número é divisível por algum número entre 2 e a raiz quadrada do número
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            eh_primo = False
            break

# Exibe o resultado
if eh_primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")