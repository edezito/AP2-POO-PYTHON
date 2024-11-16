from funcionalidades.consultasdb import consultas_BD
from gestaoVendas.pedidos import pedidos

from .autenticacao import AutenticacaoCliente
from sqlalchemy.orm import Session

class HistoricoPedidos:
    def __init__(self):
        self.autenticacao = AutenticacaoCliente()
        self.consultar_pedido = consultas_BD()
        self.pedido = pedidos(self.autenticacao)


    def menuInicial(self, db:Session):
        try:
            opcCliente = int(input(
                "[1] - CONSULTAR PEDIDOS\n"
                "[2] - EDITAR PEDIDOS\n"
                "[3] - EXCLUIR PEDIDOS\n"
                "[4] - VOLTAR\n"
            ))
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            return

        if opcCliente in [1, 2, 3]:


                if opcCliente == 1:
                    self.consultar_pedido.consultar_Pedidos(db)
                elif opcCliente == 2:
                    self.pedido.atualizar_Pedidos(db)
                elif opcCliente ==3:
                    self.pedido.excluir_Pedidos(db)
        elif opcCliente == 4:
            print("Voltando ao menu inicial...")
            return
        else:
            print("Opção Inválida, escolha um número entre 1 e 3.")
