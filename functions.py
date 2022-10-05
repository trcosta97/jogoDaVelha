def inicializarTabuleiro():
    tabuleiro = []
    for i in range(3):
        linha = []
        for x in range(3):
            linha.append("-")
        tabuleiro.append(linha)
    return tabuleiro

def imprimirTabuleiro(matrix):
    print("   0     1     2")
    print('0  ' + matrix[0][0] + '  |  ' + matrix[0][1] + '  |  ' + matrix[0][2])
    print('-------------------')
    print('1  ' + matrix[1][0] + '  |  ' + matrix[1][1] + '  |  ' + matrix[1][2])
    print('-------------------')
    print('2  ' + matrix[2][0] + '  |  ' + matrix[2][1] + '  |  ' + matrix[2][2])

def leiaCoordenadaLinha():
    linha = int(input('\nEscolha a linha: '))
    return linha

def leiaCoordenadaColuna():
    coluna = int(input('Escolha a coluna: '))
    return coluna


def posicaoValida(linha, coluna, matriz):
    if linha in range(0, 3) and coluna in range(0, 3) and matriz[linha][coluna] == '-':
        return True
    else:
        return False

def jogarNovamente():
    restart = input("Quer jogar outra vez? (s/n)").capitalize()
    if restart == 'S':
        return True
    else:
        print("Obrigado por jogar")
        return False

def verificaVencedor(matriz):
    vitoria = None

    for linha in range(0,3):
        if(matriz[linha][0] == matriz[linha][1] == matriz[linha][2] == 'X'):
            print("\nO jogador 1 venceu!\n")
            vitoria = True
            break
        elif(matriz[linha][0] == matriz[linha][1] == matriz[linha][2] == 'O'):
            print("\nO jogador 2 venceu!\n")
            vitoria = True
            break

    for coluna in range(0,3):
        if(matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna] == 'X'):
            print("\nO jogador 1 venceu!\n")
            vitoria = True
            break
        if (matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna] == 'O'):
            print("\nO jogador 2 venceu!\n")
            vitoria = True
            break

    if matriz[0][0] == matriz[1][1] == matriz[2][2] == 'X':
        print("\nO jogador 1 venceu!\n")
        vitoria = True


    elif matriz[0][0] == matriz[1][1] == matriz[2][2] == 'O':
        vitoria = True
        print("O jogador 2 venceu!")

    elif matriz[0][2] == matriz[1][1] == matriz[2][0] == 'X':
        vitoria = True
        print("O jogador 1 venceu!")

    elif matriz[0][2] == matriz[1][1] == matriz[2][0] == 'O':
        vitoria = True
        print("O jogador 2 venceu!")

    return vitoria

def verificaVelha(contador):
    rodadasFaltantes = 9 - contador
    if contador <= 8:
        print(f"\nFaltam {rodadasFaltantes} rodadas até dar velha")
        return True
    else:
        return False

def imprimePontuacao(player1, player2):
    print('-_-_-_- PONTUAÇÃO -_-_-_-')
    print(f'Jogador 1 fez {player1} pontos')
    print(f'Jogador 2 fez {player2} pontos')

def reiniciar():
    escolha = input(print("\nDeseja jogar novamente? (S/N) ")).capitalize()
    if escolha == 'S':
        return True
    elif escolha == 'N':
        return False
    else:
        print("Entrada inválida. Jogo encerrado.")
        return False

def jogar(matriz):
    imprimirTabuleiro(matriz)
    linha = leiaCoordenadaLinha()
    coluna = leiaCoordenadaColuna()
    coordenadas = (linha, coluna)
    return coordenadas

def imprimeMenuPrincipal():
    entrada = int(input("Bem vindo ao JOGO DA VELHA.\nDigite o número do modo que você deseja jogar:\n(1) PvP\n(2) PvE\n"))
    return entrada

def jogaJogador(matriz, linha, coluna, player):
    matriz[linha][coluna] = player



