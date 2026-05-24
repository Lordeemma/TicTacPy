def criar_tabuleiro(malha):
    print('=' * 10, f'{' TABULEIRO ':^14}', '=' * 10)
    print('=' * 10, f'{' COORDENADAS ':^14}', '=' * 10)
    print(f'{' a | b | c ':^36}')
    print(f'{'---|---|---':^36}')
    print(f'{' d | e | f ':^36}')
    print(f'{'---|---|---':^36}')
    print(f'{' g | h | i ':^36}')
    print('')

    for y in range(3):
        print(' ' * 11, end=' ')
        for x in range(3):

            if x < 2:
                print(f'{f' {malha[y][x]} '}', end='|')
            else:
                print(f'{f' {malha[y][x]} '}')

        if y < 2:
            print(f'{'---|---|---':^36}')

def tela_inicial():
    from time import sleep

    print("\033[H\033[J", end="")
    print('=' * 10, f'{"JOGO DA VELHA":^14}', '=' * 10)
    print('')
    sleep(1)
    msg = 'BEM-VINDO AO JOGO'
    print(' ' * 10, end='')
    for i in range(len(msg)):
        print(f'{msg[i]:^}', end='', flush=True)
        sleep(0.1)
    sleep(1.5)

def limpa_tela():
    print("\033[H\033[J", end="")