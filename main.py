from funcionalidades.cadastro import Cadastrar, Atualizar, Excluir
from funcionalidades.pedidos import realizarPedidos
from funcionalidades.consultasdb import consultas_BD, Consultar
from sqlalchemy.orm import Session
from config import get_db

db = Session

class Main():
    def __init__(self, db):
        self.db = db

    def menuIncial(self, db: Session):
        print("=" * 50)
        print("       Tech-Fruti      ")
        print("=" * 50)

        while True:
            try:
                opcEntrada = int(input("\nEscolha uma opção:"
                                       "\n[1] - CLIENTE"
                                       "\n[2] - COLABORADOR"
                                       "\n[3] - SAIR\n"))

                if opcEntrada == 1:
                    self.menu_cliente(db)
                elif opcEntrada == 2:
                    self.menu_colaborador(db)
                elif opcEntrada == 3:
                    print("Saindo do sistema. Até logo!")
                    break
                else:
                    print("Opção Inválida, escolha um número entre 1 e 3.")
            except ValueError:
                print("Entrada inválida, por favor digite um número.")

    def menu_cliente(self, db: Session):
        print("\n                  CLIENTE                  ")
        print("=" * 50)


        #SELECIONAR OPÇÕES

        try:
            opcCliente = int(input(
                "[1] - REALIZAR PEDIDO\n"
                "[2] - CONSULTAR PEDIDOS\n"
                "[3] - EXCLUIR PEDIDOS\n"
                "[4] - ATUALIZAR PEDIDOS\n"
                "[5] - VOLTAR\n"
            ))
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            return

        if opcCliente in [1, 2, 3, 4]:
                pedidos = realizarPedidos()
                consultas = consultas_BD()

                if opcCliente == 1:
                    pedidos.realizar_Pedido(db)
                elif opcCliente == 2:
                    consultas.consultar_Pedidos(db)
                elif opcCliente ==3:
                    pedidos.excluir_Pedidos(db)
                elif opcCliente ==4:
                    pedidos.atualizar_Pedidos(db)
        elif opcCliente == 4:
            print("Voltando ao menu inicial...")
            return
        else:
            print("Opção Inválida, escolha um número entre 1 e 3.")

    def menu_colaborador(self, db: Session):
        print("\n                  EMPRESA                  ")
        print("=" * 50)

        #SELECIONAR OPÇÕES

        try:
            opcColaborador = int(input(
                "[1] - CADASTRAR\n"
                "[2] - ATUALIZAR CADASTROS\n"
                "[3] - EXCLUIR CADASTROS\n"
                "[4] - CONSULTAR\n"
                "[4] - VOLTAR\n"
            ))
        except ValueError:
            print("Entrada inválida, por favor digite um número.")
            return

        if opcColaborador == 1:
            cadastros = Cadastrar()
            cadastros.cadastrar(db)
        elif opcColaborador == 2:
            atualizar = Atualizar()
            atualizar.atualizar(db)
        elif opcColaborador == 3:
            excluir = Excluir()
            excluir.excluido(db)
        elif opcColaborador == 4:
            consulta = Consultar()
            consulta.consulta(db)
            return
        else:
            print("Opção Inválida, escolha um número entre 1 e 3.")

               
db_session = next(get_db())  # Obtendo a sessão

sistema_Gerenciamento = Main(db_session)
sistema_Gerenciamento.menuIncial(db_session)
