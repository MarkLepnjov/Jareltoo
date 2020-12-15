import random  # suvalise numbri generaator

basseiniotsad = []  # tühja nimekirja tekitamine
for i in range(5):  # 5 erinevat basseiniotsa kogust
    basseiniotsad.append(random.randint(30, 50))  # lisab nimekirja

meetrid = int(input("Sisestage, mitu meetrit on üks basseiniots: "))  # input kasutaja jaoks


def kalorid(ujutud, pikkus):  # funktsiooni defineerimine
    kulunud = (ujutud * pikkus / 1000) * 120
    return kulunud


kokku = 0  # muutuja egitamine
for y in range(len(basseiniotsad)):  # basseiniotste pikkusega tsükkel
    kaloreid = kalorid(basseiniotsad[y], meetrid)
    print("Kaloreid kulus: " + str(kaloreid))
    kokku = kokku + kaloreid

print("Kokku kulus " + str(round(kokku,1)) + " kalorit.")