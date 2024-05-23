def rumus(tgl, ket, jumlah, tipe):
    with open('muti.txt', 'a') as file:
        file.write(f'{tgl}, {ket}, {jumlah}, {tipe}\n')
        print("data telah ditambahkan")
        print()

def delete(tgl):
    with open('muti.txt', 'r') as file:
        baris = file.readlines()
    with open('muti.txt', 'w') as file:
        for i in baris:
            if i.strip().split(',')[0] != tgl:
                file.write(i)
        print('Data telah dihapus')
        print()

def tampilan():
    with open('muti.txt', 'r') as file:
        baris = file.readlines()
        print('Data Keuangan Pribadi Mutia')
        print('-'*59)
        print('|   Tanggal    |    keterangan     | Jumlah |    Tipe     |')
        print('-'*59)
        for i in baris:
            tgl, ket, jumlah, tipe = i.strip().split(',')
            print(f'|{tgl:<14}|{ket:<19}|{jumlah:<8}|{tipe:<13}|')
            print('-'*59)
        print()

while True:
    print('Pilih :')
    print('1. Tambah')
    print('2. Hapus')
    print('3. Tampilkan')
    print('4. Keluar')

    pilih = int(input('pilihan (1/2/3/4):'))
    if pilih == 1:
        tgl = input('Masukkan tanggal transaksi (HH/BB/TT) :')
        ket = input('Masukkan keterangan transaksi :')
        jumlah = input('Masukkan jumlah transaksi :')
        tipe = input('Masukkan tipe transaksi (Pemasukan/Pengeluaran) : ')
        rumus(tgl, ket, jumlah, tipe)
    elif pilih == 2:
        tgl = input('Masukkan tanggal transaksi yang ingin dihapus :')
        delete(tgl)
    elif pilih == 3:
        tampilan()
    elif pilih == 4:
        print('Terima Kasih')
        print()
        break
    else:
        print('Tidak valid')
        print()