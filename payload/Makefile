CC = riscv64-unknown-elf-gcc
CFLAGS = -O2 -Wall

all: filesystem

sort: sort/sort.c
	$(CC) $(CFLAGS) -o bin/sort sort/sort.c

archive: archive/archive
	dd if=/dev/zero of=bin/blob bs=1M count=50
	cp archive/archive bin/archive

filesystem: sort archive
	@docker buildx build --platform linux/riscv64 \
		--output type=tar,dest=payload.tar \
		--file Dockerfile \
		. && \
	xgenext2fs -fzB 4096 -b 100000 -i 4096 -a payload.tar -L payload payload.ext2 && \
	rm -f payload.tar

clean:
	rm -f bin/* payload.ext2

.PHONY: all clean filesystem sort archive
