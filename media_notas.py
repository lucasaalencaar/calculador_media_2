#Sitemas de notas do Suap
nome = input('Nome do aluno: ')
print('-----Média de notas do suap-----')
nota1 = float(input('digite sua primeira nota:' ))
nota2 = float(input('digite sua segunda nota: '))
nota3 = float(input('Digite sua terceira nota: '))

#validação das notas
if nota1 and nota2 and nota3 >= 0:
    print('Notas válidas!')
else:
    print('Notas inválidas! Por favor digite novamente.')

#calcular média
media = (nota1 + nota2 +nota3)/3
print(f'Sua média final foi: {media}')
if media >= 70:
    print(f'O aluno, {nome} está aprovado!')
else:
    print(f'O aluno {nome}, está reprovado...')
