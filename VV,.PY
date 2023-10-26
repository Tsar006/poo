import os

file_name = "placar.txt"

def ler_placar():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            placar = file.read().split()
            jogador_x_vitorias = int(placar[0])
            jogador_o_vitorias = int(placar[1])
    else:
        jogador_x_vitorias = 0
        jogador_o_vitorias = 0
    return jogador_x_vitorias, jogador_o_vitorias

def zerar_placar():
    with open(file_name, 'w') as file:
        file.write("0 0")

def exibir_tabuleiro(tabuleiro):
    for row in tabuleiro:
        print("|".join(row))
        print("-----")

def verificar_vencedor(tabuleiro, jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

def exibir_placar_detalhado(jogador_x_vitorias, jogador_o_vitorias):
    print("Placar Detalhado:")
    print(f"Jogador X - Vitórias: {jogador_x_vitorias}")
    print(f"Jogador O - Vitórias: {jogador_o_vitorias}")

def sobre_equipe():
    print("Equipe:")
    print("- Ângelo Rian")
    print("- Pedro P. Sousa")

def jogo_da_velha():
    jogador_x_vitorias, jogador_o_vitorias = ler_placar()

    while True:
        tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        jogador_atual = "X"

        while True:
            exibir_tabuleiro(tabuleiro)
            posicao = input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")

            if not posicao.isdigit():
                print("Entrada inválida. Digite um número de 1 a 9.")
                continue

            posicao = int(posicao)
            if posicao < 1 or posicao > 9:
                print("Posição fora do intervalo permitido. Escolha um número entre 1 e 9.")
                continue

            x, y = (posicao - 1) // 3, (posicao - 1) % 3

            if tabuleiro[x][y] != " ":
                print("Posição já preenchida. Tente novamente.")
                continue

            tabuleiro[x][y] = jogador_atual

            if verificar_vencedor(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                if jogador_atual == "X":
                    jogador_x_vitorias += 1
                else:
                    jogador_o_vitorias += 1
                break

            if all([celula != " " for row in tabuleiro for celula in row]):
                exibir_tabuleiro(tabuleiro)
                print("Empate!")
                break

            jogador_atual = "O" if jogador_atual == "X" else "X"

        with open(file_name, 'w') as file:
            file.write(f"{jogador_x_vitorias} {jogador_o_vitorias}")

        while True:
            reiniciar = input("Deseja jogar novamente? (s/n): ").lower()
            if reiniciar == "s":
                break
            elif reiniciar == "n":
                exibir_placar_detalhado(jogador_x_vitorias, jogador_o_vitorias)
                return
            else:
                print("Entrada inválida. Digite 's' para sim ou 'n' para não.")

jogador_x_vitorias, jogador_o_vitorias = ler_placar()
exibir_placar_detalhado(jogador_x_vitorias, jogador_o_vitorias)

while True:
    print("Menu Principal:")
    print("1. Jogar")
    print("2. Zerar Placar")
    print("3. Sair")
    print("4. Sobre")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        jogo_da_velha()
    elif escolha == "2":
        zerar_placar()
        print("Placar zerado.")
    elif escolha == "3":
        print("Obrigado por jogar! Adeus.")
        break
    elif escolha == "4":
        sobre_equipe()
    else:
        print("Opção inválida. Escolha novamente.")
