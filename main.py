from corefuncs import core, inputs, screens

screens.tela_inicial()

jogadorO = jogadorX = 0
malha = [['*', '*', '*'],
         ['*', '*', '*'],
         ['*', '*', '*']]

jogador = core.escolher_jogador_inicio()

while True:
    if jogadorO >= 3 or jogadorX >= 3:
        screens.limpa_tela()
        screens.criar_tabuleiro(malha)

        resultado = core.verifica_vencedor(malha)

        if resultado != None:
            inputs.confirmar()
                
            if inputs.continuar():
                jogadorO = jogadorX = 0
                malha = [['*', '*', '*'],
                         ['*', '*', '*'],
                         ['*', '*', '*']]
                jogador = core.escolher_jogador_inicio()
                continue
            else:
                screens.limpa_tela()
                break

    screens.limpa_tela()
    screens.criar_tabuleiro(malha)

    pos = str(input(f'Vez do jogador {jogador}! Digite a posição que deseja marcar: ')).strip().lower()

    if len(pos) == 1 and pos in 'abcdefghi':
        sucesso = core.registro_jogada(jogador, pos, malha)

        if not sucesso:
            inputs.confirmar()
            continue
        else:
            inputs.confirmar()

            if jogador == 'X':
                jogadorX += 1
                jogador = 'O'
                continue
            if jogador == 'O':
                jogadorO += 1
                jogador = 'X'
                continue
    else:
        print('Posição inválida!')
        inputs.confirmar()



