#função
def validação(nota1: int, nota2: int, nota3:int) -> bool:
    if nota1 >=0 or nota1 <=100 and nota2 >= 0 or nota2 <=100 and nota3 >=0 or nota3<=100:
        print('notas válidas!')
        return True
    else:
        print('notas inválidas, tente novamente!')
    return False

def media_arit(nota1: int, nota2: int, nota3: int) -> bool:
       return (nota1 + nota2 + nota3) / 3
def aprovado_ou_nao(nota1: int, nota2: int, nota3: int) -> bool:
    if media >= 70:
        print(f'A media do aluno(a) {nome} foi {media:.2f}, está aprovado! Parabéns!')
        return True
    else:
        print(f'A média do aluno(a) {nome} foi de {media:.2f}, está reprovado...')
        return False



#Sitemas de notas do Suap(código principal)
nome = input('Nome do aluno: ')
print('-----Média de notas do suap-----')
nota1 = float(input('digite sua primeira nota:' ))
nota2 = float(input('digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))
if validação(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
aprovado_ou_nao(nota1, nota2, nota3)


















