from .autenticacao import AutenticacaoCliente
from gestaoVendas.pedidos import pedidos
from .historicoPedidos import HistoricoPedidos
from .fidelidade import programaFidelidade

from sqlalchemy.orm import Session

class MenuCliente:
    def __init__(self, db: Session):
        self.autenticacao = AutenticacaoCliente()
        self.pedidos = pedidos(self.autenticacao)
        self.historico_pedidos = HistoricoPedidos()
        self.programa_fidelidade = programaFidelidade(self.autenticacao)

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
                    self.historico_pedidos.menuInicial(db)
                elif opcCliente ==3:
                    self.programa_fidelidade.associarPontos(db)
        elif opcCliente == 4:
            print("Voltando ao menu inicial...")
            return
        else:
            print("Opção Inválida, escolha um número entre 1 e 3.")



        

