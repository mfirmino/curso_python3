import forca
import adivinhacao_com_for
from forca import jogar


print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca - (2) Adivinhação")
jogo = int(input("Qual será o jogo: "))

if jogo == 1:
    print("Jogando forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando adivinhação")
    adivinhacao_com_for.jogar()
