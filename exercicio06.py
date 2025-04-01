team1 = input("Qual o primeiro time?")
goal1 = int(input(f"Qantos gols o {team1} fez?"))
team2 = input("Qual o primeiro time?")
goal2 = int(input(f"Qantos gols o {team2} fez?"))

if goal1 == goal2:
    print(f"Os times {team1} e {team2} empataram!")
else:
    if goal1 > goal2:
        print(f"O {team1} é venceu!")
    else:
        print(f"O {team2} venceu!")

