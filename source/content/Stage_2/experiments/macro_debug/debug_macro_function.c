#include <stdio.h>
#define ABS(x)           (((x) < 0) ? -(x) : (x))
#define myhello(x)  { \
    printf("enter %s \n",x); \
    printf("exit  %s \n",x); \
    }


#define callfoo(x)         foox()  

void fooB(){
  printf("enter fooB \n");
  printf("exit fooB \n");
}

int foo(int n)
{
   static counter=0;
   counter++;
   int sum = 0,i;
   for (i=0;i<n;i++)
   {
      sum+=i;
   }
   return sum;
}

main() {
   int i;
   long result = 0;
   printf("stop at here\n");
   myhello("aba");
   myhello("ddd");
   //callfoo("a");
   //callfoo("b");
   int a  = ABS(-10);
   for (i = 1;i<100; i++) {
     result +=i;
   }
   printf("result[1-100] = %d \n",result);
   printf("result[1-200] = %d \n",foo(250));
}
