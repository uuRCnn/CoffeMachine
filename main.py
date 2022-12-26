from Bilgi import MENU
from Bilgi import resources

işlem_devam = True

order = input("seçiminizi yapınız = (espresso 1.5 - latte 2.5 - cappuccino 3.0): e-l-c ")

pennies = int(input("pennies($0.01): "))
nickles = int(input("nickles($0.05): "))
dimes = int(input("dimes($0.10): "))
quarters = int(input("quarters($0.25): "))
# para tutarı alındı


def para_hesapla(pennies_, nickles_, dimes_, quarters_):
    total = pennies_*0.01
    total += nickles_*0.05
    total += dimes_*0.10
    total += quarters_*0.25
    return total
#  girilen para hesaplandı


para_sonuç = para_hesapla(pennies, nickles, dimes, quarters)


def money_hesapla(order_):
    if order_ == "e":
        if para_sonuç >= MENU["espresso"]["cost"]:
            kalan_tutar = para_sonuç - MENU["espresso"]["cost"]
            print(f"kalan tutarınız: {kalan_tutar}")
            print("kahveniz hazırlanıyor...")
            return kalan_tutar
        else:
            print(f"{para_sonuç} ne yazıkki paranız yetmiyor")

    if order_ == "l":
        if para_sonuç >= MENU["latte"]["cost"]:
            kalan_tutar = para_sonuç - MENU["latte"]["cost"]
            print(f"kalan tutarınız: {kalan_tutar}")
            print("kahveniz hazırlanıyor...")
            return kalan_tutar

        else:
            print(f"{para_sonuç} ne yazıkki paranız yetmiyor")

    if order_ == "c":
        if para_sonuç >= MENU["cappuccino"]["cost"]:
            kalan_tutar = para_sonuç - MENU["cappuccino"]["cost"]
            print(f"kalan tutarınız: {kalan_tutar}")
            print("kahveniz hazırlanıyor...")
            return kalan_tutar

        else:
            print(f"{para_sonuç} ne yazıkki paranız yetmiyor")
# parası yetiyormu hesaplandı


money_hesapla(order)


def kaynak_hesapla(order_):
    if order_ == "e":
        we = resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        ce = resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        print(f"işlem sonrası makinenin suyu: {we}")
        print(f"işlem sonrası makinenin kahvesi: {ce}")

    if order_ == "l":
        wl = resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
        ml = resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
        cl = resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        print(f"işlem sonrası makinenin suyu: {wl}")
        print(f"işlem sonrası makinenin sütü: {ml}")
        print(f"işlem sonrası makinenin kahvesi: {cl}")

    if order_ == "c":
        wc = resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
        mc = resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        cc = resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        print(f"işlem sonrası makinenin suyu: {wc}")
        print(f"işlem sonrası makinenin sütü: {mc}")
        print(f"işlem sonrası makinenin kahvesi: {cc}")
# makinenin kaynakları hesaplanıyor


kaynak_hesapla(order)

while işlem_devam:
    order = input("seçiminizi yapınız = (espresso 1.5 - latte 2.5 - cappuccino 3.0): e-l-c ")
    para_sonuç = money_hesapla(order)
    money_hesapla(order)
    kaynak_hesapla(order)
    devammı = input("çıkmak istiyorsanız -off- yazın.  Devam ise : -on- yazın: ")
    if devammı == "off":
        işlem_devam = False

