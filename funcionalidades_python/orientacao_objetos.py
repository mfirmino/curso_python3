# Adicionamos dois caracteres _ antes e depois do nome da função construtora, para criarmos __init__
# self seria o equivalente ao this em Java
# None seria o equivalente ao null em Java
# Atributos privados são definidos por "__" dois underscores, porém não impede de vc acessá-los
# Melhor forma de fazer getters e setters no python seria colocar o método com o mesmo nome do atributo e utilizar o @property

#teste de conta
from curso_python3.oo.conta import Conta
conta = Conta(1234, "Valdir", 100.0)
conta.extrato()
conta.deposita(55.0)
conta.extrato()
conta.retira(30.0)
conta.extrato()
conta.limite
conta.limite = 10000.0
conta.limite
Conta.codigo_banco

#execução de exercício
from curso_python3.oo.datas import Data
d = Data(21,11,2007)
d.formatada()

#Cliente
from curso_python3.oo.cliente import Cliente
cliente = Cliente("marcelo")
cliente.nome
cliente.nome = "joão"
cliente.nome