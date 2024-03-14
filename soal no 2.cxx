#include<iostream>
#include<math.h>
using namespace std;

int main () {
	float X1, X2, X3, X4, X5, rata_rata, ragam, simpangan_baku, n ; 	cout<<"=========================="<<endl;
	cout<<"Nama : Mutia Gusmawarni"<<endl;
	cout<<"No BP : 2310431030"<<endl;
cout<<"=========================="<<endl<<endl;
	cout<<"masukkan X1 = ";
	cin>>X1;
	cout<<"masukkan X2 = ";
	cin>>X2;
	cout<<"masukkan X3 = ";
	cin>>X3;
	cout<<"masukkan X4 = ";
	cin>>X4;
	cout<<"masukkan X5 = ";
	cin>>X5;
	cout<<"masukkan banyak data = ";
	cin>>n;
	rata_rata = (X1+X2+X3+X4+X5)/n;
	cout<<"rata-rata dari data tersebut adalah = "<<rata_rata<<endl;
	ragam =((X1-rata_rata)*(X1-rata_rata) + (X2-rata_rata)*(X2-rata_rata) + (X3-rata_rata)*(X3-rata_rata) + (X4-rata_rata)*(X4-rata_rata) + (X5-rata_rata)*(X5-rata_rata))/n;
	cout<<"ragam dari data tersebut adalah = "<<ragam<<endl;
	simpangan_baku = sqrt(ragam);
	cout<<"simpangan baku dari data tersebut adalah = "<<simpangan_baku<<endl;
	
}