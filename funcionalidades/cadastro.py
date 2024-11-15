from sqlalchemy.orm import Session

from .consultasdb import consultas_BD
from bancoDados.models import Clientes, Itens, Colaborador

class cadastro():
    def cadastro_Cliente(self, db:Session):
        print("Cadastro de Cliente")
        nome = input("Nome: ")
        endereco = input("Endereço: ")
        telefone = input("Telefone: ")

        novo_cliente = Clientes(nome=nome, endereco=endereco, telefone=telefone)

        db.add(novo_cliente)
        db.commit()
        print(f'Cliente {nome} cadastrado com sucesso!')


    def cadastro_Item(self, db: Session):
        print("Cadastro de Item")
        nome = input(("Nome do Produto: "))
        preco = float(input("Preço: "))

        novo_item = Itens(nome=nome, preco=preco)
        db.add(novo_item)
        db.commit()
        print(f'Item {nome} cadastrado com sucesso!')

    def cadastro_Colaborador(self, db: Session):
        print("Cadastro de Colaborador")
        nome = input(("Nome do Colaborador: "))
        telefone = input(("Telefone do Colaborador: "))
        cpf = input(("CPF do Colaborador: "))

        novo_colaborador = Colaborador(nome_colaborador = nome, telefone_colaborador = telefone, cpf_colaborador = cpf)
        db.add(novo_colaborador)
        db.commit()
        print(f'Colaborador {nome} cadastrado com sucesso!')

class Cadastrar:
    def __init__(self):
        self.cadastro = cadastro()

    def cadastrar(self, db: Session):

            while True:
                print("\n" + "=" * 50)
                print("          Escolha uma opção para cadastrar          ")
                print("=" * 50)
                try:
                    opcaoCadastrar = int(input(
                        "[1] - CLIENTE\n"
                        "[2] - ITEM\n"
                        "[3] - COLABORADOR\n"
                        "[4] - SAIR\n"
                    ))

                    if opcaoCadastrar == 1:
                        self.cadastro.cadastro_Cliente(db)
                    elif opcaoCadastrar == 2:
                        self.cadastro.cadastro_Item(db)
                    elif opcaoCadastrar == 3:
                        self.cadastro.cadastro_Colaborador(db)
                    elif opcaoCadastrar == 4:
                        print("Saindo do sistema. Até logo!")
                        break
                    else:
                        print("Opção Incorreta. Tente novamente.")

                except ValueError:
                    print("Entrada inválida, digite um número entre 1 e 3.")   

