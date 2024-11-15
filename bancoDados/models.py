from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Clientes(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)
    telefone = Column(String(20), nullable=False)

    pedidos = relationship('Pedido', back_populates='cliente')


class Pedido(Base):
    __tablename__ = 'pedido'    

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_pedido = Column(String(20), nullable=False)
    quantidade_pedido = Column(Integer, nullable=False)
    id_clientes = Column(Integer, ForeignKey('clientes.id'))

    cliente = relationship('Clientes', back_populates='pedidos')
    pedido_itens = relationship('PedidoItem', back_populates='pedido')


class Itens(Base):
    __tablename__ = 'itens'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)

    pedido_itens = relationship('PedidoItem', back_populates='itens')


# (tabela intermediária entre Pedido e Itens)
class PedidoItem(Base):
    __tablename__ = 'pedido_itens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'))
    item_id = Column(Integer, ForeignKey('itens.id'))
    quantidade = Column(Integer, nullable=False)

    pedido = relationship('Pedido', back_populates='pedido_itens')
    itens = relationship('Itens', back_populates='pedido_itens')


class Colaborador(Base):
    __tablename__ = 'colaborador'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_colaborador = Column(String(100), nullable=False)
    telefone_colaborador = Column(String(20), nullable=False)
    cpf_colaborador = Column(String(20), nullable=False)