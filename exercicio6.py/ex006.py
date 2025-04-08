def valorDebito():

    saldototal= 1000
    Senha = "2514"
    tentativas = 3

    while tentativas > 0:
        
        login = input("Insira a senha:")
        if login == Senha:
            print("Valor debitado da conta (-100). Saldo restante:", (saldototal - 100))
            break
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Erro. você tem mais {tentativas} tentativas.")
            else:
                print("Erro, número de tentativas exedidas.")
valorDebito()


def Saque():
    saldoTotal= 2500
    valor = int(input("Digite o valor a ser retirado: "))
    saqueEfetuado = valor

    if valor > saldoTotal:
        print("Erro no saque, verifique se há saldo suficiente. Seu saldo é:",(saldoTotal))
    else:
        print("Saque efetuado no valor de:", saqueEfetuado, "Saldo restante:",(saldoTotal - saqueEfetuado))
Saque()