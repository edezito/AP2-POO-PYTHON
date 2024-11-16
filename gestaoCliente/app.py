from .autenticacao import autenticacaoCliente
from gestaoVendas.pedidos import realizarPedidos

from sqlalchemy.orm import Session

class MenuCliente:
    def __init__(self, db: Session):
        self.autenticacao = autenticacaoCliente()
        self.pedidos = realizarPedidos()

    def menuIncial(self, db: Session):
        self.autenticacao.autenticar(db)

        try:
            opcCliente = int(input(
                "[1] - REALIZAR PEDIDO\n"
                "[2] - HISTÓRICO DE PEDIDOS\n"
                "[3] - PROGRAMA DE FIDELIDADE\n"
                "[4] - VOLTAR\n"
            ))
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            return

        if opcCliente in [1, 2, 3]:


                if opcCliente == 1:
                    self.pedidos.realizar_Pedido(db)
                elif opcCliente == 2:
                    print("Histórico")
                elif opcCliente ==3:
                    print("Fidelidade")
        elif opcCliente == 4:
            print("Voltando ao menu inicial...")
            return
        else:
            print("Opção Inválida, escolha um número entre 1 e 3.")



        

