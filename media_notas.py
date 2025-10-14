#definições
def boas_vindas(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

def verifica_nota(nota1:float, nota2:float, nota3:float) -> bool:
    if nota1 <= 100 and nota2 <= 100 and nota3 <= 100:
        print('Notas válidas!')
        return True
    else:
        print('Notas inválidas!')
        return False

def media_arit(nota1:float, nota2: float, nota3:float) -> float:
    media = (nota1 + nota2 + nota3)/ 3
    if media >=70:
        print(f'O aluno(a) {nome} está aprovado(a)! Parabéns!')
        return media
    else:
        print(f'O aluno(a) {nome} está reprovado(a), aguarde a data da prova final!')

        return media

#código principal
boas_vindas('RESULDADO FINAL DAS TRÊS AVALIAÇÕES')

nome = input('Digite seu nome completo: ')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

verifica_nota(nota1, nota2,nota3)
media_arit(nota1, nota2, nota3)
















