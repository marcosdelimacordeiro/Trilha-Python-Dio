# Conhecendo métodos úteis da classe string

A classe String do Python é famosa por ser rica em métodos e possuir uma interface muito fácil de trabalhar. Em algumas linguagens manipular sequencias de caracteres não é um trabalho trivial,porém, em Python esse trabalho é muito simples.

## maiúscula,minúscula e titulo
* curso = "pYtHon"

* print(curso.upper())
    >>> PYTHON  (metodo upper converte tudo para maiuscula)
* print(curso.lower())
    >>> python (metodo lower converte tudo para minusculo)
* print(curso.title())
    >>> Python (metodo title converte 1º letra para maiuscula)

###  metodo eliminando espacos em brancos
* curso = "     Python "

* print(curso.strip())
    >>> "Python" (metodo strip elimina todos espacos em brancos)
* print(curso.lstrip())
    >>>"Python "  (metodo lstrip elimina todos os espacos em branco a esquerda)
* print(curso.rstrip())
    >>>"    Python" (metodo rstrip elimina espacos em branco a direita)
#### Junções e centralização
* curso = "Python"

* print(curso.center(10, "#"))
    >>> "##Python##" (metodo center ira preencher com "#" ou qualque coisa colocada ate tamanho de caracteres definidos no primeiro parametro)
* print(".".join(curso))
    >>> "P.y.t.h.o.n" (esse metodo join ira fazer a juncao entre 1º paramentro com o 2º parametro)
**OBS** : Interavel em Python seria um objeto que por ser percorrido elemento por elemento, geralmente por um for.
