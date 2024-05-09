barang =[["baju","lilin","gelas","beras","telur","minyak"],
[7000,5000,8000,22000,2000,16000],
[3,5,8,2,6,10]]

print('==LAPORAN KEUNTUNGAN TOKO MUTIA==')
print(' ')
print(5*'-','Tabel Harga Barang',6*'-')
print(31*'-')
print("| Barang  |  Harga  |  Stok   |")
print(31*'-')

for j in range (6):
	print(f"|{barang[0][j]:<9}|{barang[1][j]:<9}|{barang[2][j]:<9}|")
	print(31*'-')
 
P = []
for j in range (6):
	profit = barang[1][j]*barang[2][j]
	print('jumlah keuntungan ke ', j, ': Rp.', profit)
	P.append(profit)
	
barang2 = ["baju","lilin","gelas","beras","telur","minyak"]
profit_tertinggi = P[0]
barangtertinggi = barang2[0]
for i in range (len(P)):
	if ( P[i] > profit_tertinggi):
		profit_tertinggi = P[i]
		barangtertinggi = barang2[i]
		
profit_terkecil = P[0]
barangterkecil = barang2[0]
for i in range (len(P)):
	if ( P[i] < profit_terkecil):
		profit_terkecil = P[i]
		barangterkecil = barang2[i]
print('')
	
print(f'Barang dengan keuntungan terbesar yaitu {barangtertinggi}, sebesar Rp.{profit_tertinggi}')
print(f'Barang dengan euntungan terkecil yaitu {barangterkecil}, sebesar Rp.{profit_terkecil}')
			
Total = sum(P)

print(' ')
print('Total Keuntungan yang diperoleh : Rp.',Total)
	


