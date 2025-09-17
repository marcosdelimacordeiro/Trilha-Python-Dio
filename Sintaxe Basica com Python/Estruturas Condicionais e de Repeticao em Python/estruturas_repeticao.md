# Estruturas de Repetição 

São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

## comando FOR

O comando **FOR** e usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco de codigo deve ser executado, ou quando queremos percorrer um objeto iterável.
obs: Objeto iterável em Python, e qualquer objeto que pode ser percorrido por um estrutura de repetiçao.

### Funcao range
Range é uma função buil-in do Python, ela é usada para produzir uma sequencia de numeros inteiros a partir de um inicio(inclusivo) para um fim (exclusivo). Se usarmos range(i,j) sera produzido:
i,i+1,i+2,i+3,...,j-1.
Ela recebe 3 argumentos: stop(obrigatório),start(opcional), e step (opcional).
o range no valor no final, nao e incluido por padrao pois e j-1

obs:Em Python, um recurso built-in é algo que já vem pronto na linguagem, sem precisar importar nada ou instalar bibliotecas externas

#### Comando While

O comando **while** é usado para repetir um bloxo de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de codigo deve ser executado

##### comando Break

O comando **Break** serve para interromper imediatamente uma estrutura de repeticao, mesmo que a condicao do loop ainda seja verdadeira, ou seja, interromper mesmo que ainda haja elementos as serm percorridos.

* um variaçao do **break** e o operador **continue**, ele e util quando queremos pular ou desviar de um situação especifica dentro do laço.