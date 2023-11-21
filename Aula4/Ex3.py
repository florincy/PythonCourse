#Exercício 3
#Versão plus
n=int(input("Digite um número natural: "))
if n == 0:
    print (f"{n} não é primo")
else:
    for i in range (2,n):
        if n%i == 0 and i != n:
            print (f"{n} não é primo")
            break
    else:
        print (f"{n} é primo")

#Versão basic

n=int(input("Digite um número natural: "))
primo = True
if n == 0:
    print (f"{n} não é primo")
else:
    for i in range (2,n):
        if n%i == 0 and i != n:
            primo = False
            break
    if primo == True:
        print (f"{n} é primo")
    else: 
        print (f"{n}  não é primo")