import math

def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def processar_valor(valor):
    if valor in [1, 2]:
        return valor ** 3
    elif valor % 3 == 0:
        return math.factorial(valor)
    elif valor in [4, 5, 7, 8]:
        return valor / 9
    else:
        return "Valor inválido"

# Exibir os dados fixos
print(dados())

# Coletar o valor do usuário
valor = int(input("Digite um valor inteiro: "))



# Processar e exibir o valor processado
resultado = processar_valor(valor)
print(resultado)
