file = open("liczby.txt", 'r')
dane = file.read().splitlines()
cyfry = {'0':0,'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, 'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}
for wiersz in dane:
    sze = hex(int(wiersz))
    sze = sze[2:len(sze)]
    sze = sze.upper()
    for znak in sze:
        cyfry[znak] += 1
print(cyfry)

