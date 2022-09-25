#Commit no github 'demo for git commit and push'
#outra coisa
lista = []

def lista1():
    while True:
        inserir = input('Digite oq deseja inserir: ')
        lista.append(inserir)

        for i in range(0, len(lista)):
            print(lista[i])
        
        if inserir == 'sair':
            break


lista1()