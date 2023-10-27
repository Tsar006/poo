tabuleiro = [ '', '', '', 
              '', '', '',
              '', '', '']
def mostrar_tabuleiro():
    tabuleiro_montado = []
    linha_montado = []
    contador = 1
    for casa in tabuleiro:
        
        if contador % 3 == 0: 
            linha_montado.append(casa)
            tabuleiro_montado.append(linha_montado)
            linha_montado = []
        else: 
            linha_montado.append(casa)
        contador += 1

    for linha in tabuleiro_montado:
        for item in linha:
            print(f"| {item} |", end='' )
        print('')

def limpa_tabuleiro():
    for item in range(len(tabuleiro)):
        tabuleiro[item] = ''


def menu():
    print("---MENU PRINCIPAL----------")
    print("|1 - jogar                 |")
    print("|2 - creditos              |")
    print("|0 - Sair                  |")
    print('')
    escolha = input("escolha uma das opçoes acima: ")
    return escolha

def jogador_joga(num_jogador,jogada):
    jogada = int(jogada)
    if num_jogador == 1:
        tabuleiro[jogada] = 'x'
    else:
        tabuleiro[jogada] = 'O'

def verifica_local_jogado(num_casa):
    if tabuleiro[num_casa] != '':
        print("casa já ocupada")
        return 0
    else:
        return 1


def checar_ganho():
    if (tabuleiro[0] ==  tabuleiro[3] ==  tabuleiro[6] != '') or (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != '') or (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != ''):
        return 1
    elif (tabuleiro[0] ==  tabuleiro[1] == tabuleiro[2] != '') or (tabuleiro[3] and tabuleiro[4] == tabuleiro[5] != '' ) or (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != ''):
        return 1
    elif (tabuleiro[0] ==  tabuleiro[4] == tabuleiro[8] != '') or (tabuleiro[2] and tabuleiro[4] == tabuleiro[6] != ''):
        return 1
    else: 
        return 0
    
def iniciar_jogo():
    contador_vez = 0
    while True:
        if contador_vez % 2 == 0:
            lugar_jogar = int(input("vez do jogador 1, digite o numero da casa onde irá inserir o X: "))
            validade = verifica_local_jogado(lugar_jogar)
            if validade == 1:
                jogador_joga(1,lugar_jogar)
                mostrar_tabuleiro()
                teste = checar_ganho()
                if teste == 1:
                    print("jogador 1 venceu! \n fim de jogo")
                    limpa_tabuleiro()
                    break
                else:
                    pass
            else:
                contador_vez -= 1
            contador_vez += 1

        elif contador_vez % 2 != 0: 
            lugar_jogar = int(input("vez do jogador 2, digite o numero da casa onde irá inserir a O: "))
            validade = verifica_local_jogado(lugar_jogar)
            if validade == 1:
                jogador_joga(2,lugar_jogar)
                mostrar_tabuleiro()
                teste = checar_ganho()
                if teste == 1:
                    print("jogador 2 venceu! \n fim de jogo")
                    limpa_tabuleiro()
                    break
                else: 
                    pass
            else:
                contador_vez -= 1
            contador_vez += 1
        else:
            pass
        











while True:
    escolha_opção = menu()
    if escolha_opção == '1':
        iniciar_jogo()

    elif escolha_opção == '2': 
        pass

