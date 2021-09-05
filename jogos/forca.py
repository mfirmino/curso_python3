
import random

def jogar():
    imprime_msg_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = carrega_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    qtd_tentativas = 6
    qtd_erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra ?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    print(f"encontrei a letra {chute} na posição {index}")
                    letras_acertadas[index] = letra
                index += 1
        else:
            qtd_erros += 1

        enforcou = qtd_erros == qtd_tentativas
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        if(acertou):
            print("Parabéns !!! Você Ganhou !!!!")
        elif(enforcou):
            print("Infelizmente você perdeu ... ")
        else:
            print(f"Ainda falta(m) {letras_acertadas.count('_')} letra(s) para completar a palavra secreta")
            print(f"Quantidade de tentativas restantes: {qtd_tentativas - qtd_erros}")

    print(f"A palavra secreta era: {palavra_secreta.capitalize()}")
    print("Fim de jogo.")

def carrega_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]

def imprime_msg_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    with open('palavras.txt', 'r') as arquivo:
        palavras = []

        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta

if(__name__ == "__main__"):
    jogar()