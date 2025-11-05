# Faça um programa para calcular a média de 2 notas e mostrar essa média e o nome do aluno.


aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("digite a primeira nota do aluno: "))
nota_2 = float(input("digite a segunda nota do aluno: "))

media = (nota_1 + nota_2)/2

if media >= 7:
    print(f"{aluno} você esta Aprovado!!!")

elif media <= 4:
    print(f"{aluno} você esta Reprovado!!!")

else:
    print(f"{aluno} você esta Recuperação!!!")

print("olá", aluno, "sua média é: ", media)


