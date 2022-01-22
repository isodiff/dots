#####
#
#* Kod na zamianę liczb rzymskich na arabskie oraz arabskich na rzymskie
#
#####

def arabnarzym():
    print("\nZamiana liczb arabskich na rzymskie")
    liczbaArabskaUżytkownika= int(input("Podaj liczbę arabską: "))
    if liczbaArabskaUżytkownika > 3999:
        print("Liczba jest za duża")
    else:
        europeizowaneCyfryHinduskie = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rzym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        liczba = ''
        i = 0
        while  liczbaArabskaUżytkownika > 0:
            for _ in range(liczbaArabskaUżytkownika // europeizowaneCyfryHinduskie[i]):
                liczba += rzym[i]
                liczbaArabskaUżytkownika -= europeizowaneCyfryHinduskie[i]
            i += 1
        print(liczba)

arabnarzym()
