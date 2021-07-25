print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    print("Você digitou: ", chute_str)
    chute_int = int(chute_str)

    acertou = chute_int == numero_secreto
    maior = chute_int > numero_secreto
    menor = chute_int < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
    else:
        print("Como diria o Fautão: ERRRRROOOOOUUUUUU!")
        if(maior):
            print("O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("O seu chute foi menor do que o número secreto.")
    
    rodada = rodada + 1

print("Fim de jogo.")