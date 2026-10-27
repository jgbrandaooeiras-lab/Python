print("Informe seu nome")
Nome = input("").strip().title()

# Variaveis responsáveis por dar inico ao bloco de repetiçãoi while
n = 0
c = 1
soma = 0

# Bloco responsável por cadastrar as notas do aluno e efetuar a soma
while n != 3:
    print(f"Informe sua {c}ª nota")
    nota = float(input())
    while (
        nota < 0 or nota > 10
    ):  # Verifica se nota é menor que 0 ou maior 10, sendo isso impossivel
        print("nota inválida, valores aceitos entre 0 e 10!")
        nota = float(input("troque está nota.: "))
    c += 1
    n += 1
    soma += nota

# Calcula a media e devolve ao usuário a media
media = soma / n
print(f"Aguarde usuário {Nome}...")
print(f"Media: {media:.2f}")


print("""Apurando situação...
Maior que 7, aprovado!\n
Maior que 6, Recuperação!\n
Menor que 6, reprovação!
""")

# Bloco que verifica a condição do aluno, e informa se foi aprovado, recuperação ou reprovado
if media >= 7:
    print(f"Aluno aprovado com media {media:.2f}")

elif media >= 6:
    print(f"Aluno ficou de recuperação com media {media:.2f}")

else:
    print(f"Aluno reprovado com media de {media:.2f}")

print("Programa encerrado...")
