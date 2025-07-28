# Igual ou maior que 18 anos de idade é adulto

idade = int(input('Digite sua idade: '))
carteira = False
verificador = idade >= 18 and carteira

print(f'Posso dirigir? {verificador}.')
