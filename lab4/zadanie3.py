with open("daneZad3.txt", "r+") as plik:
    zdania = ["Mieszko I", "Bolesław Chrobry", "Mieszko II"]
    for zdanie in zdania:
        plik.write(zdanie + "\n")
        print(zdanie)

