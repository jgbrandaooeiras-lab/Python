print("MENU")
print("-" * 20)

valor = -1


# Imprime na tela as opções e o while só encerra o programa quando o usuario digita 0
while valor != 0:
    print("""Opções:
    0 > Encerra o programa 
    1 > Celsius -> Fahrenheit
    2 > Fahrenheit -> Celsius
    """)
    print("Opção escolhida: ")
    valor = int(input())

    match valor:  # Quando o usuário escolhe sua opção, caí em um dos cases a seguir:
        case 0:
            print("Programa encerrado!")
        case 1:
            print("Celsius -> Fahrenheit...")
            C = float(input("Temperatura atual: "))
            F = (C * 1.8) + 32
            print(f"Em Fahrenheit: {F:.2f}")

        case 2:
            print("Fahrenheit -> Celsius")
            F = float(input("Temperatura atual: "))
            C = (F - 32) / 1.8
            print(f"Em Celsius: {C:.2f}")

        case _:
            print("Opção inválida!")
