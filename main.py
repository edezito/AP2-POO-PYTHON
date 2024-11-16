from funcionalidades.cadastro import Cadastrar, Atualizar, Excluir
from gestaoVendas.pedidos import realizarPedidos
from funcionalidades.consultasdb import consultas_BD, Consultar
from gestaoCliente.app import MenuCliente

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
                                       "\n[3] - SAIR\n"
                                       "Selecione uma opção: "))

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
        menuClientes = MenuCliente(db)
        menuClientes.menuIncial(db)

        

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
