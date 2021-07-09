print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

print("Você digitou: ", chute_str)

chute_int = int(chute_str)

if(numero_secreto == chute_int):
    print("Parabéns! Você acertou!")
else:
    print("Como diria o Fautão: ERRRRROOOOOUUUUUU!")

print("Fim de jogo.")