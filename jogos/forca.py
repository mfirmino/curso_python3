
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra ?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f"encontrei a letra {chute} na posição {index}")
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)
        print(f"Ainda falta(m) {letras_acertadas.count('_')} letra(s) para completar a palavra secreta")

    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()