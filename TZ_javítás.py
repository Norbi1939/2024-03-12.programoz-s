#TZ dolgozat megoldása

#1.feladat

#2.feladat
f = open("adat.txt", "r", encoding="UTF-8")

adat = []

for sor in f:
    adat.append(sor.replace("", "\n").strip().split())

f.close()

#3.feladat

print(f"Ágota és áDÁM {len(adat)} napon keresztül játszottak korongfeldobósat")

#4.feladat
ssz = 1
összeg = 0
for nap in adat:
    print(f"{ssz}. nap: {len(nap)} dobás")
    összeg += len(nap)
    ssz += 1
print(f"Összesen {összeg}dobás volt a játék teljes ideje alatt.")

#5.feladat
maxÉrték = len(adat[0])
maxhely = 0


i = 1
while i < len(adat):
    if len(adat[i]) > maxÉrték:
        maxÉrték = len(adat[i])
        maxhely = i
    i += 1
print(f"A leghosszabb játék: {maxhely + 1}.nap ({maxÉrték}.dobás)")


#6.Feladat
Volt = False
nap = 1
for sor in adat:
    i = 0
    while i < len(sor) - 3:
        if sor[i] == "F" and sor[i + 1] == "F" and sor[i + 2] == "F" and sor[i + 3]:
            Volt == True
            break
        i += 1
    if Volt:
        break
    nap += 1
if Volt:
    print(f"Volt a feltételnek megfelelő nap ({nap}) a játék teljes ideje alatt.")
else:
    print(f"Nem volt a feltételnek megfelelő nap a játék teljes ideje alatt.")