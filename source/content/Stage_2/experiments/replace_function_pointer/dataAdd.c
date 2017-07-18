#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

void *dlopen(const char *filename,int flag);


extern char etext, edata,end;

int add(int a, int b) {
    printf("in  add : %d,%d",a,b);
    return a + b;
}

int sub(int a,int b){
    printf("in  sub : %d,%d",a,b);
    return a - b;
}


int replace(){
    int * temp1 = 0;
    int * add_ptr = (int)&add;
    int * sub_ptr = (int)&sub;
    temp1 = add_ptr;
    *add_ptr = sub_ptr;
     
}
int counter(int i){
    static int sum =0;
    sum += i;
    return sum;
}
int main(int argc,char *argv[]){
    printf("First address pass:\n");
    printf("      program text(etex)        %10p\n",&etext);
    printf("      initialized data (edata)  %10p\n",&edata);
    printf("      uninitialized data(end)   %10p\n",&end);
    counter(1);
    add(1,2);
    replace();
    add(1,2);
     
    
    exit(EXIT_SUCCESS);
}
