nome = input('Qual é seu nome: ')
idade = int(input('Qual é sua idade: '))
salario = float(input('Qual é seu salário: '))
aumento = float(input('Qual é seu percentual: '))
porcentagem = salario * (aumento / 100)
novo_salario = porcentagem + salario
print(f"Seu nome é: {nome} \n"
f"Sua idade é: {idade} anos \n"
f"Seu salário é: {salario:.2f} \n"
f"Seu percentual de aumento é: {aumento}\n"
f"Seu salário atual é: {novo_salario:.2f}")
