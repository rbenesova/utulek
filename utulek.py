def vytvor_utulek():
    return{
        "micí" : {"druh":"kočka", "vek":3},
        "theo" : {"druh":"pes", "vek":5},
    }

def pridej_zvire(jmeno, druh, vek):
    utulek[jmeno] ={"druh": druh, "vek": vek}
jmeno = input("zadejte jmeno zvirete")
druh = input("zadejte druh")
vek = input("zadejte vek")
pridej_zvire(jmeno,druh,vek)
def vypis_zvirata(utulek):
    for jmeno, druh, vek in utulek.items():
        print(f"{jmeno} je {druh} a je ji/mu {vek}")

utulek = vytvor_utulek()
print("vsechna zvirata")
vypis_zvirata(utulek)