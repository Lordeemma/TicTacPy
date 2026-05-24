def confirmar():
    n = input('')

def continuar():

    print('''
    Deseja continuar? 
    [1] SIM
    [2] NÃO
    ''')

    n = 0
    while n != 1 or n != 2:
        n = int(input(''))
                
        if n == 1:
            return True
        elif n == 2:
            return False
        else:
            print('Opção inválida!')
            b = input('')