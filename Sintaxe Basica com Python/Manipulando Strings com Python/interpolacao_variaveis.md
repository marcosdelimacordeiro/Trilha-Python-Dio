# Interpolacao de variaveis

Em Python temos 3 formas de interpolar variáveis em strings, a primeira e usando o sinal de %, a segunda é utilizando o metodo format e a ultimas e utilizando f strings.
A 1º forma não e atualmente recomendada e seu uso em Python 3 é raro.
* Olds style %
 - nome = "Marcos"
 - idade = 18
 - profissao = "Programador"
 - linguagem = "Python"
 - print("Ola, me chamo %s. Eu tenho %d anos de idades, trabalho como %s e estou matriculado no curso de %s." %(nome,idade,profissao,linguagem)) 
 - >>> Olá, me chamo Marcos, Eu tenho 18 anos de idade,trabalho como programador e estou matriculado no curso de Python.
* Método format - tem varias formas de formatar a string, 1º formar e utilizar chaves onde ficar a variavel e no final coloca .format(sequencias das variaveis para preencher chaves), tem que informar na order correta senao sera trocado
 - nome = "Marcos"
 - idade = 18
 - profissao = "Programador"
 - linguagem = "Python"
 - print("Ola, me chamo {}. Eu tenho { } anos de idades, trabalho como {} e estou matriculado no curso de {}.".format(nome,idade,profissao,linguagem)) 
 - >>> Olá, me chamo Marcos, Eu tenho 18 anos de idade,trabalho como programador e estou matriculado no curso de Python.
 * metodo format traz um capacidade de um pouco mais de costumizacao, como exemplo a seguir, foi pode colocar na chaves a posicao da variavel que voce quer colocar dentro da string. isso ajuda quando a variavel aparece n vezes, podendo simples colocar o indice na passagem de argumento.
  - nome = "Marcos"
 - idade = 18
 - profissao = "Programador"
 - linguagem = "Python"
 - print("Ola, me chamo {2}. Eu tenho {1 } anos de idades, trabalho como {3} e estou matriculado no curso de {0}.".format(linguagem,idade,nome,profissao)) 
 - >>> Olá, me chamo Marcos, Eu tenho 18 anos de idade,trabalho como programador e estou matriculado no curso de Python.
 *outra forma seria passar os argumentos de formas nomeadas, na hora de passar os valores ao inves de so passar o nome, tera que passar qual identidficador dela foi atribuido. 
 print("Ola, me chamo {nome}. Eu tenho {idade} anos de idades, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome,idade=idade,profissao=profissao,linguagem=linguagem)) 
 - >>> Olá, me chamo Marcos, Eu tenho 18 anos de idade,trabalho como programador e estou matriculado no curso de Python.
 * outro metodo,elabora um dicionario com o nome pessoa e defini todas as chaves ou identificadores na string. 
 print("Ola, me chamo {nome}. Eu tenho {idade} anos de idades, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**pessoa)) 
 - >>> Olá, me chamo Marcos, Eu tenho 18 anos de idade,trabalho como programador e estou matriculado no curso de Python.

 * f-string - ele e parecido com o format, diferenca que nao precisa mais acrescentar .format no final, e entre chaves ja acrescenta o nome da varivel.
 - nome = "Marcos"
 - idade = 18
 - profissao = "Programador"
 - linguagem = "Python"
 - print(f"Ola, me chamo {nome}. Eu tenho {idade} anos de idades, trabalho como {profissao} e estou matriculado no curso de {linguagem}.") 
 - >>> Olá, me chamo Marcos, Eu tenho 18 anos de idade,trabalho como programador e estou matriculado no curso de Python.

 *Formatar strings com f-string
 PI= 3.14159
- quando tem valor grande e que formatar usa como no exemplo a seguir
 print(f"valor de PI: {PI:.2f}") - quando quer exibir 2 casas depois da virgula, nenhum valor antes do ponto, ira exibir como no valor abaixo
 >>> "Valor de PI: 3.14"

 print(f"Valor de PI: {PI:10.2f}") - quando que acrescentar espaco antes do ponto e formatar depois, colocando o valor que ira ser acrescentado antes do ponto e tambem o valor que ser acrescentado depois do ponto.
 >>> "Valor de PI:      3.14"