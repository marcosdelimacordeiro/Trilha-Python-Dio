# primera parte e oque vem antes do if no exemplo e um String, na segunda parte e condição que sera testada , se ela for atendida , vai para primeira parte e dara o retorno de "sucesso", caso a segunda parte nao seja atendida, entao vai para terceira parte que sera o a mensagem de "falha", isso e muito util para teste simples, compor um mensagem ou retorno para um formatacao.
saldo = 2000
saque = 5000
status = "Sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar o saque!")