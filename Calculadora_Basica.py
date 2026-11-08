print("CALCULADORA")
print("-" * 20)

n = 0

while n != 2:
    print("Informe um número")
    nota = int(input())
    n += 1

print("""=====MENU=====\n
1 -> SOMA\n
2 -> SUBTRAÇÃO\n
3 -> MULTIPLICAÇÃO\n
4 -> DIVISÃO\n
""")
print("Qual a operação que deseja? (Informe de 1 a 4 respectivamente)")
opcao = input("")

match opcao:
    case 1:
        print("Somando...")
        soma = nota + nota
        print(f"Soma -> {soma}")
