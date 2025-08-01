
# Introdução a for/while
# Estrutura de repetição

"""
for -> Quando eu sei a quantidade 
de vezes que preciso repetir
"""

# for i in range(11):
#     print(i)

"""
while -> Qaundo eu nao sei a quantidade
de vezes que preciso executar, 
vai depender de uma condição
"""

# i = 0
# while i <= 20:
#     print(i)
#     i += 1


senha = ''
cont = 0
while senha != '123':
    senha = input('Qual é a senha do sistema? ')
    cont += 1
print(f'Voce digitou {cont}')
print('Acesso liberado.')
