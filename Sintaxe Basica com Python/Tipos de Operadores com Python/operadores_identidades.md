# Operadores de Identidade

São Operadores utilizados para comparar se os dois objetos testados ocupam a mesmas posição na memoria.
O operadore de identidade e o operador **IS**

## exemplo
curso = "Curso de Python"
nome_curso = curso
saldo,limite = 200, 200

curso is nome_curso
>>> True

curso is not nome_curso
>>> False

saldo is limite
>>> True