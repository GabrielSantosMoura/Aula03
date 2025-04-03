fuel  = input("Vai abastecer com Etanol ou Gasolina? Digite E para etanol e G para gasolina ")
litros = float(input(f"Quantos litros de {fuel} "))
gas = 5.8
etanol = 4.9

if fuel == "G" or fuel == "g":
    valor = litros * gas
else:
    valor = litros * etanol
    print(f"Você gastou {valor}")

