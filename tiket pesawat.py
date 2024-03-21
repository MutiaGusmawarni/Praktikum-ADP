Nama= input ("Nama : ")
Umur = input ("Umur : ")
Jenis_Kelamin = input ("Jenis Kelamin : ")

print("")
print("Siahkan Pilih Tujuan Anda")
print("1. Medan")
print("2. Jakarta")
print("3. Pekanbaru")
Tujuan = int(input("Tujuan yang dipilih (cukup masukkan nomor tujuan) : "))

if Tujuan == 1:
	print("")
	print("                 ☆DAFTAR HARGA TIKET☆")
	print("")
	print("Tujuan :          Padang --> Medan")
	print("|-------------------------------------------------------|")
	print("| NO |        Maskapai         |        Harga tiket     |")
	print("|----|--------------------------------------------------|")
	print("| 1. |        Economy          |       Rp. 1.020.000    |")
	print("|----|--------------------------------------------------|")
	print("| 2. |        Business         |       Rp. 2.000.000    |")
	print("|----|--------------------------------------------------|")
	print("| 3. |       First Class       |       Rp. 3.000 000    |")
	print("|----|--------------------------------------------------|")
	
elif Tujuan == 2 :
	print("")
	print("                 ☆DAFTAR HARGA TIKET☆")
	print("")
	print("Tujuan :          Padang --> Jakarta")
	print("|-------------------------------------------------------|")
	print("| NO |        Maskapai         |        Harga tiket     |")
	print("|----|--------------------------------------------------|")
	print("| 1. |        Economy          |       Rp. 1.020.000    |")
	print("|----|--------------------------------------------------|")
	print("| 2. |        Business         |       Rp. 3.000.000    |")
	print("|----|--------------------------------------------------|")
	print("| 3. |       First Class       |       Rp. 3.000.000    |")
	print("|----|--------------------------------------------------|")
	
elif Tujuan == 3 :
	print("")
	print("                 ☆DAFTAR HARGA TIKET☆")
	print("")
	print("Tujuan :          Padang --> Pekanbaru")
	print("|-------------------------------------------------------|")
	print("| NO |        Maskapai         |        Harga tiket     |")
	print("|----|--------------------------------------------------|")
	print("| 1. |        Economy          |       Rp. 1.020.000    |")
	print("|----|--------------------------------------------------|")
	print("| 2. |        Business         |       Rp. 2.000.000    |")
	print("|----|--------------------------------------------------|")
	print("| 3. |       First Class       |       Rp. 3.000.000    |")
	print("|----|--------------------------------------------------|")
	
else : 
	print("")
	print("Maaf Pilihan Tidak Ada")

print("")	
Maskapai = int(input("Maskapai yang dipilih : "))

if Maskapai == 1:
	print("Anda memilih Economy Class dengan harga Rp. 1.020.000")
elif Maskapai == 2 :
	print("Anda memilih Business Class dengan harga Rp. 2.000.000 ")
elif Maskapai == 3 :
	print("Anda memilih First Class dengan harga Rp. 3.000.000")
else :
	print("Maaf Pilihan Tidak Ada")
	
print("")	
Kursi = int(input("Jumlah tiket yang dipesan : "))

if Tujuan == 1:
	if Maskapai == 1:
		Harga = 1020000
if Tujuan == 1:
	if Maskapai == 2:
		Harga = 2000000
if Tujuan == 1:
	if Maskapai == 3:
		Harga = 3000000
if Tujuan == 2:
	if Maskapai == 1:
		Harga = 1020000
if Tujuan == 2:
	if Maskapai == 2:
		Harga = 2000000
if Tujuan == 2:
	if Maskapai == 3:
		Harga = 3000000
if Tujuan == 3:
	if Maskapai == 1:
		Harga = 1020000
if Tujuan == 3:
	if Maskapai == 2:
		Harga = 2000000
if Tujuan == 3:
	if Maskapai == 3:
		Harga = 3000000						

Total = Kursi*Harga

print("")
if Kursi < 3:
		diskon = 0
		Total_setelah_diskon = Total - diskon
		print("Maaf, anda tidak mendapatkan diskon")
		print("Total harga : Rp.",Total_setelah_diskon)
	
else :
		diskon = Total*0.25
		Total_setelah_diskon = Total-diskon
		print("Diskon yang didapatkan : ",diskon)
		print("Total harga setelah diskon : Rp.",Total_setelah_diskon)
		
print("")
print("Nama          : ", Nama)
print("Umur          : ", Umur)
print("Jenis kelamin : ", Jenis_Kelamin)
print("=================================")
if Tujuan == 1 :
	Kota = "Medan"
elif Tujuan == 2 :
	Kota = "Jakarta"
elif Tujuan == 3 :
	Kota = "Pekanbaru"

print("Kota Tujuan   : ",Kota)
	
if Maskapai == 1 :
	Kelas = "Economy"
elif Maskapai == 2 :
	Kelas = "Business"
elif Maskapai == 3 :
	Kelas = "First Class"
	
print("Jenis Maskapai: ", Kelas)
	
print("Jumlah tiket  : ", Kursi)
print("Total Harga   : Rp.",Total_setelah_diskon)

	
