n1 = float(input("Qual a primeira nota:"))
n2 = float(input("Qual a segunda nota:"))
n3 = float(input("Qual a terceira nota:"))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f"Aprovado, nota: {media}")
else:
    print(f"Reprovado, nota: {media}")