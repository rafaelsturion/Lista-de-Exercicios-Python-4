import math

def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def realizar_conta(numero):
    if numero in [1,2,3]:
        return numero ** 2
    elif numero in [4,9]:
        return math.sqrt(numero)
    elif numero in [6,7,8]:
        return (numero / 9)
    else:
        return "Número inválido"
numero = float(input("Digite um número entre 1 e 9: "))

print(dados())
print(realizar_conta(numero))