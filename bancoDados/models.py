from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)
    telefone = Column(String(20), nullable=False)

    pedidos = relationship('Pedido', back_populates='cliente')
    fidelidade = relationship('Fidelidade', back_populates='cliente', uselist=False)

class Pedido(Base):
    __tablename__ = 'pedidos'    

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_pedido = Column(String(20), nullable=False)
    quantidade_pedido = Column(Integer, nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

    cliente = relationship('Cliente', back_populates='pedidos')
    itens_pedido = relationship('PedidoItem', back_populates='pedido', cascade="all, delete-orphan")

class Item(Base):
    __tablename__ = 'itens'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)

    estoque = relationship('Estoque', back_populates='item', uselist=False)
    pedidos_itens = relationship('PedidoItem', back_populates='item')
    compras_itens = relationship('CompraItem', back_populates='item')

class PedidoItem(Base):
    __tablename__ = 'pedido_itens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'))
    item_id = Column(Integer, ForeignKey('itens.id'))
    quantidade = Column(Integer, nullable=False)

    pedido = relationship('Pedido', back_populates='itens_pedido')
    item = relationship('Item', back_populates='pedidos_itens')

class Estoque(Base):
    __tablename__ = 'estoques'

    id = Column(Integer, primary_key=True, autoincrement=True)
    item_id = Column(Integer, ForeignKey('itens.id'))
    quantidade = Column(Integer, nullable=False)

    item = relationship('Item', back_populates='estoque')

class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    contato = Column(String(100), nullable=False)
    endereco = Column(String(200), nullable=False)

    compras = relationship('Compra', back_populates='fornecedor')

class Compra(Base):
    __tablename__ = 'compras'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))
    data_compra = Column(String(20), nullable=False)
    valor_total = Column(Float, nullable=False)

    fornecedor = relationship('Fornecedor', back_populates='compras')
    itens_comprados = relationship('CompraItem', back_populates='compra', cascade="all, delete-orphan")

class CompraItem(Base):
    __tablename__ = 'compra_itens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    compra_id = Column(Integer, ForeignKey('compras.id'))
    item_id = Column(Integer, ForeignKey('itens.id'))
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)

    compra = relationship('Compra', back_populates='itens_comprados')
    item = relationship('Item', back_populates='compras_itens')

class Colaborador(Base):
    __tablename__ = 'colaboradores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)
    cpf = Column(String(20), nullable=False)

class TransacaoFinanceira(Base):
    __tablename__ = 'transacoes_financeiras'

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String(20), nullable=False)  # "receita" ou "despesa"
    valor = Column(Float, nullable=False)
    data = Column(String(20), nullable=False)
    descricao = Column(String(200), nullable=True)

class Fidelidade(Base):
    __tablename__ = 'fidelidades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    pontos = Column(Integer, nullable=False)
    nivel_fidelidade = Column(String(50), nullable=False)

    cliente = relationship('Cliente', back_populates='fidelidade')