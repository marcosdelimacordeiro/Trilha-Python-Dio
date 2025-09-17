maior_idade = 18
idade_especial = 17

idade =int(input("Informe sua idade: ?"))
# teste usando IF, que pode ser usado quantas vezes necessario.
if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")
if idade < maior_idade:
    print("Você ainda nao pode tirar CNH")


# Utilizando ELSE, facilitando que precisa de uma segunda condicao para executar o bloco, se IF for verdadeiro sera executado, se for falso sera executado o ELSE.
if idade >= maior_idade:
    print("Maior de idade pode tirar CNH")
else:
    print("Ainda nao pode tirar Cnh")

# Utilizando ELIF,podemos utilizar quantos elif forem necessarios para codigo, mas isso aumenta a complexidade do codigo tambem.

if idade >= maior_idade:
    print("Maior de Idade pode tirar a CNH")
elif idade == idade_especial:
    print("Pode fazer aulas teoricas, mas nao pode fazer aulas praticas.")
else:
    print("Ainda nao pode tira CNH")