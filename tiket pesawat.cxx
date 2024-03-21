#include<iostream>
using namespace std;
string nama, umur, gender;
	int tujuan, maskapai, kursi;
	float diskon; 
	int Total, Harga, Total_setelah_diskon;


int main () {
	
	cout<<("^^^^PROGRAM PEMBELIAN TIKET PESAWAT MUTIA GUSMAWARNI^^^^")<<endl<<endl;
	
	cout<<("Silahkan Masukkan Data Diri Anda")<<endl;
	cout<<"Nama : ";
	getline(cin, nama);
	cout<<"Umur : ";
	getline(cin, umur);
	cout<<"Jenis kelamin : ";
	cin>>gender;
	cout<<endl;

	cout<<"Silahkan Pilih Tujuan Anda"<<endl;
	cout<<"1. Medan"<<endl;
	cout<<"2. Jakarta"<<endl;
	cout<<"3. Pekanbaru"<<endl;
	
	cout<<"Tujuan yang dipilih (cukup masukkan nomor tujuan) : ";
	cin>>tujuan;
	cout<<endl;

if (tujuan == 1) {
	cout<<"                 ☆DAFTAR HARGA TIKET☆"<<endl;
	cout<<"Tujuan :          Padang --> Medan"<<endl;
	cout<<("|-------------------------------------------------------|")<<endl;
	cout<<("| NO |        Maskapai         |        Harga tiket     |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 1. |        Economy          |       Rp. 1.020.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 2. |        Business         |       Rp. 2.000.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 3. |       First Class       |       Rp. 3.000.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<endl;}
	
else { if(tujuan == 2) {
	cout<<"                 ☆DAFTAR HARGA TIKET☆"<<endl;
	cout<<"Tujuan :          Padang --> Jakarta"<<endl;
	cout<<("|-------------------------------------------------------|")<<endl;
	cout<<("| NO |        Maskapai         |        Harga tiket     |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 1. |        Economy          |       Rp. 1.020.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 2. |        Business         |       Rp. 2.000.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 3. |       First Class       |       Rp. 3.000.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<endl;}
	
else { if(tujuan == 3) {
	cout<<"                 ☆DAFTAR HARGA TIKET☆"<<endl;
	cout<<"Tujuan :          Padang --> Pekanbaru"<<endl;
	cout<<("|-------------------------------------------------------|")<<endl;
	cout<<("| NO |        Maskapai         |        Harga tiket     |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 1. |        Economy          |       Rp. 1.020.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 2. |        Business         |       Rp. 2.000.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<("| 3. |       First Class       |       Rp. 3.000.000    |")<<endl;
	cout<<("|----|--------------------------------------------------|")<<endl;
	cout<<endl;}

else {cout<<"Maaf Pilihan Tidak Ada";}}}
	
	cout<<"Maskapai yang dipilih (cukup masukkan nomor maskapai) : ";
	cin>>maskapai;
	cout<<endl;
	
	if ( maskapai == 1 ) {cout<<"Anda memilih Economy class dengan harga Rp. 1.020.000";}
	else { if ( maskapai == 2) {cout<<"Anda memilih Business class dengan harga Rp. 2.000.000";}
	else { if ( maskapai == 3) {cout<<"Anda memilih First class dengan harga Rp. 3.000.000";}}}
	cout<<endl;
	
	if ( tujuan == 1 & maskapai == 1) {Harga = 1020000;}
	else { if ( tujuan == 1 & maskapai == 2) {Harga = 2000000;}
	else { if ( tujuan == 1 & maskapai == 3) {Harga = 3000000;}
	else { if ( tujuan == 2 & maskapai == 1) {Harga = 1020000;}
	else { if ( tujuan == 2 & maskapai == 2) {Harga =2000000;}
	else { if ( tujuan == 2 & maskapai == 3) {Harga = 3000000;}
	else { if ( tujuan == 3 & maskapai == 1) {Harga = 1020000;}
	else { if ( tujuan == 3 & maskapai == 2) {Harga = 2000000;}
	else { if ( tujuan == 3 & maskapai == 3) {Harga = 3000000;}}}}}}}}}
	
	cout<<endl;
	cout<<"Jumlah kursi yang dipesan : ";
	cin>>kursi;
	
	Total = Harga*kursi;
	
	if(kursi>=3) {
		diskon = Total*0.25;
		Total_setelah_diskon = Total-diskon;
		cout<<"Diskon yang didapatkan : "<<diskon<<endl;
		cout<<"Total harga setelah diskon : Rp."<<Total_setelah_diskon<<endl;
	}
	else {
		diskon=0;
		Total_setelah_diskon = Total-diskon;
		cout<<"Maaf, anda tidak mendapatkan diskon"<<endl;
		cout<<"Total harga : Rp."<<Total_setelah_diskon<<endl;
	}
	
	cout<<endl;
	cout<<"Nama           : "<<nama<<endl;
	cout<<"Umur           : "<<umur<<endl;
	cout<<"Jenis Kelamin  : "<<gender<<endl;
	cout<<"================================="<<endl;
	cout<<"Kota Tujuan    : ";
	if (tujuan == 1 ) {cout<<"Medan";}
	else {if (tujuan == 2) {cout<<"Jakarta";}
	else {if (tujuan ==3) {cout<<"Pekanbaru";}}}
	cout<<endl;
	
	cout<<"Jenis Maskapai : ";
	if (maskapai == 1) {cout<<"Economy";}
	else {if (maskapai == 2) {cout<<"Business";}
	else {if (maskapai == 3) {cout<<"First class";}}}
	cout<<endl;
	
	
	cout<<"Jumlah Tiket   : "<<kursi<<endl;
	cout<<"Total Harga    : Rp."<<Total_setelah_diskon<<endl;
	
	
}