class cadastroAtualizado():


    def atualizar_Clientes(self, db: Session):
        self.consultaItens = consultas_BD()

        #consultar Clientes
        self.consultaItens.consulta_Clientes(db)

        opc_ID = (input(("\n\033[93mDigite o ID do Cliente que deseja atualizar (ou 0 para cancelar): \033[0m")))
        if opc_ID == "0":
            print("\033[92mOperação de exclusão cancelada pelo usuário.\033[0m")
            return
        
        #CONSULTAR CLIENTE
        atualizar = db.query(Clientes).filter_by(id=int(opc_ID)).first()
        if not atualizar:
            print("\033[91mCliente não encontrado. Verifique o ID e tente novamente.\033[0m")
            return
        
    
        opc_atualizar = int(input("\033[93mDigite a opção desejada: \033[0m\n"
                                  f"[1] - Nome: \n"
                                  f"[2] - Endereço:\n"
                                  f"[3] - Telefone:\n"))
        
        #ATUALIZAR CLIENTES NO BANCO (UPDATE)

        if opc_atualizar == 1:
            novo_nome = input("\033[93mDigite o novo Nome do Cliente: \033[0m")
            atualizar.nome = novo_nome
        elif opc_atualizar == 2:
            novo_endereco = input("\033[93mDigite o novo Endereço do Cliente: \033[0m")
            atualizar.endereco = novo_endereco
        elif opc_atualizar == 3:
            novo_telefone = input("\033[93mDigite o novo Telefone do Cliente: \033[0m")
            atualizar.endereco = novo_telefone

        else:
            print("\033[91mOpção inválida. Por favor, selecione uma opção válida.\033[0m")

        db.commit()
        print("\033[92mCliente atualizado com sucesso.\033[0m")
        

    def atualizar_Itens(self, db: Session):
        self.consultar_Itens = consultas_BD()

        #consultar item
        self.consultar_Itens.consultar_Item(db)

        opc_ID = int(input(("\n\033[93mDigite o ID do Item que deseja atualizar (ou 0 para cancelar): \033[0m")))
        if opc_ID ==0:
            print("\033[92mOperação de exclusão cancelada pelo usuário.\033[0m")
            return
        
        itens = db.query(Itens).filter_by(id=int(opc_ID)).first()

        if not itens:
            print("\033[91mCliente não encontrado. Verifique o ID e tente novamente.\033[0m")
            return
        
    
        opc_atualizar = int(input("\033[93mDigite a opção desejada: \033[0m\n"
                                  f"[1] - Nome: \n"
                                  f"[2] - Preço:\n"))
        
        if opc_atualizar == 1:
            novo_nome = input("\033[93mDigite o novo Nome do Item: \033[0m")
            itens.nome = novo_nome
        elif opc_atualizar == 2:
            novo_preco = input("\033[93mDigite o novo Preço do Item: \033[0m")
            itens.preco = novo_preco

        else:
            print("\033[91mOpção inválida. Por favor, selecione uma opção válida.\033[0m")

        db.commit()
        print("\033[92mItens atualizado com sucesso.\033[0m")

    def atualizar_Colaborador(self, db: Session):
        self.consulta_Coloaborador = consultas_BD()

        #consultar Clientes
        self.consulta_Coloaborador.consulta_Colaborador(db)

        opc_ID = (input(("\n\033[93mDigite o ID do Colaborador que deseja atualizar (ou 0 para cancelar): \033[0m")))
        if opc_ID == "0":
            print("\033[92mOperação de exclusão cancelada pelo usuário.\033[0m")
            return
        
        #CONSULTAR CLIENTE
        colaborador = db.query(Colaborador).filter_by(id=int(opc_ID)).first()
        if not colaborador:
            print("\033[91mColaborador não encontrado. Verifique o ID e tente novamente.\033[0m")
            return
        
    
        opc_atualizar = int(input("\033[93mDigite a opção desejada: \033[0m\n"
                                  f"[1] - Nome: \n"
                                  f"[2] - CPF:\n"
                                  f"[3] - Telefone:\n"))
        
        if opc_atualizar == 1:
            novo_nome = input("\033[93mDigite o novo Nome do Colaborador: \033[0m")
            colaborador.nome_colaborador = novo_nome
        elif opc_atualizar == 2:
            novo_endereco = input("\033[93mDigite o novo CPF do Colaborador: \033[0m")
            colaborador.cpf_colaborador = novo_endereco
        elif opc_atualizar == 3:
            novo_telefone = input("\033[93mDigite o novo Telefone do Colaborador: \033[0m")
            colaborador.telefone_colaborador = novo_telefone

        else:
            print("\033[91mOpção inválida. Por favor, selecione uma opção válida.\033[0m")

        db.commit()
        print("\033[92mCliente atualizado com sucesso.\033[0m")

class Atualizar():
    def __init__(self):
        self.atualizacao = cadastroAtualizado()

    def atualizar(self, db: Session):

            while True:
                print("\n" + "=" * 50)
                print("          Escolha uma opção para atualizar          ")
                print("=" * 50)
                try:
                    opcaoCadastrar = int(input(
                        "[1] - CLIENTE\n"
                        "[2] - ITEM\n"
                        "[3] - COLABORADOR\n"
                        "[4] - SAIR\n"
                    ))

                    if opcaoCadastrar == 1:
                        self.atualizacao.atualizar_Clientes(db)
                    elif opcaoCadastrar == 2:
                        self.atualizacao.atualizar_Itens(db)
                    elif opcaoCadastrar == 3:
                        self.atualizacao.atualizar_Colaborador(db)
                    elif opcaoCadastrar == 4:
                        print("Saindo do sistema. Até logo!")
                        break
                    else:
                        print("Opção Incorreta. Tente novamente.")

                except ValueError:
                    print("Entrada inválida, digite um número entre 1 e 3.")  

