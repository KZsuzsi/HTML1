#elágazások
#egyszerű egyirányú elágazás : ha (feltétel)--> utasítás
'''
if feltétel. -- ha az adott feltétel teljesül az if alatt lévő utasítás fog lefutni utasítás

else:        -- ha az adott feltétel nem teljesül (minden más esetben), akkor az else alatt lévő utrasítás fut


Mindaz, ami az if-hez tartoziik(Ami a feltétel teljesülése után végre akarunk hajtani, az egy tabulátorral)

Logikai ÉS and: akkor igaz, ha mindkét feltétel igaz
Logikai VAGY or: akkor igaz, ha legalább egy tag igaz
Logikai tagadás negáció: not vagy !
'''
'''
A = True
B = True
if A == True and B == True: #mivel az if-be akkor lép bele, ha true, ezért a logikai operátorokoknak nem kell......
    print("mindkettő igaz")
if A or B:
    print("legalább az egyik igaz")
szam= int(input("Kérek egy számot "))
if szam >= and szam <= 15   #............


egesz= int(input("Kérek egy egész számot: "))
if egesz <0:
    print("A megadott szám negatív")
    print("A szám abszolútértéke: ", (-1*egesz))
elif egesz == 0:                                   #ha több feltétel van, akkor elif
    print("A szám nulla")
else:
    print("A megadott szám nem negatív")           #else mögé már nem teszünk feltételt
    print("A szám abszolútértéke: ", (egesz))

    #logikai operátorok
#                                                          3-25
-------------------------------------------------------------------------------------------------------------------------------
#3. feladat
a = int(input("kérek egy egész számot: " ))
print(a%10)
if a%10 == 0:
    print("Osztható 10-zel")

#4.feladat
számláló = int(input("Kérek két egész számot! \n Első: "))
nevező = int(input("Második: "))
if nevező == 0:
    print(" hiba üzent")
else:
    print("számláló: ", számláló)
    print("nevező: ", nevező)

#5. feladat
szam = int(input("Kérek egy háromjegyű pozitív egész számot! "))
a = szam//100
maradek = szam%100
b = maradek//10
c = maradek%10

if szam == a**3 + b**3 + c**3:
    print("Armstrong szám!")
else:
    print("nem  Armstrong szám!")

#6. feladat
a = int(input("Kérek egy egész számot: " ))
if a == 4:
    print("A megadott szám a 4-es")
else:
    print("")
if a < 10:
    print("A megadott szám kisebb mint 10.")
if a%2 == 0:
    print("A megadott szám páros.")

if a >= 0 and a <= 10:
    print("A megadott szám a [0,10] intervallumba esik")

#7. feladat
a = int(input("Kérek két egész számot! \nElső: "))
b = int(input("Második: "))
if a == b:
    print("A két szám egyenlő.")
if a%2 and b%2 > 0:
    print("Mind a két szám páratlan.")
if a%3 or b%3 == 0:
    print("Legalább az egyik szám osztható hárommal.")
if a and b < 0:
    print("Mind a két szám negatív.")
if ((a>0 and b<0))or(a<0 and(b>0)):
    print("Az egyik szám negatív, a másik szám pozitív.")

#8. feladat
a = int(input("Kérem a téglalap méretét! \nelső: "))
b = int(input("második: "))
if a == b:
    print("négyzet")
else:
    print("téglalap")

#9. feladat
a = int(input("Kérem egy 3szög 3 oldalát! \nElső: "))
b = int(input("Második: "))
c = int(input("Harmadik: "))
if a==b or a==c or b==c:
    print("szabályos háromszög")
else:
    print("nem szabályos háromszög")

#10. feladat
a = int(input("Kérek egy egész számot: " ))
if a == 10 or 100 or 1000:
    print("A megadott szám  egyenlő 10-zel, 100-zal vagy 1000-rel!")
else: 
    print("A megadott szám nem  egyenlő -e 10-zel, 100-zal vagy 1000-rel!")

#11. feladat
a = int(input("Kérek egy számot!"))
if a>=1 and a<=10:
    print("A megadott szám benne van az [1,9] intervallumban.")
else:
    print("A megadott szám nincs benne az [1,9] intervallumban.")

#12. feladat
a = int(input("Kérek egy számot!"))
if a<0 and a%2!=0:
    print("negatív páratlan szám")

#13. feladat
a = int(input("Kérek két egész számot \nElső: "))
b = int(input("Második: "))

#14. feladat
a = int(input("Kérek egy pozitív számot! "))
if a>0:
    a**0.5
else:
    print("a gyökvonás csak nem negatív számok esetén értelmezett művelet.")

#15. feladat
a = int(input("Kérek három számot, hogy csinálhassunk egy háromszöget! Első: "))

#16. feladat
km = int(input("Hány km-t tett meg?: "))
ido = int(input("Mennyi idő alatt?: "))
if km/ido > 145 or km/ido < 80:
    print("Nem megfelelő sebességgel közlekedett!")
else:
    print("Minden rendben")

#17. feladat
a = int(input("Kérek egy egész számot! "))
if a < 0:
    print("-" (a))
elif a > 0:
    print("+ " (a))
elif a == 0:
    print(" ")

#18. feladat
a = int(input("Kérek két számot! Első: "))
b = int(input("Második: "))
if a < b:
    print(str((a) ("<") (b)))
elif a > b:
    print(str((a) (">") (b)))
else:
    print(str((a) ("=") (b)))

#19. feladat
homerseklet = int(input("víz hőmérséklete: "))
if homerseklet < 0:
    print("Szilárd (jég)")
elif homerseklet > 0 and homerseklet < 100:
    print("folyékony (víz)")
elif homerseklet < 100:
    print("légnemű (gőz)")

#20. feladat
a = int(input("Kérek két tetszőleges pontot! Első: "))
b = int(input("Második: "))
if a and b > 0:
    print("Első síknegyed")
elif a and b < 0:
    print("Harmadik síknegyed")
elif a > 0 and b < 0:
    print("negyedik síknegyed")
elif a < 0 and b > 0:
    print("Második síknegyed")

#21. feladat
a = int(input("hány pontot értél el?: "))
if a <= 42:
    print("Elégtelen lett a dolgozata mert a pontszáma: " (a))
elif a <= 57 and a > 42:
    print("elégséges lett a dolgozata mert a pontszáma: " (a))
elif a <= 72 and a > 57:
    print("közepes lett a dolgozata mert a pontszáma: " (a))
elif a <= 87 and a > 72:
    print("jó lett a dolgozata mert a pontszáma: " (a))
elif a > 87:
    print("jeles lett a dolgozata mert a pontszáma: " (a))

#22. feladat
a = float(int(input("Kérek egy pozitív egész számot: ")))
if a <= 13:
    print("gyerek")
elif a <= 17 and a > 13:
    print("fiatalkorú")
elif a <= 23 and a> 17:
    print("Ifjú")
elif a <= 59 and a > 23:
    print("Felnőtt")
elif a > 60:
    print("Idős")

#23. feladat
af = int(input("Kérek egy számot, ami megadja a folyadék sűrűségét!: "))
bt = int(input("Kérek egy számot, ami megadja a tárgy sűrűségét! "))
if bt > af:
    print("elmerül")
elif bt < af:
    print("úszik")
elif bt == af:
    print("lebeg")

#24. feladat
a = int(input("Igazolatlan száma: "))
if a == 0:
    print("5")
elif a > 0 and a <= 3:
    print("4")
elif a > 3 and a <= 9:
    print("3")
elif a > 10:
    ev = int(input("Kérem a születési évét!: "))
    if (2022 - ev) < 18:
        print("szülői értesítés szükséges")
    elif (2022 - ev) >= 18:
        print("felszólítás kiküldése szükséges")
'''
#25. feladat




