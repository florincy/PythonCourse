#Aula 3

#Python conditions

#1) Operadores comparativos
nome = "Simone"
tipo_sanguineo = "o+"
if tipo_sanguineo == "o+":
    print("Doador universal")
else: 
    print("Não é doador universal")

#Sim, você pode usar um if sem um else!

numero = 1
if  numero >= 0:
    print("Número positivo")

denominador = 0
numerador = 1
if numero != 0:
    resultado = numerador/denominador
    print(resultado)
else:
    print("Não é possível dividir por zero")

#2) Operadores Lógicos 

if a >= 0 and a%2 == 0:
    print("a é número par positivo")

#3) Operadores de identidade

vetor1=[0,0,0]
vetor2=[1,1,1]
if vetor1 is vetor2:
    print("Estão no mesmo lugar na memória")
else:
    print("Não estão no mesmo lugar da memória")

#Fun fact do interpretador CPython
a = 1
b = 1
print(id(a))  
print(id(b))  
print(a is b) 

#4) Operadores de associação 
vetor1=[0,0,0]
if 1 in vetor1:
    print("1 está no vector 1")
else:   
    print("1 não está no vector 1")


