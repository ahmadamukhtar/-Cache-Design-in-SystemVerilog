BLOCKS ?= 256
WORDS_PER_BLOCK ?= 4
WAYS ?= 1

clean: 
	rm -rf ./init_files/

cache:
	python3 ./scripts/cache_init.py -b ${BLOCKS} -w ${WORDS_PER_BLOCK} -a ${WAYS}