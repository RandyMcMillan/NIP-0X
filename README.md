## NIP-0X - Deterministic Aliases
### MAKE
```sh
[COMMAND]       	[DESCRIPTION]	

help            	print verbose	
report          	print environment arguments	

all             	init venv	
venv            	create python3 virtualenv .venv	
venv-test       	test virutalenv .venv	
init            	basic setup	
initialize      	install libs and dependencies	


MacOS python3 bug fix:
MacOS: x86_64
make report init initialize install python-version=python3.10
MacOS: Arm64
make report init initialize install python-version=python3.9


submodules      	git submodule update --init --recursive	

privkey         	mnemonic="<bip39> ... <bip39>"	
abandon-art     	unsecure demonstration seed (default 12)	
awesome         	unsecure demonstration seed (default 12)	
bacon           	unsecure demonstration seed (default 12)	

[BIP39]
make privkey mnemonic="<string> ... <string>"
[TEST VECTORS]
make abandon-art words=24
make abandon-art words=24 index=0
make abandon-art words=24 index=1
make abandon-art words=24 index=2147483647
make awesome     words=24
make awesome     words=24 index=0
make awesome     words=24 index=1
make awesome     words=24 index=2147483647
make bacon       words=24
make bacon       words=24 index=0
make bacon       words=24 index=1
make bacon       words=24 index=2147483647
```

```sh
Original seed:
408b285c123836004f4b8842c89324c1f01382450c0d439af345ba7fc49acf705489c6fc77dbd4e3dc1dd8cc6bc9f043db8ada1e243c4a0eafb290d399480840
Original master key:
xprv9s21ZrQH143K4VHfAaPWRTm4aoHAZhJHunsZZTQptR82FSTZRjBGXBP8kQKHrUVUE8vMM2Z3h7UoG9x9XCt9FHQ1t1nHU7zQDqrEszAg28q
Derived private key:
5ea01c7e63fa417e5d846cb7444fc10d9d3e96a8af0838e9b7953561469ff500
Derived entropy (128)
b0af4affebd5e1241863cc955f3bb178511448003d9925663fc02c78be07d97fe250ff5d78ceb3750671a444f23d536d155371c304bae12d28e1b549abceb588
Derived mnemonic:
radar kid say stumble fun must ghost kangaroo next what unable valley
```
```sh
Original seed:
7f59b005d0005cb57c4ef7b481b1a0469ecba8b290166d314a47544e382e0cfcd4a9ae03748067ce2419d06bc7178df15268c1788720891e300ffe742b0cac83
Original master key:
xprv9s21ZrQH143K2gvkwLposF7uBm1X5kgxCweMkuhVrJsCjxh1BtFWCG6mfq2dSehEhwwEF47MmvP91rsximoHEjHqUFWSc7m3Nhfo6yAmTtq
Derived private key:
64c52cc00f1584b84002473cf302ae32ba38846351924ca6f4f7bb6d0f1739fb
Derived entropy (128)
c66fecf5949bae4083d2e0e652e3e9c39ac64c130c3bf1be6d12b42a9779a89ad69f0bd2e32ace2f9d04b3819f00c069c0daa509bb506e060bc172f0e0fd5875
Derived mnemonic:
shoe legal dice circle road cake aunt foster town novel whip mammal
```
```sh
Original seed:
241e86356db60a686bb8c30b1054eac70701493b6702ed5f4a0e54cd3d13f0ccfd6d8b37506dc5c65af5575e720196d6d81aca24f0f083a5c65597541ada0e32
Original master key:
xprv9s21ZrQH143K3sv6nA2qxNdUo8ZqLAMjzDrh3kRa6sT77ZcQhNGVEop97UiXt41Em61im2FwoFk92igAju78wXdhzrfXWKGJ9N9YZLp8LD1
Derived private key:
0ca8244bb209c214c848feff9fe1403d342eeb8e87a09f14152f6691e4405d45
Derived entropy (128)
a2a10e3b05dca074ff7b49d600be4dbb13d9e9a3c3eaa43a1eabd93e6c4de829e463985b58648a35b3239759e4bdf9972fac169a67a339b850f53e8d82edb4e0
Derived mnemonic:
pencil anchor mom arm skate denial worth hard stock album nature jaguar
```
