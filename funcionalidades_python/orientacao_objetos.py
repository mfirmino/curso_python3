# self seria o equivalente ao this em Java
# None seria o equivalente ao null em Java
# Atributos privados são definidos por "__" dois underscores, porém não impede de vc acessá-los

#teste de conta
from oo.conta import Conta
conta = Conta(1234, "Valdir", 100.0)
conta.extrato()
conta.deposita(55.0)
conta.extrato()
conta.retira(30.0)
conta.extrato()

#execução de exercício
from oo.datas import Data
d = Data(21,11,2007)
d.formatada()

