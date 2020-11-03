# zmienna 1 = a
# zmienna 2 = b
# wielokrotność = w

a = 21
b = 37
if a > b:
    w = a
else:
    w = b

while w > 0:
    if w % a == 0 and w % b == 0:
        print("NWW=" + str(w))
        break
    w += 1

