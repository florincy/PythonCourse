#Aula 4

numeros=[1,2,3]
letras = ["a","b",'c']

for i in range (0,3,1):
    print(f"Rodando a iteração {i}, elemento é {numeros[i]}")

for i in range (0,3,1):
    print(f"Rodando a iteração {i}, elemento é {letras[i]}")

for i in numeros:
    print(f"Passando pelo elemento {i}")

for i in letras:
    print(f"Passando pelo elemento {i}")

#Contador em python
i=0
while i <= 10:
    print (i)
    i+=1

#break
i=0
while True:
    print("Iteração ", i)
    i += 1
    if i > 10:
        print("Acabouuu :(")
        break

#continue
for i in range (0,10,1):
    if i == 0:
        print(f"{i+1}/{i} não é possível!")
        continue
    print(f"{i+1}/{i} é {(i+1)/i}")

#pass
for i in range(1,10):
   pass 
    



