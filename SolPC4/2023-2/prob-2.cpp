#include <iostream> 
#include <fstream>
#include <cmath> 


using namespace std ; 


struct coordenadas{
 
 float x , y ; 

}; 


void Ver_coor(ofstream&A1 , int v , coordenadas *p){

 A1.open("poligono1.txt" , ios::out); 

 // primera linea 
   A1 << v << endl ; 

  for(int i = 0 ;  i < v ; i++){
      cout << "Escribe coordenadas del vertice "<< i << " : "<< endl ; 
      cout << "X"<<i << " : "; 
      cin>>  (p+i)->x ; 
      cout << "y"<<i << " : "; 
      cin>>  (p+i)->y ;
   
      // agregamos al archivo poligono1.txt 

      A1 << (p+i)->x << " " << (p+i)->y << endl ; 
    } 
 
 A1.close(); 

}

// funcion para rotar angulos y ponerlos en un nuevo archivo 
void rotacion(ofstream &P2 , int v , coordenadas *p ,float ang){
 
 P2.open("Poligono2.txt" , ios:: out) ; 
  
  P2 << v << endl ; // primera linea del segundo archivo

    for(int i = 0 ; i < v ; i++){
    
     P2 << cos(ang)*((p+i)->x) - sin(ang)*((p+i)->y) << "  " << sin(ang)*((p+i)->x) - cos(ang)*((p+i)->y) << endl ; 
     
    }
 

 P2.close(); 


}





int main(){
 
 int v ; 

 cout << "Nro de vertices del poligono: "; 
 cin >> v ; 

 ofstream A1 ; 
 coordenadas *ptr = new coordenadas [v]; 

 // llamamos 

 Ver_coor(A1 , v , ptr) ; 

 cout << "------------------------------------"<< endl ; 

 float angulo; 
 float radianes; 
 cout << "Ingrese un angulo para rotar las coordenadas: "; 
 cin>> angulo ; 

 radianes = angulo*(3.1415/180); 

 cout << "-----------------------------------"<< endl ; 
 ofstream P2 ; 
 rotacion(P2 , v , ptr , radianes) ; 

 delete [] ptr ; 
    return 0 ; 
}