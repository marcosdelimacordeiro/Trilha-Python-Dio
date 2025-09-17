texto = "python"
vogais ="aeiou"
for letras in texto:
    if letras in vogais:
        print(letras, end="")

print()


# exemplo utilizando a funcao buil-in range
for numeros in range(0,11,1):
    print(f" 5 X {numeros}  =  {numeros * 5}")