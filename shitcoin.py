from random import *
from time import sleep

para = 1000

class randomcoin():
    fiyat = random()*100
    alisfiyat = fiyat/100*102
    satisfiyat = fiyat/100*99
    eldevar = 0

def fiyatdegisimi(coindeger, alisdeger, satisdeger):
    degerler = ["azalma","artma","değişme"]
    şans = randint(0,101)    
    secim = choice(degerler)
    print(şans)
    if 5 > şans:
        paradegisimi = coindeger-0.0001
        secim = "azalma"
    elif 92>şans:
        paradegisimi = random()*randint(0,10)
    elif 96>şans:
        paradegisimi = random()*randint(0,100)
    elif 97>şans:
        paradegisimi = random()*randint(0,1000)
        secim = choice(["azalma", "değişme"])
    elif 100>şans:
        paradegisimi = random()*randint(0,1000)
        secim = "artma"
    elif şans == 100:
        paradegisimi = random()*randint(0,10000)
    elif şans == 101:
        paradegisimi = random()*randint(0,100000)

    if secim=="azalma":
        if coindeger-paradegisimi<=0:
            paradegisimi = coindeger-0.00001
            coindeger -= paradegisimi
            secim = "-"
        else:
            coindeger -= paradegisimi
            secim = "-"

    elif secim =="artma":
        coindeger += paradegisimi
        secim = "+"

    elif secim=="değişme":
        paradegisimi = 0
        coindeger == coindeger
        secim = "="

    alisdeger = coindeger/100*102
    satisdeger = coindeger/100*99
    return coindeger, alisdeger, satisdeger, secim, paradegisimi

   
tur = 1
while True:
    eskifiyat = randomcoin.fiyat
    if tur > 1:
        randomcoin.fiyat, randomcoin.alisfiyat, randomcoin.satisfiyat, degisim, paradegisimi=fiyatdegisimi(randomcoin.fiyat, randomcoin.alisfiyat, randomcoin.satisfiyat)
    else:
        degisim = "="
        paradegisimi = 0
    print("------------------------------------\n")
    print(f"randomcoinfiyat: {randomcoin.fiyat}|{degisim}{paradegisimi}")
    print(f"elde olan randomcoin: {randomcoin.eldevar}")
    sleep(0.1)
    print("------------------------------------")
    print(f"randomcoin alis: {randomcoin.alisfiyat}")
    print(f"randomcoin satis: {randomcoin.satisfiyat} |bakiye: {round(para, 2)}")
    print("------------------------------------")
    while True:
        print("işlem seçin:\nrandomcoin al-miktar|randomcoin sat-miktar|geç")
        
        user_input=input(">")
        user_input=user_input.split("-")

        if user_input[0]=="randomcoin al":
            user_input[1]=float(user_input[1])
            if para>=randomcoin.alisfiyat*user_input[1]:
                para-=randomcoin.alisfiyat*user_input[1]
                randomcoin.eldevar+=user_input[1]
                break

            else:
                print("paranız yetersiz")
        
        if user_input[0]=="randomcoin sat":
            user_input[1]=float(user_input[1])
            if randomcoin.eldevar>=user_input[1]:
                randomcoin.eldevar-=user_input[1]
                para+=user_input[1]*randomcoin.satisfiyat
                break

            else:
                print("elinizde yeterince coin yok")

        if user_input[0]=="geç":
            break
    
    tur += 1
