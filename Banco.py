# ALUNOS: Bruno César Gonçalves Meireles - RA: 22303293
#         Felipe Rodrigues Queiroz - RA: 22301517
#         Gabriel de Medeiros Lima - RA: 22303031

##################################
## Criação de Classes e Métodos ##
##################################

import datetime

class Historico_Conta:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprimir_historico(self):
        print("Data de abertura da Conta: {}".format(self.data_abertura))
        print("Transações na conta: ")
        for transacao in self.transacoes:
            print("-", transacao)
        
    def gravar_historico(self):
        hist = open('historico.txt', 'a')
        hist.write("---------------------------------\n")
        hist.write("Data de abertura da conta: " + str(self.data_abertura) + "\n")
        hist.write("Transacoes dessa conta: " + str(self.transacoes) + "\n")
        hist.write("---------------------------------")
        hist.write("\n")
        hist.close()

    def ler_historico(self):
        with open('historico.txt', 'r') as arquivo:
            lista_hist = arquivo.readlines()
            print(lista_hist)
        return lista_hist
    

class Cliente:
    def __init__(self, nome_completo, cpf):
        self.nome_completo = nome_completo
        self.cpf = cpf

    def imprimir_cliente(self):
        print("Nome Completo: {} | CPF cadastrado: {} \n".format(self.nome_completo, self.cpf))

    def gravar_cliente(self):
        cli = open("cliente.txt", "a")
        cli.write("---------------------------------\n")
        cli.write("Nome do cliente: " + self.nome_completo + "\n")
        cli.write("CPF: " + self.cpf + "\n")
        cli.write("---------------------------------")
        cli.write("\n")
        cli.close()

    def ler_cliente(self):
        with open("cliente.txt", "r") as arquivo:
            lista_clientes = arquivo.readlines()
            print(lista_clientes)
        return lista_clientes
    

class Conta:
    def __init__(self, cliente, numero_conta, saldo):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.historico = Historico_Conta()

    def deposito(self, quantia):
        self.saldo += quantia
        self.historico.transacoes.append("Foi confirmado um depósito de R${} .".format(quantia))

    def saque(self, quantia):
        if self.saldo < quantia:
            print("Não é possível sacar essa quantia de dinheiro. Seu saldo é insuficiente. \n")
            return False
                
        elif self.saldo == 0.0:
            print("Não é possível sacar essa quantia de dinheiro. Seu saldo é insuficiente. \n")
            return False
        
        else:
            self.saldo -= quantia
            self.historico.transacoes.append("Foi feito um saque com valor de R${} .".format(quantia))

    def extrato_conta(self):
        print("Cliente: {} | Número da Conta : {} | Saldo: {} |".format(self.cliente, self.numero_conta, self.saldo))
        self.historico.transacoes.append("Foi conferido o extrato da conta - o saldo é de {}".format(self.saldo))

    def transferencia(self, conta_destino, valor):
        envio_de_dinheiro = self.saque(valor)

        if envio_de_dinheiro == False:
            return False
        
        else:
            conta_destino.deposito(valor)
            self.historico.transacoes.append("Transferência de R${} para a conta {} do cliente {}. ".format(valor, conta_destino.numero_conta, conta_destino.cliente))


    def gravar_conta(self):
        acc = open("conta.txt", "a")
        acc.write("---------------------------------\n")
        acc.write("Cliente da conta: " + self.cliente + "\n")
        acc.write("Numero da conta: " + self.numero_conta + "\n")
        acc.write("Saldo da conta: R$" + str(self.saldo) + "\n")
        acc.write("---------------------------------")
        acc.write("\n")
        acc.close()

    def ler_conta(self):
        with open("conta.txt", "r") as arquivo:
            lista_contas = arquivo.readlines()
            print(lista_contas)
        return lista_contas
    


#############################################
## Parte Principal de Execução do Programa ##
#############################################

cliente1 = Cliente("Marco Prada", "256719809-21")
conta1 = Conta(cliente1.nome_completo, "1100-9", 4000.0)

cliente2 = Cliente("Pietro Cesare", "339428101-05")
conta2 = Conta(cliente2.nome_completo, "1856-3", 2500.0)

cliente3 = Cliente("Phillip Augustin", "521099712-80")
conta3 = Conta(cliente3.nome_completo, "3002-10", 6150.0)

conta1.deposito(150.0)
conta1.saque(400.0)

conta3.saque(85.0)

conta1.transferencia(conta2, 250.0)

conta3.transferencia(conta1, 120.0)

cliente1.imprimir_cliente()
conta1.extrato_conta()
conta1.historico.imprimir_historico()

print("==================================================================\n")
cliente2.imprimir_cliente()
conta2.extrato_conta()
conta2.historico.imprimir_historico()

print("==================================================================\n")
cliente3.imprimir_cliente()
conta3.extrato_conta()
conta3.historico.imprimir_historico()

print("==================================================================\n")
###########################################
## Gravações e leituras em arquivos .txt ##
###########################################

cliente1.gravar_cliente()
cliente2.gravar_cliente()
cliente3.gravar_cliente()

cliente1.ler_cliente()

conta1.gravar_conta()
conta2.gravar_conta()
conta3.gravar_conta()

conta1.ler_conta()

conta1.historico.gravar_historico()
conta2.historico.gravar_historico()
conta3.historico.gravar_historico()

conta1.historico.ler_historico()
