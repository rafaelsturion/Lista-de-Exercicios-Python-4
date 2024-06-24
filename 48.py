def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def processar_salario(valor):
    if valor <=1500:
        return f"O seu novo sálario é de R${valor * 1.2} reais."
    elif valor > 1500 and valor < 2500:
        return f"O seu novo sálario é de R${valor * 1.1} reais."
    else: 
        return f"O seu novo sálario é de R${valor * 1.05} reais."
    
# Exibir os dados fixos
print(dados())

valor = float(input("Digite um valor: "))


# Processar e exibir o valor processado
resultado = processar_salario(valor)
print(resultado )
