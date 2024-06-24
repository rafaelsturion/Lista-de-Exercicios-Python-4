def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def processar_idade(nome,idade):
    if idade >=18 and idade < 65:
        return f"Bem vindo {nome.title()} você é maior de idade"
    elif idade >= 65:
        return f"Bem vindo {nome.title()} você é maior de 65 anos"
    else: 
        return f"Bem vindo {nome.title()} você é menor de idade"
    
# Exibir os dados fixos
print(dados())

nome = str(input("Digite seu nome: "))
idade = int(input("Digite uma idade: "))


# Processar e exibir o idade processado
resultado = processar_idade(nome,idade)
print(resultado )
