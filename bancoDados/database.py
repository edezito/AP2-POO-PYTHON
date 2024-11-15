from config import Base, engine, SessionLocal

def import_models():
    from bancoDados.models import (
        Clientes,
        Pedido,
        Itens,
        Entrega,
        Colaborador
    )

# Criação das tabelas no banco de dados
import_models()
Base.metadata.create_all(bind=engine)
print("Banco de dados e tabelas criados com sucesso!")

if __name__ == "__main__":
    pass