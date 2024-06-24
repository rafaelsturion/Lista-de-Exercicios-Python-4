def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def calcular_desconto(valor):
    if valor >= 300:
        return valor * 0.8
    elif valor >= 200 and valor <299.99:
        return valor * 0.9
    else: 
        return valor * 0.95
    
# Exibir os dados fixos
print(dados())

valor = float(input("Digite o valor do produto: "))


# Processar e exibir o valor processado
resultado = calcular_desconto(valor)
print(resultado)
