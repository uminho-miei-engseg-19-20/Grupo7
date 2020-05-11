import re
import datetime

def pagar(): # Valor a pagar até 5 dígitos, excluindo os cêntimos
    while True:
        valor = input('Valor a pagar: \n')
        if re.match("^[0-9]{1,5}\.[0-9]{2}$", valor):
            return valor
        else:
            print('Por favor insira o valor seguido dos cêntimos (ex: 105.20)')

def dob(): # Data de nascimento (formato DD-MM-AAAA)
    while True:
        dob = input('Data de nascimento (dd/mm/aaaa): \n')
        isValid = False
        try:
            date = datetime.datetime.strptime(dob, '%d/%m/%Y')
            print("Date: " + str(date))
            today = datetime.datetime.today()
            if(date < today):
                return dob
            else:
                print("Data de nascimento deve estar no passado")
        except ValueError:
            print("Data de nascimento inválida, tente DD/MM/AAAA")

def nome(): # Nome (desde de que tenha pelo menos uma letra para primeiro e último nome, no máximo 6 nomes desde que comecem por letra maiúscula); cada nome próprio tem no máximo 10 caracteres; não permite "da Costa" por exemplo, ou deve escrever "Da Costa"
    while True:
        nome = input('Escreva o seu nome: \n')
        if re.match("^([A-Z][a-z]{0,9})(\s[A-Z][a-z]{0,9}){1,5}$", nome):
            return nome
        else:
            print("Escreva o nome no formato correto, deve ter pelo menos primeiro e último nome e devem começar por letra maiúscula")

def nif(): # Número de identificação fiscal
    while True:
        nif = input('Escreva o seu NIF (9 dígitos): \n')
        if re.match("^[0-9]{9}$", nif):
            return nif
        else:
            print("Escreva o NIF no formato correto")

def nic(): # Número de identificação de cidadão https://www.autenticacao.gov.pt/documents/20126/115760/Valida%C3%A7%C3%A3o+de+N%C3%BAmero+de+Documento+do+Cart%C3%A3o+de+Cidad%C3%A3o.pdf/bdc4eb37-7316-3ff4-164a-f869382b7053?t=1588780568207&download=true
    while True:
        nic = input('Escreva o seu número de identificação de cidadão:\n')
        if re.match("^[0-9]{8}\s[0-9]\s([A-Z]|[0-9]){2}[0-9]$", nic):
            return nic
        else:
            print("Escreva o seu NIC no formato correto")

def cardNr(): # Valida número do cartão
    while True:
        nr = input('Insira o seu número de cartão de crédito\n')
        if re.match("^[0-9]{14}$", nr):
            return nr
        else:
            print("Formato incorreto")

def dataValidade():
    while True:
        val = input('Insira a data de validade do cartão:\n')
        if re.match("^(0[6-9]/20|(0[1-9]|[1][0,1,2])/2[1-6])$", val):
            return val
        else:
            print("Formato ou data inválida, tente MM/AA")

def cvv():
    while True:
        cvv = input('Insira o seu CVC/CVV:\n')
        if re.match("^[0-9]{3,4}$", cvv):
            return cvv
        else:
            print("Formato inválido, tente novamente")

def credito(): # Nr. cartão de crédito, validade e CVC/CVV
    nc = cardNr()
    dv = dataValidade()
    c = cvv()
    return nc, dv, c

def main():
    p = pagar()
    d = dob()
    n = nome()
    nifs = nif()
    nics = nic()
    a, b, d = credito()

    print("Recolhidos todos os dados\n")
    print("Mostrando dados recolhidos: \n")
    print("Valor a pagar: " + p)
    print("Data de nascimento: " + d)
    print("Nome: " + n)
    print("NIF: " + nifs)
    print("NIC: " + nics)
    print("Cartão de crédito nr.: " + a + " de validade " + b + " e CVC/CVV " + d)


main()