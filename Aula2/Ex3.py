#Exercício 3

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = b**2 - 4*a*c
# Calcula as raízes
raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)

print(f"Raiz 1: {raiz1}")
print(f"Raiz 2: {raiz2}")
print(f"O valor de Δ (discriminante) é: {delta}")
