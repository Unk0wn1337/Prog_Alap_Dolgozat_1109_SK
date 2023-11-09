
import random
import math
# 1.
# Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)
# Kérj be 1 páros számot a felhasználótól. (1 pont)


def elsoFeladat():
    print("1.")
    szam:int =  int(input("Szeretnék kérni egy páros számot: "))
    while not szam % 2 == 0:
        szam:int = int(input("Ez nem páros! PÁROS számot kérek!: "))
    print(szam)

 # 2.
 #Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. Hány 3-mal osztható van közöttük? A kiírás formátuma: „A számok között X db 3-mal osztható van!”

def masodikFeladat():
    print("2.")
    index:int = 0
    harommalOszhatokDb:int = 0
    while index < 13:
        szam:int = math.floor(random.random()*(151-10)+10)
        print(szam,end=" ")
        if szam % 3 == 0:
            harommalOszhatokDb += 1
        index+=1
    print(f"\nA számok között {harommalOszhatokDb} db 3-mal osztható van!")

# 3.
# Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot.
# Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
# Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor!


def harmadikFeladat(text,n):
    print("3.")
    if len(text) < n:
        print("Nincsen N. karakter")

    else:
        szoveg = (text[n])
        nagySzoveg = szoveg.upper()
        print(f"A Szöveg {n}-dik karaktere {szoveg} - {nagySzoveg*3}")


# 4.
#Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
#Hány nevet adott meg a felhasználó?
#A kiírás formája: „A felhasználó 12 nevet adott meg.”

def negyedikFeladat():
    print("4.")
    nevDb:int = 0
    nevBekeres:str = str(input("Szeretnék kérni neveket: "))
    while not nevBekeres == '@':
        nevDb+=1
        nevBekeres:str = str(input("Szeretnék kérni neveket: "))
    print(f"A felhasználó {nevDb} nevet adott meg.")


# 5.
def otodikFeladat():
    print("5.")
    bekeres:str = str(input("Szeretnék kérni egy ko/papir/ollo-t"))
    felhasznalo_tippje = bekeres.lower()
    if  (felhasznalo_tippje == "ko") or (felhasznalo_tippje == "papir") or (felhasznalo_tippje == "ollo"):
        gep_tippje = math.floor(random.random()*(4-1)+1)
        if felhasznalo_tippje == "ko" and gep_tippje == 1:
            print("Döntetlen: KO vs KO")
        if felhasznalo_tippje == "ko" and gep_tippje == 2:
            print("Gép nyert: KO vs papir")
        if felhasznalo_tippje == "ko" and gep_tippje == 3:
            print("Nyertél: KO vs ollo")
        if felhasznalo_tippje == "papir" and gep_tippje == 1:
            print("Gép nyert: papir vs ko")
        if felhasznalo_tippje == "papir" and gep_tippje == 2:
            print("Döntetlen: papir vs papir")
        if felhasznalo_tippje == "papir" and gep_tippje == 3:
            print("Gép nyert: papir vs ollo")
        if felhasznalo_tippje == "ollo"and gep_tippje == 1:
            print("nyertél: ollo vs ko")
        if felhasznalo_tippje == "ollo" and gep_tippje == 2:
            print("Gép nyert: ollo vs papir")
        if felhasznalo_tippje == "ollo" and gep_tippje == 3:
            print("Döntetlen: ollo vs ollo")
    else:
        print("HIBA: csak papir, ko, ollo lehet")