class cadastroExcluido():

    def excluir_Cliente(self, db: Session):
        self.consultar_clientes = consultas_BD()

        #consultar clientes
        self.consultar_clientes.consulta_Clientes(db)

        opc_ID = (input(("\n\033[93mDigite o ID do Cliente que deseja excluir (ou 0 para cancelar): \033[0m")))
        if opc_ID == "0":
            print("\033[92mOperação de exclusão cancelada pelo usuário.\033[0m")
            return
        
        cliente_excluido = db.query(Clientes).filter_by(id=int(opc_ID)).first()

        if not cliente_excluido:
            print("\033[91mCliente não encontrado. Verifique o ID e tente novamente.\033[0m")
            return
        
        db.delete(cliente_excluido)
        db.commit()
        print(f"\033[92mCliente do ID {opc_ID} excluído com sucesso.\033[0m")

    def excluir_Item(self, db: Session):
        self.consultar_itens = consultas_BD()
        self.consultar_itens.consultar_Item(db)

        opc_ID = (input(("\n\033[93mDigite o ID do Item que deseja excluir (ou 0 para cancelar): \033[0m")))
        if opc_ID == "0":
            print("\033[92mOperação de exclusão cancelada pelo usuário.\033[0m")
            return
        
        itens_excluidos = db.query(Itens).filter_by(id=int(opc_ID)).first()

        if not itens_excluidos:
            print("\033[91mItem não encontrado. Verifique o ID e tente novamente.\033[0m")
            return
        
        db.delete(itens_excluidos)
        db.commit()
        print(f"\033[92mCliente do ID {opc_ID} excluído com sucesso.\033[0m")

    def excluir_colaborador(self, db: Session):
        self.consultar_colaboradores = consultas_BD
        self.consultar_colaboradores.consulta_Colaborador(db)

        opc_ID = (input(("\n\033[93mDigite o ID do Colaborador que deseja excluir (ou 0 para cancelar): \033[0m")))
        if opc_ID == "0":
            print("\033[92mOperação de exclusão cancelada pelo usuário.\033[0m")
            return
        
        colaborador_exluido = db.query(Colaborador).filter_by(id=int(opc_ID)).first()

        if not colaborador_exluido:
            print("\033[91mColaborador não encontrado. Verifique o ID e tente novamente.\033[0m")
            return
        
        db.delete(colaborador_exluido)
        db.commit()
        print(f"\033[92mColaborador do ID {opc_ID} excluído com sucesso.\033[0m")

class Excluir():
    def __init__(self):
        self.excluir = cadastroExcluido()

    def excluido(self, db: Session):

            while True:
                print("\n" + "=" * 50)
                print("          Escolha uma opção para excluir          ")
                print("=" * 50)
                try:
                    opcaoCadastrar = int(input(
                        "[1] - CLIENTE\n"
                        "[2] - ITEM\n"
                        "[3] - COLABORADOR\n"
                        "[4] - SAIR\n"
                    ))

                    if opcaoCadastrar == 1:
                       self.excluir.excluir_Cliente(db)
                    elif opcaoCadastrar == 2:
                        self.excluir.excluir_Item(db)
                    elif opcaoCadastrar == 3:
                        self.excluir.excluir_colaborador(db)
                    elif opcaoCadastrar == 4:
                        print("Saindo do sistema. Até logo!")
                        break
                    else:
                        print("Opção Incorreta. Tente novamente.")

                except ValueError:
                    print("Entrada inválida, digite um número entre 1 e 3.")  






    