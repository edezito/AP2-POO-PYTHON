from datetime import datetime

from sqlalchemy.orm import Session
from bancoDados.models import Itens, PedidoItem, Pedido, Clientes

from ..funcionalidades.consultasdb import consultas_BD

class realizarPedidos:
    def __init__(self):
        self.pedidos = []

        #consultas
        self.consulta_item = consultas_BD()
        self.consulta_pedido = consultas_BD()
        

    def realizar_Pedido(self, db: Session):
        
        #ITENS DISPONÍVEIS
        self.consulta_item.consultar_Item(db)

        while True:
            codigo_selecionado = input("\n\033[93mDigite o código do produto desejado:\033[0m ")

            #SELECIONAR PEDIDO
            item_selecionado = db.query(Itens).filter_by(id = codigo_selecionado).first()
            if not item_selecionado:
                print(f"\033[91mProduto com código {codigo_selecionado} não encontrado. Tente novamente.\033[0m")
                continuar = input("Tente novamente? (S/N): ")
                if continuar.lower() != 's':
                    break
                continue

            if item_selecionado:
                print(f"Produto '{item_selecionado.nome}' adicionado ao pedido.")

                #SELECIONAR QUANTIDADE
                quantidade = int(input(f"Digite a quantidade do produto '{item_selecionado.nome}': "))

                # ID - CLIENTE 
                while True:
                    nome_cliente = input("\n\033[93mDigite o seu nome (ou digite 'sair' para encerrar):\033[0m").strip()
                    
                    if nome_cliente.lower() == 'sair':
                        print("\033[92mEncerrando a busca.\033[0m")
                        break

                    if not nome_cliente:
                        print("\033[91mO nome do cliente não pode estar vazio.\033[0m")
                        continue
                    
                    cliente = db.query(Clientes).filter(Clientes.nome.ilike(f"%{nome_cliente}%")).first()
                    
                    if not cliente:
                        print(f"\033[91mNão encontramos um cliente com o nome {nome_cliente}. Tente novamente.\033[0m")
                    else:
                        print(f"\033[92mCliente encontrado: {cliente.nome}\033[0m")
                        break
                    
                
                cliente_id = cliente.id


            #ADICIONAR PEDIDO
            novo_pedido = Pedido(
                    data_pedido=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    quantidade_pedido=quantidade,
                    id_clientes=cliente.id
                )

            #ADICIONAR PEDIDO NO BD (CREATE)
            db.add(novo_pedido)
            db.commit()

            #ADICIONAR ITEM AO PEDIDO
            pedido_item = PedidoItem(
                    pedido_id=novo_pedido.id,
                    item_id=item_selecionado.id,
                    quantidade=quantidade
                )
            db.add(pedido_item)
            db.commit()

            print("\033[92mPedido salvo com sucesso.\033[0m")
            break

    def excluir_Pedidos(self, db: Session):
        
        #PEDIDOS DISPONÍVEIS
        self.consulta_pedido.consultar_Pedidos(db)
        
        id_pedido = input(("\n\033[93mDigite o ID do pedido que deseja excluir (ou 0 para cancelar): \033[0m"))
        if id_pedido == 0:
            print("\033[92mOperação de exclusão cancelada pelo usuário.\033[0m")
            return
        
        #DELETAR PEDIDOS NO BD (DELETE)
        pedido_excluir = db.query(Pedido).filter_by(id=id_pedido).first()
        if pedido_excluir:
            db.delete(pedido_excluir)
            db.commit()
            print(f"\033[92mPedido ID {id_pedido} excluído com sucesso.\033[0m")
        else:
            print(f"\033[91mPedido com ID {id_pedido} não encontrado.\033[0m")

    def atualizar_Pedidos(self, db: Session):
        # PEDIDOS DISPONÍVEIS
        self.consulta_item.consultar_Pedidos(db)

        id_pedido = input("\n\033[93mDigite o ID do pedido que deseja atualizar (ou 0 para cancelar): \033[0m").strip()

        if id_pedido == "0":
            print("\033[92mOperação de atualização cancelada pelo usuário.\033[0m")
            return

        if not id_pedido.isdigit():
            print("\033[91mID inválido. Por favor, digite um número válido.\033[0m")
            return

        pedido_para_atualizar = db.query(Pedido).filter_by(id=int(id_pedido)).first()
        if not pedido_para_atualizar:
            print("\033[91mPedido não encontrado. Verifique o ID e tente novamente.\033[0m")
            return

        print("\n\033[94mOpções de atualização:\033[0m")
        print("[1] - Atualizar Item")
        print("[2] - Atualizar Quantidade")

        opc_atualizar = input("\033[93mDigite a opção desejada: \033[0m").strip()

        if opc_atualizar == "1":
            novo_item_id = input("\033[93mDigite o novo ID do item: \033[0m").strip()
            if not novo_item_id.isdigit():
                print("\033[91mID de item inválido. Por favor, digite um número válido.\033[0m")
                return
            
            item_atualizado = db.query(Itens).filter_by(id=int(novo_item_id)).first()
            if item_atualizado:
                pedido_para_atualizar.itens = item_atualizado.nome
                db.commit()
                print("\033[92mItem do pedido atualizado com sucesso.\033[0m")
            else:
                print("\033[91mItem com ID fornecido não encontrado.\033[0m")

        elif opc_atualizar == "2":
            nova_quantidade = input("\033[93mDigite a nova quantidade: \033[0m").strip()
            if not nova_quantidade.isdigit() or int(nova_quantidade) <= 0:
                print("\033[91mQuantidade inválida. Digite um número positivo.\033[0m")
                return

            pedido_para_atualizar.quantidade_pedido = int(nova_quantidade)
            db.commit()
            print("\033[92mQuantidade do pedido atualizada com sucesso.\033[0m")
        
        else:
            print("\033[91mOpção inválida. Por favor, selecione uma opção válida.\033[0m")







        
           



