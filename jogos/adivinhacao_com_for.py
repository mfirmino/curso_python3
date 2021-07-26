import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade ?")
    print("(1) Fácil - (2) Médio - (3) Difícil")

    nivel_int = int(input("Defina o nível: "))

    if nivel_int == 1:
        total_de_tentativas = 20
    elif nivel_int == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute_int = int(chute_str)

        if(chute_int < 1 or chute_int > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if acertou:
            print("Parabéns! Você acertou!")
            print(f"Sua pontuação final foi de {pontos}")
            break
        else:
            print("Como diria o Faustão: ERRRRROOOOOUUUUUU!")
            if maior:
                print("O seu chute foi maior do que o número secreto.")
            elif menor:
                print("O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

    print(f"O número secreto era {numero_secreto}")
    print("Fim de jogo.")