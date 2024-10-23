notaAluno = int(input(f'Digite uma nota de 0 a 10'))

if notaAluno == 0 or notaAluno == 10:
    print(f"Nota salva!")
else:
    notaAluno = int(input("Nota invalida, digite novamente a nota."))
