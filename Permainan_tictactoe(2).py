#Modul 9 Animasi
import time
from termcolor import colored

#Modul 7 Fungsi
#Modul 8 File Text
def nyimpandata(pemain1, pemain2, menang):
    #Modul 8 Dictionary
    game_data = {
        'Pemain 1': pemain1,
        'Pemain 2': pemain2,
        'Pemenang': menang,
    }
    with open('mz.txt', 'a') as file:
        for key, value in game_data.items():
            file.write(f'{value},')
        file.write('\n')

def tampilandata():
    with open('mz.txt', 'r') as file:
        baris = file.readlines()
        print('Hasil Permainan')
        print('-'*38)
        print('|Nama pemain 1|Nama Pemain 2|Pemenang|')
        print('-'*38)
        for i in baris:
            value = i.strip().split(',')
            print(f'|{value[0]:<13}|{value[1]:<13}|{value[2]:<8}|')
        print('-'*38)
        print()

time.sleep(1)
#Modul 1 Pengenalan Program
print('Selamat Datang di Permainan Tic Tac Toe!')
time.sleep(1)
print('Permainan ini dimainkan oleh dua orang dengan menginputkan nomor 1-9')
print()

while True:
    time.sleep(1)
    print('Pilih 1 atau 2')
    time.sleep(1)
    print('1. Mulai permainan')
    print('2. Keluar')
    print()
    time.sleep(1)
    pilihan = int(input("Masukkan nomor 1 atau 2 = "))

    #Modul 2 Pengkondisian
    if pilihan == 1:
        print()
        time.sleep(1)
        pemain1 = input('Nama Pemain 1 : ')
        pemain2 = input('Nama Pemain 2 : ')
        print()
        time.sleep(1)

        #Modul 6 Array 2D
        nomorpapan = [['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']]
        print('Ini adalah tampilan papan Tic Tac Toe yang akan dimainkan dengan menginputkan nomor 1-9')
        time.sleep(1)
        print('|===========| ')
        time.sleep(1)
        #Mpdul 4 Perulangan Bersarang
        for baris in nomorpapan:
            for elemen in baris:
                print(f'|{elemen:<3}', end='')
            print('|')
        print('|===========| ')
        print()

        #Modul 5 Array 1D
        papan = [' '] * 9

        def tampilan_papan():
            print(f'''
            | {warna(papan[0])} | {warna(papan[1])} | {warna(papan[2])} |
            | {warna(papan[3])} | {warna(papan[4])} | {warna(papan[5])} |
            | {warna(papan[6])} | {warna(papan[7])} | {warna(papan[8])} |
            ''')

        def warna(simbol):
            if simbol == 'X':
                return colored(simbol, 'red')
            elif simbol == 'O':
                return colored(simbol, 'blue')
            else:
                return simbol

        def inputXO(namapemain):
            while True:
                try:
                    posisi = int(input(f'{namapemain}, pilih nomor untuk letakkan {colored("X", "red") if namapemain == pemain1 else colored("O", "blue")} : ')) - 1
                    if 0 <= posisi < 9 and papan[posisi] == ' ': 
                        return posisi
                    else:
                        print('Posisi sudah terisi atau tidak valid. Pilih posisi lain.')
                except ValueError:
                    print('Masukkan hanya nomor 1-9.')

        def cek_menang():
            for simbol in ['X', 'O']:
                global menang
                #Modul 4 Pengkondisian Bersarang
                if (papan[0] == papan[1] == papan[2] == simbol or
                    papan[3] == papan[4] == papan[5] == simbol or
                    papan[6] == papan[7] == papan[8] == simbol or
                    papan[0] == papan[3] == papan[6] == simbol or
                    papan[1] == papan[4] == papan[7] == simbol or
                    papan[2] == papan[5] == papan[8] == simbol or
                    papan[0] == papan[4] == papan[8] == simbol or
                    papan[2] == papan[4] == papan[6] == simbol):
                    if simbol == "X":
                        namapemenang = pemain1
                        menang = pemain1
                    else:
                        namapemenang = pemain2
                        menang = pemain2
                    print( colored(f'Selamat {namapemenang}, Anda memenangkan permainan!', 'green'))
                    print()
                    return True
            return False

        time.sleep(1)
        print(f'Terima Kasih telah bergabung {pemain1} dan {pemain2}!')
        time.sleep(1)
        print()
        print(f'Dalam permainan ini, {pemain1} akan menjadi {colored("X", "red")} dan {pemain2} akan menjadi {colored("O", "blue")}')
        time.sleep(1)
        print('Silakan bergantian untuk memilih posisi. Papan permainan ditampilkan di bawah.')
        print()

        tampilan_papan()
        
        #Modul 3 Perulangan
        for i in range(9):
            if i % 2 == 0:
                pemain = pemain1 
                simbol = 'X'
            else:
                pemain = pemain2
                simbol = 'O'
            print(f'Giliran {pemain}, pilih posisi yang ingin diisi')
            index = inputXO(pemain)
            papan[index] = simbol

            tampilan_papan()

            if cek_menang():
                nyimpandata(pemain1, pemain2, menang)
                break

        else:
            print('Permainan seri. Tidak ada pemenang.')

    elif pilihan == 2:
        tampilandata()
        print('Terima kasih telah bermain!')
        break
    else:
        print('Masukkan hanya nomor 1 atau 2.')