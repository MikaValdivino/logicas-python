# Solicita ao usuário que insira uma string
texto = input("Digite uma string: ").lower()

# Divide a string em palavras
palavras = texto.split()

# Conta a ocorrência de cada palavra
ocorrencias = {}
for palavra in palavras:
    if palavra in ocorrencias:
        ocorrencias[palavra] += 1
    else:
        ocorrencias[palavra] = 1

# Exibe as ocorrências de cada palavra
print("A ocorrência de cada palavra na string é:")
for palavra, contagem in ocorrencias.items():
    print(f"{palavra}: {contagem}")