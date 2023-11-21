
print("Escolha a unidade de temperatura:")
print("1. Kelvin (K)")
print("2. Celsius (C°)")
print("3. Fahrenheit (F°)")
escolha_origem = input("Digite a unidade de temperatura de origem (K/C/F): ")
escolha_destino = input("Digite a unidade de temperatura de destino (K/C/F): ")
temperatura = float(input("Digite a temperatura: "))
# Realizar as conversões diretamente
match (escolha_origem, escolha_destino):
    case ('K', 'C'):
        resultado = temperatura - 273.15
    case ('K', 'F'):
        resultado = (temperatura - 273.15) * 9/5 + 32
    case ('C', 'K'):
        resultado = temperatura + 273.15
    case ('C', 'F'):
        resultado = temperatura * 9/5 + 32
    case ('F', 'K'):
        resultado = (temperatura - 32) * 5/9 + 273.15
    case ('F', 'C'):
        resultado = (temperatura - 32) * 5/9
print(f"\nA temperatura convertida é: {resultado:.2f} {escolha_destino}")