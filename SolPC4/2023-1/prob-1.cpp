#include <iostream> 
#include <cstdlib> 
#include <ctime> 


using namespace std ; 

struct TFECHA{
    int dia , mes ; 
};

struct TCARGA{

 int nropasajeros; 
 TFECHA *fecha ; 
 
};









int main(){

 srand(time(NULL)) ; 


 int A[360] ; 

 // creamos arreglo 

 for(int i = 0 ; i<360; i++){
    A[i] = 500 + rand()%(700-500+1) ; 
 }
 



    return 0 ; 
}