lista = []


def listaF():
    while True:
        inserir = input('\nDigite oq deseja inserir: ')
        if inserir != 'sair':
            lista.append(inserir)

        '''for i in lista:
            print(i)'''

        print('------' * 10)

        for i in range(len(lista)):
            print(f'{i} - {lista[i]}')

        if inserir == 'sair':
            break


def dicionarioF():
    pessoasCadastradas = list()
    pessoa = dict()
    soma = 0

    while True:
        pessoa.clear()
        print('-=' * 30)
        pessoa['nome'] = input('Nome: ').upper()

        while True:
            pessoa['sexo'] = input('Sexo: [M/F]: ').upper()[0]
            if pessoa['sexo'] in 'MF':
                break
            print('ERRO! Por favor digite [M] ou [F].')

        pessoa['idade'] = int(input('Idade: '))
        soma += pessoa['idade']
        pessoasCadastradas.append(pessoa.copy())

        while True:
            option = input('Deseja Continuar? [S/N] ').upper()[0]
            if option in 'SN':
                break
            print('ERRO! Por favor digite Sim ou Não.')

        if option == 'N':
            break

    media = soma / len(pessoasCadastradas)

    print('-=' * 30)
    print(f'A) NO TOTAL FORAM CADASTRADAS {len(pessoasCadastradas)} PESSOAS.')
    print(f'B) A MÉDIA DE IDADE É {media:5.2f}')
    print('C) AS MULHERES CADASTRADAS SÃO: ', end='')
    for p in pessoasCadastradas:
        if p['sexo'] == 'F':
            print(f'{p["nome"]}, ', end='')
    print()

    print('D) AS PESSOAS ACIMA DA MÉDIA SÃO: ', end='')
    for p in pessoasCadastradas:
        if p['idade'] >= media:
            print(f'{p["nome"]}, ', end='')
    print()

    print('E) AS PESSOAS ABAIXO DA MÉDIA SÃO: ', end='')
    for p in pessoasCadastradas:
        if p['idade'] < media:
            print(f'{p["nome"]}, ', end='')
    print('\n\n')

    print(f"{'<ENCERRADO>': ^50}")
    print('-=' * 30)


dicionarioF()
