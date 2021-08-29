
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

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
            print(f"A palavra secreta era: {palavra_secreta.capitalize()}")
        else:
            print(f"Ainda falta(m) {letras_acertadas.count('_')} letra(s) para completar a palavra secreta")
            print(f"Quantidade de tentativas restantes: {qtd_tentativas - qtd_erros}")

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()