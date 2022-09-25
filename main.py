lista = []

def lista1():
    while True:
        inserir = input('Digite oq deseja inserir: ')
        lista.append(inserir)

        for i in range(0, len(lista)):
            print(lista[i])
        
        if inserir == 'sair':
            break


def lista2():
    while True:
        inserir = input('Digite oq deseja inserir: ')
        lista.append(inserir)

        print(lista[0:])

        if inserir == 'sair':
            break


lista2()