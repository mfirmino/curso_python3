# Posicionamento das strings
print("Tentativa {} de {}".format(1, 3))
print("Tentativa {1} de {0}".format(1, 3))

# formatação de floats
print("R$ {}".format(1.59))
print("R$ {:f}".format(1.59))
print("R$ {:f}".format(1.5))
print("R$ {:.2f}".format(1.59))
print("R$ {:.2f}".format(1.5))
print("R$ {:7.2f}".format(1.59))
print("R$ {:7.2f}".format(1234.59))
print("R$ {:07.2f}".format(1.59))
print("R$ {:07d}".format(1))
print("R$ {:07d}".format(321))

# formatação de inteiros
print("Data {}/{}".format(9,4))
print("Data {}/{}".format(19,12))
print("Data {:02d}/{:02d}".format(9,4))


# python 3.6+
nome = "Marcelo Firmino"
print(f"Meu nome é {nome}")
print(f"Meu nome é {nome.lower()}")

