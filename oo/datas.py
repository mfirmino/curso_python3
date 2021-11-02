class Data():

    def __init__(self, dia = "1", mes = "1", ano = "1900"):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        print(f"{self.dia}/{self.mes}/{self.ano}")
