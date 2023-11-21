#Exercício 4
def tabuada(n):
    print(f"Tabuada do {n} usando for:")
    for i in range(0, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")

def main():
    for i in range(0, 11):
	    tabuada(i)
          
if __name__ == "__main__":
	main()
