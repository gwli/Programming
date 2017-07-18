src="debug_macro_function.c"

default:
	echo "generate -g"
	gcc -g ${src} -o tst.dbg

gdb3:
	echo "generate -ggdb3"
	gcc -ggdb3 ${src} -o tst.dbg3


all: default gdb3
clean:
	rm -fr tst.*
