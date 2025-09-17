conta_normal = False
conta_universitaria = False
saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque Realizado com Sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não foi possivel Realizar o Saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque Realizado com Sucesso!")
    else:
        print("Saldo Insuficiente!")
else:
    print("Sistema não reconheceu o tipo de conta entre em contato com seu Gerente!")