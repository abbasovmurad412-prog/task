
balance = 500

while True:
    print("\n1. Balansı göstər")
    print("2. Pul yatır")
    print("3. Pul çıxar")
    print("4. Çıxış")

    choice = input("Seçiminizi edin: ")

    if choice == "1":
        print("Balans:", balance, "AZN")

    elif choice == "2":
        amount = float(input("Yatırılacaq məbləğ: "))

        if amount <= 0:
            print("Yanlış məbləğ")
        else:
            balance += amount
            print("Pul yatırıldı")

    elif choice == "3":
        amount = float(input("Çıxarılacaq məbləğ: "))

        if amount <= 0:
            print("Yanlış məbləğ")
        elif amount > balance:
            print("Balansda kifayət qədər vəsait yoxdur")
        else:
            balance -= amount
            print("Pul çıxarıldı")

    elif choice == "4":
        print("Son balans:", balance, "AZN")
        break

    else:
        print("Belə seçim yoxdur")
