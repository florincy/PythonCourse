#Exercício 2

n=int(input("Digite o número para cálculo do fatorial "))
if n == 0:
    print(f"fatorial de {n} é 1")
else:   
    resultado=1
    i=0
    while i <n:
        i += 1
        resultado *= i
    print(f"fatorial de {n} é {resultado}")   
    