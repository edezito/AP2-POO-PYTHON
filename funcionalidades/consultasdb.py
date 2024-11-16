from sqlalchemy.orm import Session
from bancoDados.models import Pedido, Item, Cliente, Colaborador

class consultas_BD():

    def consultar_Item(self, db: Session):
        itens_cadastrados = db.query(Item).all()
        
        if not itens_cadastrados:
            print("\033[91mNão há produtos disponíveis no momento. Operação cancelada.\033[0m")
            return False
        
        print("\033[96m=== Lista de Produtos Disponíveis ===\033[0m")
        for item in itens_cadastrados:
            print(f'\033[92mID: {item.id}\033[0m')
            print(f'\033[92mNome: {item.nome}\033[0m')
            print(f'\033[92mPreço: {item.preco:.2f}\033[0m')
        return True

    def consultar_Pedidos(self, db: Session):
        while True:
            print("\n\033[94m===== Consulta de Pedidos =====\033[0m")
            nome_cliente = input("\033[94mDigite seu nome (ou digite 'sair' para encerrar): \033[0m").strip()

            if nome_cliente.lower() == 'sair':
                print("\033[92mEncerrando a consulta de pedidos. Obrigado!\033[0m")
                break

            if not nome_cliente:
                print("\033[91mO nome do cliente não pode estar vazio. Tente novamente.\033[0m")
                continue

            cliente = db.query(Cliente).filter(Cliente.nome.ilike(f"%{nome_cliente}%")).first()

            if not cliente:
                print(f"\033[91mNão encontramos um cliente com o nome {nome_cliente}. Tente novamente.\033[0m")
                continue

            pedidos_cliente = db.query(Pedido).filter_by(id_clientes=cliente.id).all()

            if not pedidos_cliente:
                print(f"\033[91mNão encontramos pedidos para {nome_cliente}.\033[0m")
                continue

            print(f"\n\033[94mPedidos de {nome_cliente}\033[0m".center(60, "="))
            for pedido in pedidos_cliente:
                print(f"\n\033[92mID Pedido:\033[0m \033[1m{pedido.id}\033[0m")
                print(f"\033[92mData do Pedido:\033[0m {pedido.data_pedido}")
                print(f"\033[92mQuantidade de Produtos:\033[0m {pedido.quantidade_pedido}")
                print(f"\033[92mID Cliente:\033[0m {pedido.id_clientes}")
                print("-" * 50)

                # Exibir os itens do pedido
                if pedido.pedido_itens:
                    print("\033[94mItens do Pedido:\033[0m")
                    for pedido_item in pedido.pedido_itens:
                        item = pedido_item.itens  # Acessando o item relacionado
                        print(f"\033[93mID Produto:\033[0m {item.id}")
                        print(f"\033[93mNome Produto:\033[0m \033[1m{item.nome}\033[0m")
                        print(f"\033[93mPreço Produto:\033[0m R$ {item.preco:.2f}")
                        print(f"\033[93mQuantidade:\033[0m {pedido_item.quantidade}")
                        print("-" * 50)
                else:
                    print("\033[91mEste pedido não contém itens.\033[0m")
                    print("-" * 50)
            break

    def consulta_Clientes(self, db: Session):
        clientes_cadastrados = db.query(Clientes).all()

        if not clientes_cadastrados:
            print ("Não existem clientes cadastrados")
            return

        for clientes in clientes_cadastrados:
            print(f'ID: {clientes.id}\n'
                  f'Nome: {clientes.nome}\n'
                  f'Endereço: {clientes.telefone}\n'
                  f'Telefone: {clientes.endereco}\n')
            
    def consulta_Colaborador(self, db: Session):
        colaboradores_cadastrados = db.query(Colaborador).all()

        if not colaboradores_cadastrados:
            print("Não temos colaboradores cadastrados")
            return
        
        for colaboradores in colaboradores_cadastrados:
            print(f'ID: {colaboradores.id}\n'
                  f'Nome: {colaboradores.nome_colaborador}\n'
                  f'CPF: {colaboradores.cpf_colaborador}\n'
                  f'Telefone: {colaboradores.telefone_colaborador}\n')
            
class Consultar():
    
    def __init__(self):
        self.consultas = consultas_BD()

    def consulta(self, db: Session):

            while True:
                print("\n" + "=" * 50)
                print("          Escolha uma opção para consultar          ")
                print("=" * 50)
                try:
                    opcaoCadastrar = int(input(
                        "[1] - CLIENTE\n"
                        "[2] - ITEM\n"
                        "[3] - COLABORADOR\n"
                        "[4] - SAIR\n"
                    ))

                    if opcaoCadastrar == 1:
                       self.consultas.consulta_Clientes(db)
                    elif opcaoCadastrar == 2:
                        self.consultas.consultar_Item(db)
                    elif opcaoCadastrar == 3:
                        self.consultas.consulta_Colaborador(db)
                    elif opcaoCadastrar == 4:
                        print("Saindo do sistema. Até logo!")
                        break
                    else:
                        print("Opção Incorreta. Tente novamente.")

                except ValueError:
                    print("Entrada inválida, digite um número entre 1 e 3.")  

