tabuleiro = [ '', '', '', 
              '', '', '',
              '', '', '']
placar = {}
pontos_um = 0
pontos_dois = 0
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

############ tratamento de erros
def testa_erro(nome):
    #não numero
    try:
        nome = int(nome)
        if nome > 9 or nome < 1:
            print("tente novamente e digite um numero entre 1 e 9")
            return 1
        else:
            return 0
    except:
        print('Caractere não aceito! tente novamente. ')
        return 1

#boa sorte mozinho<3

def mostrar_placar():
    for nome, pontos in placar.items():
        print("_______________")
        print(f"{nome}| {pontos}", end = '|')
        print("")
##############json
import json

def adicionar_jogador(nome, pontos):
    # Se o nome já existe no placar, atualizar sua pontuação
    if nome in placar:
        placar[nome] += pontos
    else:
        placar[nome] = pontos

# Função para salvar o placar em um arquivo json
def salvar_placar():
    with open("placar.json", "w") as arquivo:
        string_json = json.dumps(placar)
        arquivo.write(string_json)

def carregar_placar():
    with open("placar.json", "r") as arquivo:
        placar = json.load(arquivo)
    return placar

adicionar_jogador("Antonia", 10) 
adicionar_jogador("Thiago", 5)
adicionar_jogador("Antonia", 5)
salvar_placar() 

def salvar_carregar(opcao):
    if opcao == "salvar":
        jogador_um_nome = input("digite o nome do jogador um: ")
        jogador_dois_nome = input("digite o nome do jogador dois: ")
        adicionar_jogador(jogador_um_nome, pontos_um)
        adicionar_jogador(jogador_dois_nome,pontos_dois)
        salvar_placar()
    elif opcao == "carregar":
        carregar_placar()


def checar_ganho():
    if (tabuleiro[0] ==  tabuleiro[3] ==  tabuleiro[6] != '') or (tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != '') or (tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != ''):
        return 1
    elif (tabuleiro[0] ==  tabuleiro[1] == tabuleiro[2] != '') or (tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != '' ) or (tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != ''):
        return 1
    elif (tabuleiro[0] ==  tabuleiro[4] == tabuleiro[8] != '') or (tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ''):
        return 1
    else: 
        return 0

def empate():
    if all(casa != '' for casa in tabuleiro):
        print("empate")
        return 1


def iniciar_jogo():
    contador_vez = 0
    while True:
        if contador_vez % 2 == 0:
            lugar_jogar = input("vez do jogador 1, digite o numero da casa, entre 1 e 9 onde irá inserir o X: ")
            erro = testa_erro(lugar_jogar)
            if erro == 1:
                continue
            elif erro != 1:
                lugar_jogar = int(lugar_jogar) - 1
                pass
            validade = verifica_local_jogado(lugar_jogar)
            if validade == 1:
                jogador_joga(1,lugar_jogar)
                mostrar_tabuleiro()
                teste = checar_ganho()
                if teste == 1:
                    print("jogador 1 venceu! \n fim de jogo")
                    global pontos_um
                    pontos_um += 1
                    mostrar_placar()
                    limpa_tabuleiro()
                    break
                else:
                    empate_teste = empate()
                    if empate_teste == 1:
                        break

            else:
                contador_vez -= 1
            contador_vez += 1

        elif contador_vez % 2 != 0: 
            lugar_jogar = input("vez do jogador 2, digite o numero da casa, entre 1 e 9, onde irá inserir a O: ")
            erro = testa_erro(lugar_jogar)
            if erro == 1:
                continue
            elif erro != 1:
                lugar_jogar = int(lugar_jogar) - 1
                pass
            validade = verifica_local_jogado(lugar_jogar)
            if validade == 1:
                jogador_joga(2,lugar_jogar)
                mostrar_tabuleiro()
                teste = checar_ganho()
                if teste == 1:
                    print("jogador 2 venceu! \n fim de jogo")
                    global pontos_dois
                    pontos_dois += 1
                    limpa_tabuleiro()
                    break
                else:
                    empate_teste = empate()
                    if empate_teste == 1:
                        break
            else:
                contador_vez -= 1
            contador_vez += 1
        else:
            pass
        











def equipe():
    print('Equipe de desenvolvimento: \n - Antonia Vitória - \n - Thiago Andrade -')


def menu():
    print("---MENU PRINCIPAL----------")
    print("|1 - jogar                 |")
    print("|2 - creditos              |")
    print("|3 - salvar/carregar       |")
    print("|4 - mostrar placar        |")
    print("|0 - Sair                  |")
    print('')
    escolha = input("escolha uma das opçoes acima: ")
    return escolha



while True:
    escolha_opção = menu()
    if escolha_opção == '1':
        iniciar_jogo()
    elif escolha_opção == '2': 
        equipe()
    elif escolha_opção == '3':
        escolha = input("digite 'salvar' para salvar e 'carregar' para carregar: ")
        salvar_carregar(escolha)
    elif escolha_opção == '4':
        mostrar_placar()
    elif escolha_opção == '0':
        print("encerrando")
        break
    else:
        print('Esta opção não existe!')
