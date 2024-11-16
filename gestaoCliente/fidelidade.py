from bancoDados.models import Item, Cliente, PedidoItem
from sqlalchemy.orm import Session
from .autenticacao import AutenticacaoCliente

class programaFidelidade():
    def __init__(self, autenticacao_cliente: AutenticacaoCliente):
        self.autenticacao = autenticacao_cliente

    def associarPontos(self, db: Session):

        if self.autenticacao.opcCPF:
            verificar_cliente = db.query(Cliente).filter_by(cpf=self.autenticacao.opcCPF).first()
            
            if not verificar_cliente:
                print("Cliente não encontrado.")
                return
            
            if not verificar_cliente.pedidos:
                print("Você não tem pedidos realizados.")
                return
            
            pontos_totais = 0
            
            for pedido in verificar_cliente.pedidos:
                # Obtém os itens relacionados a esse pedido
                verificar_pedidos = db.query(PedidoItem).filter_by(pedido_id=pedido.id).all()
                
                if verificar_pedidos:
                    pontos_do_pedido = len(verificar_pedidos)
                    pontos_totais += pontos_do_pedido

                    print(f"Pedido {pedido.id} - {pedido.data_pedido}: {pontos_do_pedido} pontos atribuídos.")
                else:
                    print(f"Pedido {pedido.id}: Nenhum item encontrado.")
            
            verificar_cliente.pontos += pontos_totais
            db.commit()

            print(f"Total de pontos do cliente: {verificar_cliente.pontos}")
            
        else:
            print("CPF não informado. Realize a autenticação primeiro.")
