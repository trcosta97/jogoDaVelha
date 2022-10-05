from functions import *

# THIAGO RIBEIRO DA COSTA
# RM92800

matriz = inicializarTabuleiro()
contador = 9
player1 = 'X'
player2 = 'O'
pontos1 = 0
pontos2 = 0

escolhaJogador = imprimeMenuPrincipal()

if escolhaJogador == 1:
    print("Bem vindo ao Jogo da Velha! Os jogadores devem alternar entre si as jogadas."
          "\nEm cada jogada você deve escolher o número da LINHA e depois da COLUNA de"
          "\nonde deseja jogar.O jogador 1 será representado por X e o jogador 2 por O."
          "\nLembrando que jogo da velha é um jogo sobre atenção, então se você entrar uma"
          "\nlinha oucoluna inexistente, ou uma casa já ocupada, você PERDERÁ a vez.")
    contador = 0
elif escolhaJogador == 2:
    print("Opção ainda não implementada. Reinicie o programa para jogar.")
else:
    print("Entrada inválida. Reinicie o programa para jogar.")

print()

while verificaVelha(contador):

    # VEZ DO JOGADOR 1
    coordenadas = jogar(matriz)

    if posicaoValida(coordenadas[0], coordenadas[1], matriz):
        jogaJogador(matriz, coordenadas[0], coordenadas[1], player1)
        contador += 1
        if verificaVencedor(matriz):
            pontos1 += 1
            if reiniciar():
                matriz = inicializarTabuleiro()
                contador = 0
            else:
                break
    else:
        print("Posição inválida, você perdeu a vez.")
        continue


    # VEZ DO JOGADOR 2
    coordenadas = jogar(matriz)

    if posicaoValida(coordenadas[0], coordenadas[1], matriz):
        jogaJogador(matriz, coordenadas[0], coordenadas[1], player2)
        contador += 1
        if verificaVencedor(matriz):
            pontos2 += 1
            if reiniciar():
                matriz = inicializarTabuleiro()
                contador = 0
            else:
                break
    else:
        print("Posição inválida, você perdeu a vez.")
        continue

imprimePontuacao(pontos1, pontos2)



