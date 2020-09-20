/*


*/

#include <stdio.h>
#include <stdlib.h>
#include "righe.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(void)
{ 
 unsigned int conta;	
 FILE*Fin;	
 char var[150]; // Varibile per inserire la locazione dove si trova il file
 // Richiesta di inserire il file da leggere:
 printf("Inserire la locazione del file di testo");
 scanf("%s",&var);	
 // Verifica del file se è trovato:
 Fin = fopen(var,"rt")
 if(Fin)
 {
  conta=conta_righe(Fin);
  printf("Righe contate: %i",&conta);	
 } 
 else
 {
  printf("File non trovato");	
 }
 fclose(Fin);
 //
 return 0;
}
