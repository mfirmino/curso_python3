
import random

def jogar():

    imprime_msg_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    qtd_tentativas = 7
    qtd_erros = 0

    while(not enforcou and not acertou):

        chute = captura_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, letras_acertadas, chute)
        else:
            qtd_erros += 1
            desenha_forca(qtd_erros)

        enforcou = qtd_erros == qtd_tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            imprime_mensagem_ganhador()
        elif(enforcou):
            imprime_mensagem_perdedor()
        else:
            imprime_mensagem_status(letras_acertadas, qtd_tentativas, qtd_erros)

    imprime_mensagem_final(palavra_secreta)

def imprime_mensagem_ganhador():
    print("Parabéns !!! Você Ganhou !!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor():
    print("Infelizmente você perdeu ... ")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_final(palavra_secreta):
    print(f"A palavra secreta era: {palavra_secreta.capitalize()}")
    print("Fim de jogo.")

def imprime_mensagem_status(letras_acertadas, qtd_tentativas, qtd_erros):
    print(f"Ainda falta(m) {letras_acertadas.count('_')} letra(s) para completar a palavra secreta")
    print(f"Quantidade de tentativas restantes: {qtd_tentativas - qtd_erros}")

def marca_chute_correto(palavra_secreta, letras_acertadas, chute):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            print(f"encontrei a letra {chute} na posição {index}")
            letras_acertadas[index] = letra
        index += 1

def captura_chute():
    chute = input("Qual letra ?")
    chute = chute.strip().upper()
    return chute

def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def imprime_msg_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta(nome_arquivo="curso_python3/jogos/palavras.txt"):
    with open(nome_arquivo, 'r') as arquivo:
        palavras = []

        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta

if(__name__ == "__main__"):
    jogar()