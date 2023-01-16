make [COMMAND] [EXTRA_ARGUMENTS]	

help            	print verbose help
report          	print environment arguments
all             	init venv
venv            	create python3 virtualenv .venv
venv-test       	test virutalenv .venv
init            	basic setup
initialize      	install libs and dependencies
submodules      	git submodule update --init --recursive
abandon-art     	unsecure demonstration seed (default 12)

make abandon-art words=24	
make abandon-art words=24 index=2147483647	
make privkey mnemonic="<string> ... <string>"	
