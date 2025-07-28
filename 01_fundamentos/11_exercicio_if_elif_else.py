# Verificar notas do aluno
# Introduzindo elif

nota = float(input('Digite sua nota no exame? '))

if nota >= 7 and nota <= 10:
    print('PARABÉNS você foi aprovado.')
elif nota >= 5 and nota < 7:
    print('Você esta de recuperação.')
elif nota <= 4:
    print('Desculpa você foi reprovado!')
else:
    print('Digite uma nota valida')
