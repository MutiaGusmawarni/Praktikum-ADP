print('Nama : Mutia Gusmawarni')
print('NIM  : 2310431030')
print('Shift: 4')
print('')
n = int(input('banyak data : '))

V0 = []
for i in range (n):
	x = int(input('input kec awal : '))
	V0.append(x)
a = []
for i in range (n):
	k = int(input('input percepatan : '))
	a.append(k)
t = []
for i in range (n):
	g = int(input('input waktu : '))
	t.append(g)

Vakhir = []
S = []
def hitung_kecakhir_jarak(a, t, V0):
	V2 = a*t + V0
	jarak = (V0*t) + (a*t*t*1/2)
	return V2, jarak
for i in range (n):	
	V2, jarak = hitung_kecakhir_jarak(a[i], t[i], V0[i])
	Vakhir.append(V2)
	S.append(jarak)


print('-'*77)       
print('|Kecepatan Awal|  Percepatan  |    Waktu     |Kecepatan Akhir|    Jarak     |')
print('-'*77)
for i in range (n):
    print(f'|{V0[i] :<14}|{a[i] :<14}|{t[i] :<14}|{Vakhir[i] :<15}|{S[i] :< 14}|')
print('-'*77)
