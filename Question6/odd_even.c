/*

  Jen Anderson
  anderjen@onid.oregonstate.edu
  CS311-400
  Homework1
  Question6 & 7	
 
  from:
  http://www.programmingsimplified.com/c/source-code/c-program-check-odd-even

*/


#include<stdio.h>
 
int main()
{
   int n;
 
   printf("Enter an integer\n");
   scanf("%d", &n);
 
   if ( n & (1 == 1) )
   {
      printf("Odd\n");
   }	
   else
   {
      printf("Even\n");
   }
   return 0;

}
