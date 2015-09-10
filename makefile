FLAGS = -Wall

CC = gcc ${FLAGS}
WINCC32 = i686-w64-mingw32-gcc ${FLAGS}
WINCC64 = x86_64-w64-mingw32-gcc ${FLAGS}


all:
	make pattern
	make windows
	make hex
	make test


install: pattern
	sudo cp ./pattern /usr/bin/pattern


installall: pattern hex
	sudo cp ./pattern /usr/bin/pattern
	sudo cp ./pat3.sh /usr/bin/pat3
	sudo cp ./pat4.sh /usr/bin/pat4
	sudo cp ./pat8.sh /usr/bin/pat8
	sudo cp ./hex /usr/bin/hex
	sudo cp ./unhex /usr/bin/unhex


pattern: mixedradix.o libhex.o pattern.c
	${CC} -o pattern mixedradix.o libhex.o pattern.c


windows:
	 ${WINCC32} pattern.c mixedradix.c libhex.c -o pattern32.exe
	 ${WINCC64} pattern.c mixedradix.c libhex.c -o pattern64.exe


hex: hex.c unhex.c libhex.o
	${CC} -o hex hex.c libhex.o
	${CC} -o unhex unhex.c libhex.o


test: mixedradix.o mixedradix-test.c rotate_string-test.c
	${CC} -o test-mixedradix mixedradix-test.c mixedradix.o
	${CC} -o test-rotate_string rotate_string-test.c mixedradix.o


mixedradix.o: mixedradix.c mixedradix.h
	${CC} -c mixedradix.c


libhex.o: libhex.c libhex.h
	${CC} -c libhex.c


clean:
	rm -f pattern hex unhex test-mixedradix test-rotate_string *.o *.exe
