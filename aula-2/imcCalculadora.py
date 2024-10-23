

peso = float(input(f'Digite seu peso:'))
altura = float(input(f'Digite sua altura'))

imc = peso / altura ** 2

print(imc)

if imc < 18.5 :
    print(f"Abaixo do peso")
elif imc == 18.5 or imc < 24.9:
    print(f"peso normal")
elif imc < 25 or imc < 29.9:
    print(f"peso normal")
elif imc > 30:
    print(f"obsidade")