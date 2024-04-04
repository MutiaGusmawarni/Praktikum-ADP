#include <iostream>
#include <stdio.h>
using namespace std;
int jumlah_dor, a, i, j;
int main () {
	a = 1;
	jumlah_dor = 0;
	cout<<"=====TUGAS MODUL 4=====\n";
	cout<<"Nama : Mutia Gusmawarni\n";
	cout<<"NIM  : 2310431030\n";
	cout<<"=======================\n\n";
	for ( i = 1; i <= 10; i++) 
	{
		for ( j = 1; j<= 10; j++) 
		{
	    	if ( a%3 == 0) {
	    		cout<<"DOR "; jumlah_dor++;
     	   }   else if (a%5 == 0) {
     	   	cout<<"DOR ";jumlah_dor++;
     	   }   else {
     	   	cout<<a<<" ";
     	   }
   	 	a++;
		}
		cout<<endl;
     }
     cout<<"\nTotal jumlah DOR yang muncul: "<<jumlah_dor;
}