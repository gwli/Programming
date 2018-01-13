gcc -c section.c -o section.o
readelf -S section.o

gcc -T ldscript.lds section.o -o section
