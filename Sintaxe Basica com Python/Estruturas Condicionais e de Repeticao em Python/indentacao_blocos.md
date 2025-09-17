# Indentacao e os Blocos de comandos.

Identar código e uma forma de manter o codigo fonte mais legível e manutenível. Mas em Python ela exerce um segundo papel, através da identação o interpretador consegue determinar onde um bloco  de comando inicia e onde ele termina.

## Bloco de comando

As linguagens de programação costumam utilizar caracteres ou palavras reservadas para determinar o inicio e o fim do bloco. Em Java e C por exemplo, utiliza chaves:

### Utilizando espaços

Existe um converção em Python, que define as boas práticas para escrita de código na linguagem. Nesse Documento é indicado utilizar 4 espaços em brancos por nivel de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

* exemplo de bloco em Python
    def sacar(self, valor: float) -> none: # inicio do bloco do metodo
        if self.saldo >= valor: # inicio do bloco if
            self.saldo -= valor
        #fim do bloco if
     #fim do bloco do metodo

* exemplo sem indentação em Python, ele nao funciona sem a Indentação
def sacar(self, valor: float) -> none: # inicio do bloco do metodo
if self.saldo >= valor: # inicio do bloco if
self.saldo -= valor
#fim do bloco if
#fim do bloco do metodo

