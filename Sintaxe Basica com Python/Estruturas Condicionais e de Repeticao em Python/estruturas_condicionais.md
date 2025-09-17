# Estruturas Condicionais 

A estrutura condicionais permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

## IF

Para criar um estrutura condicional simples, composta por um unico desvio, podemos utilizar a palavra reservada **IF**. o comando irá testar a expressao logica, e em caso de retorno verdadeiro as acões presentes no bloco de código do **IF** serão executadas. e a forma mais simplificada de fazer um teste.

### IF/ELSE

Para criar um estruturas condicionais com dois desvios, podemos utilizar as palavaras reservadas **IF** e **ELSE**. se a expressao logica testada for verdadeira, entao bloco do **IF** será executado. senao  o bloco do código do **ELSE** que sera executado.
### IF/ELIF/ELSE

Em alguns cenarios queremos mais de dois desvio, para isso podemos utilizar a palavra reservada **ELIF**. O ELIF e composto por um nova expressão logica, que sera testada e caso retorne verdadeiro o bloco de codigo do elif sera executado. Não existe numero maximo de ElIFS que podemos utilizar, porém evite criar grandes estruturas condicionais,pois elas aumentam a complexidade do seu código.
#### IF ANINHADO
Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estruturas if/elif/else, ou seja,podemos ter if dentro de if, se a condicao do if atendida, pode ter outra condicao if para ser testada dentro do bloco.

##### IF TERNARIO

O **IF TERNARIO** permite escrever uma condicão em um unica linha. Ele e composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.
