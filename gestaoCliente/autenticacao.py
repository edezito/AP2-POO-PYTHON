from funcionalidades.cadastro import cadastro
from sqlalchemy.orm import Session
from bancoDados.models import Cliente

class AutenticacaoCliente:
    def __init__(self):
        self.cadastro = cadastro()

    def autenticar(self, db: Session):
        while True:
            try:
                print("\033[96m=== Bem-vindo ao sistema de autenticação de clientes ===\033[0m")
                opc_cliente = int(input("\nVocê é nosso cliente?\n"
                                       "\033[93m[1] - Sim\033[0m\n"
                                       "\033[93m[2] - Não\033[0m\n"
                                       "\033[94mSelecione uma opção: \033[0m"))
                
                if opc_cliente == 1:
                    opcCPF = input("\033[94mDigite seu CPF: \033[0m")
                    cliente = db.query(Cliente).filter(Cliente.cpf.ilike(f"%{opcCPF}%")).first()
                    
                    if not cliente:
                        print(f"\033[91m\n Não encontramos um cliente com o CPF {opcCPF}. Tente novamente.\033[0m\n")
                    else:
                        print(f"\033[92m\n Olá, {cliente.nome}! Seja bem-vindo!\033[0m\n")
                        break 
                elif opc_cliente == 2:
                    print("\033[93m\nRedirecionando para o cadastro...\033[0m")
                    self.cadastro.cadastro_Cliente(db)
                    break 
                else:
                    print("\033[91m\nOpção inválida! Selecione 1 ou 2.\033[0m\n")
            except ValueError:
                print("\033[91m\nEntrada inválida! Por favor, insira um número (1 ou 2).\033[0m\n")