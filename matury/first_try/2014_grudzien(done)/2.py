file = open("dane_PR/dziennik.txt", 'r')
dane = file.read().splitlines()
dane = list(map(int,dane))
najdluszy = max(dane)
najkrotszy = min(dane)
print(dane.index(najdluszy)+1)
print(dane.index(najkrotszy)+1)