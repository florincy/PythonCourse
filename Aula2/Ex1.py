#Exercício 1
nome = input("Digite o nome do estudante: ")
idade = int(input("Digite a idade do estudante: "))
cpf = input("Digite o CPF do estudante: ")
status_matricula = input("Digite o status da matrícula (True para ativa, False para trancada): ")
# Exibe na tela todas as informações do estudante cadastrado
print("\nInformações do estudante cadastrado:")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"CPF: {cpf}")
print(f"Status da Matrícula: {status_matricula}")
