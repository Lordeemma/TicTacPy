def registro_jogada(jogador, posicao, lista):
    espacos = [['a', 'b', 'c'],
               ['d', 'e', 'f'],
               ['g', 'h', 'i']]

    for y in range(len(lista)):
        for x in range(len(lista)):

            if posicao == espacos[y][x]:

                if lista[y][x] == '*':
                    lista[y][x] = jogador
                    print('Jogada registrada.')
                    return True
                else:
                    print('Campo já preenchido!')
                    return False

    return False

def escolher_jogador_inicio():
    from random import choice as escolha

    pX = 'X'
    pO = 'O'
    resultado = escolha([pX, pO])

    return resultado

def verifica_vencedor(jogadorO, jogadorX, lista):
    comb = ''
    vitoria = ''

    for y in range(len(lista)):
        if (comb == 'XXX') or (comb == 'OOO'):
            vitoria = comb
            break
        else:
            comb = ''

            for x in range(len(lista)):
                comb += lista[y][x]
        
    for x in range(len(lista)):
        if (comb == 'XXX') or (comb == 'OOO'):
            vitoria = comb
            break
        else:
            comb = ''
            
            for y in range(len(lista)):
                comb += lista[y][x]
    
    if (comb == 'XXX') or (comb == 'OOO'):
        vitoria = comb
    else:
        comb = ''
        
    comb += lista[0][0]
    comb += lista[1][1]
    comb += lista[2][2]

    if (comb == 'XXX') or (comb == 'OOO'):
        vitoria = comb
    else:
        comb = ''

    comb += lista[0][2]
    comb += lista[1][1]
    comb += lista[2][0]

    if (comb == 'XXX') or (comb == 'OOO'):
        vitoria = comb
    else:
        comb = ''
    
    if vitoria == 'XXX':
        print('Jogador X é o vencedor!')
    elif vitoria == 'OOO':
        print('Jogador O é o vencedor!')
    elif vitoria == '' and (jogadorO == 5 and jogadorX == 4) or (jogadorO == 4 and jogadorX == 5):
        print('EMPATE!')
        return 'empate'

    return vitoria