#include <iostream>

using namespace std;

int main() {
    cout<<"Nama : Mutia Gusmawarni"<<endl;
    cout<<"NIM  : 2310431030"<<endl;
    cout<<"Program Menampilkan Pola Piramida Alphabet"<<endl;
    cout<<"=========================================="<<endl;
    int m, i, j;
    char huruf;
    cout << "Masukkan jumlah huruf pada piramida: ";
    cin >>m;

    for ( i = 1; i <= m; i++) {
        huruf = 'A';
        

        for (j = 1; j <= m - i; j++) {
            cout << " ";
        }

        for ( j = 1; j <= i; j++) {
            cout << huruf++;
        }

        for ( j = 1; j < i; j++) {
            cout << --huruf;
        }
        cout << endl;
    }


}