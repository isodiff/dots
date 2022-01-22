import time, calendar
from datetime import datetime

class Smartfon:
    def __init__(self, nrtelefonu, pamiec, pin):
        self.__numerTelefonu = nrtelefonu
        self.storage = pamiec
        self.pin = pin
        self.twojeKontakty = {"Numer ratunkowy":112}
        self.aplikacje = ["Chrome", "Aparat", "Telefon", "Sms", "Zegar"]
        self.histPol = {}

    def Kontakty(self):
        for osoba in self.twojeKontakty:
            print(f"Nazwa: {osoba}, Numer: {self.twojeKontakty[osoba]}")
            


    def Zadzwon(self,ktos):
        if type(ktos) == int:
            if ktos in self.twojeKontakty.values():
                nazwaKontaku = list(self.twojeKontakty.keys())[list(self.twojeKontakty.values()).index(ktos)]
                print(f"Dzwonienie do {nazwaKontaku}")
                time.sleep(5)
                print("Zakończono połączenie")
                teraz = datetime.now()
                czas = teraz.strftime("%H:%M:%S")
                self.histPol[nazwaKontaktu] = czas
            else:
                print(f"Dzwonienie do {ktos}")
                time.sleep(5)
                print("Zakończono połączenie")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                self.histPol[ktos] = current_time
        else:
            if ktos in self.twojeKontakty:
                print(f"Dzwonienie do {ktos}")
                time.sleep(5)
                print("Zakończono połączenie")
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                self.histPol[ktos] = current_time
            else:
                print("Nie ma takiego kontaktu")
    
    def WyslijSms(self,ktos,tresc):
        if type(ktos) == int:
            if ktos in self.twojeKontakty.values():
                nazwaKontaku = list(self.twojeKontakty.keys())[list(self.twojeKontakty.values()).index(ktos)]
                print(f"Wysłano wiadomość do {nazwaKontaku}")
                print(f"\n{tresc}")
            else:
                print(f"Wysłano wiadomość do {ktos}")
                print(f"\n{tresc}")
        else:
            if ktos in self.twojeKontakty:
                print(f"Wysłano wiadomość do {ktos}")
                print(f"\n{tresc}")
            else:
                print("Nie ma takiego kontaktu")
    
    def DodajKontakt(self,numer,nazwa):  
        self.storage -= 0.5
        if self.storage < 0:
            self.storage == 0
            print("Za mało miejsca na urządzeniu")
        else:
            if nazwa in self.twojeKontakty:
                print("Ten kontakt już istnieje")
            else:
                self.twojeKontakty[nazwa] = numer 
                print(f"Pomyślnie dodano kontakt {nazwa}, na dysku pozostało {self.storage} GB")

    def UsunKontakt(self,nazwa):
        del self.twojeKontakty[nazwa]

    def ZainstalujApk(self,nazwa):
        if nazwa in self.aplikacje:
            print("Ta aplikacja już jest zainstalowana")
        else:
            self.storage -= 1
            if self.storage < 0:
                self.storage == 0
                print("Za mało miejsca na urządzeniu")
            else:
                if nazwa in self.aplikacje:
                    print("Ta aplikacja już jest zainstalowana")
                self.aplikacje.append(nazwa) 
                print(f"Pomyślnie zainstalowano {nazwa}, na dysku pozostało {self.storage} GB")

    def OdinstalujApk(self,nazwa):
        if nazwa not in self.aplikacje:
            print("Ta aplikacja nie jest zainstalowana")
        else:
            self.storage += 1
            self.aplikacje.remove(nazwa) 
            print(f"Pomyślnie odinstalowano {nazwa}, na dysku pozostało {self.storage} GB")     

    def Aplikacje(self):
        for i in self.aplikacje:
            print("|",i,end=" | ")

    def Historia(self):
        print("Połączenia: ")
        for osoba in self.histPol:
            print(f"Nazwa: {osoba}, Godzina: {self.histPol[osoba]}")

    dzisMiesiac = datetime.now().month
    def Kalendarz(self,miesiac = dzisMiesiac):
        print("\n")
        dzisData = datetime.now().date()
        teraz = datetime.now()
        czas = teraz.strftime("%H:%M:%S")
        dzis = datetime.today().year
        print("     ",czas)
        print("     ",dzisData)
        print(calendar.month(dzis, miesiac))


#============================================================#

### Dodaj telefon
# tefelon = Smartfon(nrtelefonu, pamiec, pin)
tefelon = Smartfon(575575575, 128, 1234)

### Dodaj Kontakt
tefelon.DodajKontakt(345765987, "Michał")
tefelon.DodajKontakt(345765098, "Adam")

### Usuń Kontakt
tefelon.UsunKontakt("Michał")

### Wyświetl Kontakty
tefelon.Kontakty()

### Zadzwon na numer albo do Kontaktu
tefelon.Zadzwon("Adam")

### Wyslij sms na numer albo do Kontaku
tefelon.WyslijSms("Adam", "Hej!")

### Wyświetl Aplikacje
tefelon.Aplikacje()

### Zainstaluj Aplikację
tefelon.ZainstalujApk("Messenger")

### Odinstaluj Aplikację
tefelon.OdinstalujApk("Chrome")

### Wyświetl historię połączeń
tefelon.Historia()

### Wyświetl kalenarz (Funkcja wywołana bez argumentu wyświetli obecny miesiąc)
tefelon.Kalendarz(1)
