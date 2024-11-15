from sqlalchemy.orm import Session
from ..bancoDados.models import
from funcionalidades.cadastro import cadastro

class autenticacao():
    def __init__(self, db: Session):
        self.cadastro = cadastro()

    def autenticarCliente(self, db: Session):
        
        while True:
            opcCadastro = int(input("Você tem cadastro?"
                                    "[1] - SIM"
                                    "[2] - NÃO"))

            try:
                if opcCadastro == 1:
                    opcCPF = input("Digite seu CPF: ")
                    verificarCPF = db.query(Cliente).filter_by(cpf = opcCPF).first()
                    if not verificarCPF:
                        print(f"Não temos Cliente cadastrado com esse CPF: {opcCPF}")
                        continuar = input("Tente novamente? (S/N): ")
                        if continuar.lower() != 's':
                            break
                        continue
                    if verificarCPF:
                        print(f'Olá, {verificarCPF.nome} seja bem vindo!')

                elif opcCadastro == 2:
                    self.cadastro.cadastro_Cliente()
            except ValueError:
                print("Entrada inválida, digite um número entre 1 e 2.")

