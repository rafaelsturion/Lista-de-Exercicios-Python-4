def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def processar_valor(valor):
    if valor < 0:
        return abs(valor)
    elif valor >10:
        valor2 = float(input("Digite outro número: "))
        return abs(valor - valor2)
    else: 
        return valor / 5
    
# Exibir os dados fixos
print(dados())

valor = float(input("Digite um valor: "))


# Processar e exibir o valor processado
resultado = processar_valor(valor)
print(resultado)
