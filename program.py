# v.1.0 dzialajacej aplikacji

wiek = input("Podaj wiek uzytkownika: ")
# sprawdzenie czy wiek jest liczba calkowita
if wiek.isdigit() == False:
    exit("Wiek musi byc liczba calkowita. Zamykam aplikacje")
wiek=int(wiek)
if wiek >= 18 and wiek<=40:
    print("Witamy w apce. Mozesz kupowac u nas alkohol")
elif wiek>40 and wiek<=120:
    print("Witamy w apce. Mozesz kupowac u nas alkohol")
    print("Prosze korzystaj z produktu z umiarem")
elif wiek>120:
    print("Witamy w apce. Mozesz kupowac u nas alkohol")
    print("W twoim wieku alkohol? Masz zdrowie...")
else:
    a = 18 - wiek
    print("Jestes za mlody/a na alkohol. Zapraszamy za",a,"lat/a")
    exit
