#Exercicio 2
a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))
c = float(input("Digite o valor do lado c: "))

if a + b > c and a + c > b and b + c > a:
    # Verifica se os lados formam um triângulo
    if a == b == c:
        print("É triângulo equilátero")  # Três lados iguais
    elif a == b or a == c or b == c:
        print("É triângulo isósceles")  # Dois lados iguais
    else:
        print("É triângulo escaleno")    # Todos os lados diferentes
else:
    print("Não é um triângulo")