print("Tugas Modul 5 ")
print("Nama : Mutia Gusmawarni")
print("NIM  : 2310431030")
print(" ")

def inputarray():
   
        
            inputangka = input("Masukkan bilangan bulat 0-9 (tanpa menggunakan spasi) : ")
            array = [int(angka) for angka in inputangka]
            if all(0 <= angka <= 9 for angka in array):
                return array
            else:
                print("invalid")
        

print("~Array Mawar~ ")
Mawar = inputarray()

print(" ")

print("~Array Melati~ ")
Melati = inputarray()

print(" ")

Mawarsaja = []
Melatisaja = []
irisanMawardanMelati = []

for angka in range(10):  
    if angka in Mawar and angka not in Melati:
        Mawarsaja.append(angka)
    elif angka in Melati and angka not in Mawar:
        Melatisaja.append(angka)
    elif angka in Mawar and angka in Melati:
        irisanMawardanMelati.append(angka)

print("elemen yang berada di Mawar (tidak ada di Melati):", Mawarsaja)
print("elemen yang berada di Melati (tidak ada di Mawar):", Melatisaja)
print("elemen yang berada di Mawar dan Melati:", irisanMawardanMelati)