#Tipo numeroa
primeiroNumero = int(input(f'Digite o primeiro numero'))

segundoNumero = int(input(f'Digite o segundo numero'))

if primeiroNumero > segundoNumero:
    print(f"{primeiroNumero} é maior do que {segundoNumero}")
if segundoNumero > primeiroNumero:
    print(f"{segundoNumero} é maior do que {primeiroNumero}")
elif primeiroNumero == segundoNumero:
    print("numeors iguais")