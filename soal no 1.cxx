#include<iostream>
using namespace std;

int main () {
	float Volume, Luas, r;
	const float phi=3.14;
			 cout<<"=========================="<<endl;
	cout<<"Nama : Mutia Gusmawarni"<<endl;
	cout<<"No BP : 2310431030"<<endl;
cout<<"=========================="<<endl<<endl;
	cout<<"masukkan jari-jari bola = ";
	cin>>r;
	Luas = phi*r*r*4;
	cout<<"Luas bola tersebut adalah =  " <<Luas<<endl;
	Volume = phi*r*r*r*4/3;
	cout<<"Volume bola tersebut adalah = " <<Volume<<endl;

}