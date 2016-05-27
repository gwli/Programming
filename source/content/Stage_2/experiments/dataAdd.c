#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

void *dlopen(const char *filename,int flag);


extern char etext, edata,end;

int main(int argc,char *argv[]){
    printf("First address pass:\n");
    printf("      program text(etex)        %10p\n",&etext);
    printf("      initialized data (edata)  %10p\n",&edata);
    printf("      uninitialized data(end)   %10p\n",&end);
    
    exit(EXIT_SUCCESS);
}
