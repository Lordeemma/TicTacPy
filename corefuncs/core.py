def registro_jogada(jogador, posicao, tabuleiro):
    espacos = 'abcdefghi'

    index = espacos.index(posicao)
    y, x = divmod(index, 3)

    if tabuleiro[y][x] == '*':
        tabuleiro[y][x] = jogador
        print('Jogada registrada.')
        return True
    else:
        print('Campo já preenchido!')
        return False

def escolher_jogador_inicio():
    from random import choice as escolha

    pX = 'X'
    pO = 'O'
    resultado = escolha([pX, pO])

    return resultado

def verifica_vencedor(tabuleiro):
    linhas = []

    linhas.extend(tabuleiro)

    for col in range(3):
        linhas.append([
            tabuleiro[0][col],
            tabuleiro[1][col],
            tabuleiro[2][col]
        ])

    linhas.append([
        tabuleiro[0][0],
        tabuleiro[1][1],
        tabuleiro[2][2]
    ])

    linhas.append([
        tabuleiro[0][2],
        tabuleiro[1][1],
        tabuleiro[2][0]
    ])

    for linha in linhas:
        if linha == ['X', 'X', 'X']:
            print('Jogador X é o vencedor!')
            return 'X'

        if linha == ['O', 'O', 'O']:
            print('Jogador O é o vencedor!')
            return 'O'

    if all(campo != '*' for linha in tabuleiro for campo in linha):
        print('EMPATE!')
        return 'empate'

    return None