# Fatiamento de string

Fatiamento de strings é uma técnica utilizada para retornar substrings(partes da string original), informando inicio(start), fim(stop) e passo(step): [start:stop[,step]].

* exemplo de fatimento
- nome = "Fabio da Silva Santos"

-nome[0] - ira pegar apenas o primeiro indice
>>> "F"

-nome[:5] - senao informar o Start ele considera a partir o 0 vai ate indice stop indicado no ex.
>>> "Fabio"

-nome[5:] -se indice start ,vai comecar no 5 percorrer ate o final
>>> "da Silva Santos"

-nome[5:14] - indice start 5, vai comecar no 5 ate indice stop indica 
>>> "da Silva"

-nome[5:14:2]- indice start 5, percorre ate indice stop 14, mas pulando de 2 em 2 indice.
>>> "aSla"

-nome[:] - nao indica o star e nem o stop, ira retorna a variavel inteira
>>> "Fabio da Silva Santos"

-nome[::-1] - passa sem star, stop, passando step -1 ,vai criar copia invertida da variavel.
>>> "sotnaS avliS ad oibaF"