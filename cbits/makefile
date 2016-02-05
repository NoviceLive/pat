FLAGS = -Wall

CC = gcc ${FLAGS}
WINCC32 = i686-w64-mingw32-gcc ${FLAGS}
WINCC64 = x86_64-w64-mingw32-gcc ${FLAGS}

BINDIR = bin


all:
	make pattern
	make windows
	make hex


install: pattern
	sudo cp ./${BINDIR}/pattern /usr/bin/pattern


installall: pattern hex
	make install
	sudo cp ./pat3.sh /usr/bin/pat3
	sudo cp ./pat4.sh /usr/bin/pat4
	sudo cp ./pat8.sh /usr/bin/pat8
	sudo cp ./${BINDIR}/hex /usr/bin/hex
	sudo cp ./${BINDIR}/unhex /usr/bin/unhex


pattern: mixedradix.o libhex.o pattern.c
	${CC} -o ${BINDIR}/pattern \
		${BINDIR}/mixedradix.o ${BINDIR}/libhex.o pattern.c


windows:
	 ${WINCC32} pattern.c mixedradix.c libhex.c \
		-o ${BINDIR}/pattern32.exe
	 ${WINCC64} pattern.c mixedradix.c libhex.c \
		-o ${BINDIR}/pattern64.exe


hex: hex.c unhex.c libhex.o
	${CC} -o ${BINDIR}/hex hex.c ${BINDIR}/libhex.o
	${CC} -o ${BINDIR}/unhex unhex.c ${BINDIR}/libhex.o


mixedradix.o: mixedradix.c mixedradix.h
	mkdir -p ${BINDIR}
	${CC} -c mixedradix.c -o ${BINDIR}/mixedradix.o


libhex.o: libhex.c libhex.h
	mkdir -p ${BINDIR}
	${CC} -c libhex.c -o ${BINDIR}/libhex.o


clean:
	rm -rf ${BINDIR}
