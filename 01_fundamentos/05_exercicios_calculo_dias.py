'''
Calcular quantos dias um produto duraria se a pessoa usar X 
porções por dia
'''

total_porcoes = int(input('Quantas porções o produto tem? '))
porcoes_dia = int(input('Quantas você usa por dia? '))

dias = total_porcoes / porcoes_dia

print(f'O produto {dias:.0f} dias!')
# print(f'O produto {int(dias)} dias!')
