class projeto_bancario:
    def __init__(self):
        self.saldo = 0
        self.saques_diarios = 0
        self.extrato = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(('Depósito', valor))
            print("Depósito de R$ {:.2f} realizado com sucesso.".format(valor))
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if self.saques_diarios < 3:
            if valor <= 500 and valor <= self.saldo:
                self.saldo -= valor
                self.saques_diarios += 1
                self.extrato.append(('Saque', valor))
                print("Saque de R$ {:.2f} realizado com sucesso.".format(valor))
            else:
                print("Valor de saque excede o limite diário ou saldo insuficiente.")
        else:
            print("Número máximo de saques diários atingido.")

    def extrato_conta(self):
        if not self.extrato:
            print("Não há movimentações na conta.")
        else:
            print("Extrato da conta:")
            for operacao, valor in self.extrato:
                print("{}: R$ {:.2f}".format(operacao, valor))
            print("Saldo atual: R$ {:.2f}".format(self.saldo))


# Função principal para interagir com o usuário
def main():
    sistema = projeto_bancario()

    while True:
        print("\n======= Menu =======")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            sistema.deposito(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            sistema.saque(valor)
        elif opcao == '3':
            sistema.extrato_conta()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
