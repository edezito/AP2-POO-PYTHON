from funcionalidades.cadastro import cadastro
from sqlalchemy.orm import Session
from bancoDados.models import Cliente

class autenticacaoCliente():
    def __init__(self):
        self.cadastro = cadastro()

    def autenticar(self, db: Session):
        while True:
            try:
                opc_cliente = int(input("Olá, você é nosso cliente?\n"
                                       "[1] - Sim\n"
                                       "[2] - Não\n"
                                       "Selecione uma opção: "))
                
                if opc_cliente == 1:
                    opcCPF = input("Digite seu CPF: ")
                    cliente = db.query(Cliente).filter(Cliente.cpf.ilike(f"%{opcCPF}%")).first()
                    
                    if not cliente:
                        print(f"\033[91mNão encontramos um cliente com o CPF {opcCPF}. Tente novamente.\033[0m")
                    else:
                        print(f"\033[92mOlá, {cliente.nome} seja bem vindo!\033[0m")
                        break 
                elif opc_cliente == 2:
                    self.cadastro.cadastro_Cliente(db)
                    break 
                else:
                    print("Opção inválida! Selecione 1 ou 2.")
            except ValueError:
                print("Opção Inválida, selecione um número entre 1 e 2.")