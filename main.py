# This is a sample Python script.
from conta import Conta
from cliente import Cliente

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi,', name)
    # guadar em json
    cliente = Cliente('joão', 'estanislau', '455.555.444-34')
    conta = Conta('123-41', cliente.nome, 1000.0)
    conta1 = Conta('456-98', 'nicolas', 2000.0)
    conta2 = Conta('312-66', 'maria', 3000.0)
    conta.depositar(50.0)
    conta.saca(100.0)
    conta.extrato(conta)
    conta1.extrato(conta1)
    conta2.extrato(conta2)

    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
