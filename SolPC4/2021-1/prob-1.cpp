#include <iostream> 


using namespace std ; 

// creamos clase 

class Complejo{
 
 private: 

 // Atributos 
  
  int Re ; 
  int Im ; 

  public:

  // constructor 

  Complejo(int Re , int Im){
    this-> Re = Re ; 
    this-> Im = Im ;
  }

  // miembros

  int getReal(){
    return Re ; 
  }

  int getImag(){
    return Im; 
  }

  void setReal(int r){
    Re = r ; 
  }

  void setImaginario(int i){
    Im = i ; 
  } 

}; 


void sumaComplejos(Complejo p1 , Complejo p2){
    cout << "La suma de los numeros es : "<< p1.getReal() + p2.getReal() << " + "<< p1.getImag()+p2.getImag()<<"i "<< endl ; 
}




int main(){
 
 int Im1 , Re1 ; 
 int Im2 , Re2 ; 

 cout <<"Escriba la parte real e imaginaria de dos numeros complejos: "<< endl ; 

 cout << "*Nro1 "<< endl ; 
 cout << " -Re1: ";
 cin>> Re1;
 cout << " -Im1: ";
 cin>> Im1  ; 
 
 cout << endl ; 

 cout << "*Nro2 "<< endl ; 
 cout << " -Re2: ";
 cin>> Re2 ; 
 cout << " -Im2: ";
 cin>> Im2 ; 

 cout<< "---------------------------------------------"<< endl ; 

 // pasamos los valores a los objetos 

 // definimos objetos 

 Complejo p1(Re1 , Im1) ; 
 Complejo p2(Re2 , Im2) ; 
  
 cout << "El nro1 es: "<< p1.getReal()<< " + "<< p1.getImag()<< "i "<< endl ; 
 cout << "El nro2 es: "<< p2.getReal()<< " + "<< p2.getImag()<< "i "<< endl ; 

 cout<< "--------------------------------------------------------------------"<< endl ; 
 
 sumaComplejos(p1 , p2) ; 

    return 0 ; 
}