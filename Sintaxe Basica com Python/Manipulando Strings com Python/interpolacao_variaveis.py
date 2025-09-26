nome = "Marcos"
idade = 18 
profissao = "programador"
linguagem = "Python"
saldo = 45.435
#dicionario
dados = {"nome":"Marcos", "idade":20, "saldo": 45.435}

print("nome: %s , idade: %i"%(nome,idade))

print("nome: {}, idade: {}".format(nome,idade))

print("nome:{1}, idade: {0}".format(idade,nome))
print("nome: {1}, idade: {0} , nome: {1} {1}".format(idade, nome))

print("nome: {name}, idadade: {idade}".format(name=nome, idade=idade))
print("nome:{name} idade:{age} {name} {name} {age}".format(age=idade,name=nome))

print("nome: {nome}, idade: {idade}".format(**dados))
print(f"nome: {nome} idade: {idade} saldo: {saldo:10.2f}")
print(f"nome: {nome} idade: {idade} saldo: {saldo:.2f}")