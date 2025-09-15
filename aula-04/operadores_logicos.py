saldo = 500 #variavel saque atribuido valor de 500
saque = 200 #variavel saque atribuido valor de 200
limite = 100 #variavel saque atribuido valor de 100

#verificando se saldo e maior ou igual a saque
print(saldo >= saque)
#verificando se saque e menor ou igual a limite
print(saque <= limite)

#adicionando operadores logicos junto com operadores de comparação
#operador AND, somente tera retorno TRUE se as duas condicoes forem verdadeiras, senao o retorno sera FALSE.
print(saldo >= saque and saque <= limite)

# Operador OR, se uma das condicoes forem sastifeitas ele retorna TRUE, se nenhuma das condicões forem verdadeiras ele retorna FALSE.

print(saldo >= saque or saque <= limite)

# Operador Negacao, e usado para negar algo.
contatos_emergencia = [] # lista vazia em python e considerado FALSE
print(not 1000 > 1500)
print(not contatos_emergencia)
print(not "saque 1500") #uma String com valor 
print(not "") #string vazia

#pode comparar expressao que retorna um valor BOOLEANO, em Python tambem da para negar valores dentro de um sequencia, como objetos ou caracteres.

# utilizando com parênteses para determinar ordem de precedencias.
