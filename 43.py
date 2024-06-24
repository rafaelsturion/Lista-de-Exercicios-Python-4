def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def coletar_dados():
    nome = str(input("Digite o seu nome: "))
    ra = int(input("Digite o seu RA: "))
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    nota_exame = float(input("Digite a nota do exame: "))
    return nome, ra, nota1, nota2, nota_exame

def calcular_media(nota1,nota2):
    return (((nota1 + nota2) / 2) + nota_exame / 2 )

def verificar_aprovacao(media):
    if media >= 5:
        return "Parabéns, você aproveitou a sua chance! Está aprovado."
    else:
        return "Estude mais para a proxima!"
    


print(dados())

nome, ra, nota1, nota2, nota_exame = coletar_dados()
media = calcular_media(nota1, nota2)
resultado = verificar_aprovacao(media)


print(resultado)