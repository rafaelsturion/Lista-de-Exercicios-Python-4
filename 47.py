def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def processar_valor(valor):
    if valor % 10 == 0 and valor % 5 == 0 and valor % 2 == 0:
        return "O número é divisível por 10, 5 e 2"
    elif valor % 10 == 0 and valor % 5 == 0:
        return "O número é divisível por 10 e 5"
    elif valor % 10 == 0 and valor % 2 == 0:
        return "O número é divisível por 10 e 2"
    elif valor % 5 == 0 and valor % 2 == 0:
        return "O número é divisível por 5 e 2"
    elif valor % 10 == 0:
        return "O número é divisível por 10"
    elif valor % 5 == 0:
        return "O número é divisível por 5"
    elif valor % 2 == 0:
        return "O número é divisível por 2"
    else: 
        return "O número não é divisível por 10, 5 ou 2"
    
# Exibir os dados fixos
print(dados())

valor = float(input("Digite um valor: "))


# Processar e exibir o valor processado
resultado = processar_valor(valor)
print(resultado)
