czy_jest_pierwsza = True
a = 47
for x in range(2,a):
    if a % x == 0:
        czy_jest_pierwsza = False

if czy_jest_pierwsza:
    print(f'{str(a)} jest liczba pierwsza')
else:
    print(f'{str(a)} nie jest liczba pierwsza')