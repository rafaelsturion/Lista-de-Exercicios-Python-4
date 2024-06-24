def dados():
    return "João Rafael Sturion Mantoanelli, RA1051392411012, turma DSM 1"

def coletar_dados():
    nome = str(input("Digite o seu nome: "))
    ra = int(input("Digite o seu RA: "))
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    return nome, ra, nota1, nota2

def calcular_media(nota1,nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    if media >= 7:
        return "Parabéns, você está aprovado"
    else:
        return "Você ainda tem uma chance! Estude mais para o exame"

print(dados())

nome, ra, nota1, nota2 = coletar_dados()
media = calcular_media(nota1, nota2)
resultado = verificar_aprovacao(media)


print(resultado)