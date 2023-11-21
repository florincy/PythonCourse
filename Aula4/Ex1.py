#Exercício 1

# Tabuada do 5 usando um loop for
print("Tabuada do 5 usando for:")
for i in range(0, 11):
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")

# Tabuada do 5 usando um loop while
print("\nTabuada do 5 usando while:")
i = 0
while i <= 10:
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")
    i += 1