SHELL := /bin/bash

PWD 									?= pwd_unknown

THIS_FILE								:= $(lastword $(MAKEFILE_LIST))
export THIS_FILE
TIME									:= $(shell date +%s)
export TIME

ARCH                                    :=$(shell uname -m)
export ARCH
ifeq ($(ARCH),x86_64)
TRIPLET                                 :=x86_64-linux-gnu
export TRIPLET
endif
ifeq ($(ARCH),arm64)
TRIPLET                                 :=aarch64-linux-gnu
export TRIPLET
endif
ifeq ($(user),)
HOST_USER								:= root
HOST_UID								:= $(strip $(if $(uid),$(uid),0))
else
HOST_USER								:=  $(strip $(if $(USER),$(USER),nodummy))
HOST_UID								:=  $(strip $(if $(shell id -u),$(shell id -u),4000))
endif
export HOST_USER
export HOST_UID

PYTHON                                  := $(shell which python)
export PYTHON
PYTHON2                                 := $(shell which python2)
export PYTHON2

ifneq ($(python-version),)
PYTHON3                                 := $(python-version)
else
PYTHON3                                 := $(shell which python3.9)
endif
export PYTHON3

python_version_full  := $(wordlist 2,4,$(subst ., ,$(shell $(PYTHON3) --version 2>&1)))
python_version_major := $(word 1,${python_version_full})
python_version_minor := $(word 2,${python_version_full})
python_version_patch := $(word 3,${python_version_full})

my_cmd.python.3 := $(PYTHON3) some_script.py3
my_cmd := ${my_cmd.python.${python_version_major}}

PYTHON_VERSION                         := ${python_version_major}.${python_version_minor}.${python_version_patch}
PYTHON_VERSION_MAJOR                   := ${python_version_major}
PYTHON_VERSION_MINOR                   := ${python_version_minor}

export python_version_full
export python_version_major
export python_version_minor
export python_version_patch
export PYTHON_VERSION
export PYTHON_VERSION_MAJOR
export PYTHON_VERSION_MINOR

PIP                                     := $(shell which pip)
export PIP
PIP2                                    := $(shell which pip2)
export PIP2
PIP3                                    := $(shell which pip${python_version_major}.${python_version_minor})
export PIP3

NOSTR_RELAY                             := $(shell which nostr-relay)
export NOSTR_RELAY

### BIP85
BIP85_CLI:=$(shell command -v bip85-cli)
export BIP85_CLI
ifeq ($(words),)
WORDS:=12
else
WORDS:=$(words)
endif

ifneq ($(mnemonic),)
MNEMONIC:=$(mnemonic)
endif
export MNEMONIC

##REF: https://en.wikipedia.org/wiki/2,147,483,647
ifneq ($(index),)
INDEX:=$(index)
else
INDEX:=0
endif
INDEX_LIMIT:=2147483647
export INDEX

PROJECT_NAME							:= $(notdir $(PWD))
export PROJECT_NAME

#GIT CONFIG
GIT_USER_NAME							:= $(shell git config user.name)
export GIT_USER_NAME
GIT_USER_EMAIL							:= $(shell git config user.email)
export GIT_USER_EMAIL
GIT_SERVER								:= https://github.com
export GIT_SERVER

GIT_REPO_NAME							:= $(PROJECT_NAME)
export GIT_REPO_NAME

#Usage
#make package-all profile=rsafier
#make package-all profile=asherp
#note on GH_TOKEN.txt file below
ifeq ($(profile),)
GIT_PROFILE								:= $(GIT_USER_NAME)
ifeq ($(GIT_REPO_ORIGIN),git@github.com:PLEBNET_PLAYGROUND/plebnet-playground-docker.dev.git)
GIT_PROFILE								:= PLEBNET-PLAYGROUND
endif
ifeq ($(GIT_REPO_ORIGIN),https://github.com/PLEBNET_PLAYGROUND/plebnet-playground-docker.dev.git)
GIT_PROFILE								:= PLEBNET-PLAYGROUND
endif
else
GIT_PROFILE								:= $(profile)
endif
export GIT_PROFILE

GIT_BRANCH								:= $(shell git rev-parse --abbrev-ref HEAD)
export GIT_BRANCH
GIT_HASH								:= $(shell git rev-parse --short HEAD)
export GIT_HASH
GIT_PREVIOUS_HASH						:= $(shell git rev-parse --short HEAD^1)
export GIT_PREVIOUS_HASH
GIT_REPO_ORIGIN							:= $(shell git remote get-url origin)
export GIT_REPO_ORIGIN
GIT_REPO_PATH							:= $(HOME)/$(GIT_REPO_NAME)
export GIT_REPO_PATH

ifneq ($(bitcoin-datadir),)
BITCOIN_DATA_DIR						:= $(bitcoin-datadir)
else
BITCOIN_DATA_DIR						:= $(HOME)/.bitcoin
endif
export BITCOIN_DATA_DIR

ifeq ($(nocache),true)
NOCACHE					     			:= --no-cache
#Force parallel build when --no-cache to speed up build
PARALLEL                                := --parallel
else
NOCACHE						    		:=
PARALLEL                                :=
endif
ifeq ($(parallel),true)
PARALLEL                                := --parallel
endif
ifeq ($(para),true)
PARALLEL                                := --parallel
endif
export NOCACHE
export PARALLEL

ifeq ($(verbose),true)
VERBOSE									:= --verbose
else
VERBOSE									:=
endif
export VERBOSE

#TODO more umbrel config testing
ifeq ($(port),)
PUBLIC_PORT								:= 80
else
PUBLIC_PORT								:= $(port)
endif
export PUBLIC_PORT

ifeq ($(nodeport),)
NODE_PORT								:= 8333
else
NODE_PORT								:= $(nodeport)
endif
export NODE_PORT

ifneq ($(passwd),)
PASSWORD								:= $(passwd)
else
PASSWORD								:= changeme
endif
export PASSWORD

ifeq ($(cmd),)
CMD_ARGUMENTS							:=
else
CMD_ARGUMENTS							:= $(cmd)
endif
export CMD_ARGUMENTS

PACKAGE_PREFIX                          := ghcr.io
export PACKAGE_PREFIX

SED:=$(shell which sed)
export SED
DECOLORIZE:="$(SED) 's/\x1B\([0-9]{1,3}(;[0-9]{1,3})*)?[mGK]//g'"
export DECOLORIZE


.SILENT:
.PHONY: - all
-:
	#NOTE: 2 hashes are detected as 1st column output with color
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	#sed -n 's/^###//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^//'

.PHONY: help
help:## 	print verbose help
	echo '[COMMAND]       	[DESCRIPTION]	'
	echo ''
	echo 'help            	print verbose	'
	echo 'report          	print environment arguments	'
	echo ''
	echo 'all             	init venv	'
	echo 'venv            	create python3 virtualenv .venv	'
	echo 'venv-test       	test virutalenv .venv	'
	echo 'init            	basic setup	'
	echo 'initialize      	install libs and dependencies	'
	echo ''
	echo ''
	echo 'MacOS python3 bug fix:'
	echo 'MacOS: x86_64'
	echo 'make report init initialize install python-version=python3.10'
	echo 'make                        install python-version=python3.10'
	echo 'MacOS: Arm64'
	echo 'make report init initialize install python-version=python3.9'
	echo ''
	echo ''
	echo 'submodules      	git submodule update --init --recursive	'
	echo ''
	echo 'privkey         	mnemonic="<bip39> ... <bip39>"	'
	echo 'abandon-art     	unsecure demonstration seed (default 12)	'
	echo 'awesome         	unsecure demonstration seed (default 12)	'
	echo 'bacon           	unsecure demonstration seed (default 12)	'
	echo ''
	### :[BIP39]
	### :make privkey mnemonic="<string> ... <string>"
	### :		
	### :		
	### :[TEST VECTORS]
	### :make abandon-art words=24
	### :make abandon-art words=24 index=0
	### :make abandon-art words=24 index=1
	### :make abandon-art words=24 index=2147483647
	### :make awesome     words=24
	### :make awesome     words=24 index=0
	### :make awesome     words=24 index=1
	### :make awesome     words=24 index=2147483647
	### :make bacon       words=24
	### :make bacon       words=24 index=0
	### :make bacon       words=24 index=1
	### :make bacon       words=24 index=2147483647
	sed -n 's/^	### ://p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^###/	/'
	#sed -n 's/^	###//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^###/	/'

### test
.PHONY: report
report:## 	print environment arguments
### verbose report
	@echo ''
	@echo '	[ARGUMENTS]	'
	@echo '      args:'
	@echo '        - PROJECT_NAME=${PROJECT_NAME}'
	@echo '        - HOME=${HOME}'
	@echo '        - PWD=${PWD}'
	@echo ''
	#@echo '        - DECOLORIZE=${DECOLORIZE}'
	@echo '        - PYTHON=${PYTHON}'
	@echo '        - PYTHON2=${PYTHON2}'
	@echo '        - PYTHON3=${PYTHON3}'
	@echo '        - PYTHON_VERSION=${PYTHON_VERSION}'
	@echo '        - PYTHON_VERSION_MAJOR=${PYTHON_VERSION_MAJOR}'
	@echo '        - PYTHON_VERSION_MINOR=${PYTHON_VERSION_MINOR}'
	@echo '        - PIP=${PIP}'
	# @echo '        - PIP2=${PIP2}'
	@echo '        - PIP3=${PIP3}'
	@echo ''
	@echo '        - NOSTR_RELAY=${NOSTR_RELAY}'
	@echo ''
	@echo ''
	@echo '        - BIP85_CLI=${BIP85_CLI}'
	@echo '        - WORDS=${WORDS}'
	@echo '        - INDEX=${INDEX}'
	@echo '        - INDEX_LIMIT=${INDEX_LIMIT}'
	@echo ''
	@echo '        - TIME=${TIME}'
	@echo '        - ARCH=${ARCH}'
	@echo '        - HOST_USER=${HOST_USER}'
	@echo '        - HOST_UID=${HOST_UID}'
	@echo '        - GIT_USER_NAME=${GIT_USER_NAME}'
	@echo '        - GIT_USER_EMAIL=${GIT_USER_EMAIL}'
	@echo '        - GIT_SERVER=${GIT_SERVER}'
	@echo '        - GIT_PROFILE=${GIT_PROFILE}'
	@echo '        - GIT_BRANCH=${GIT_BRANCH}'
	@echo '        - GIT_HASH=${GIT_HASH}'
	@echo '        - GIT_PREVIOUS_HASH=${GIT_PREVIOUS_HASH}'
	@echo '        - GIT_REPO_ORIGIN=${GIT_REPO_ORIGIN}'
	@echo '        - GIT_REPO_NAME=${GIT_REPO_NAME}'
	@echo '        - GIT_REPO_PATH=${GIT_REPO_PATH}'

all: init initialize install venv## 	init initialize install venv
.PHONY: venv
venv:## 	create python3 virtualenv .venv
	test -d .venv || $(PYTHON3) -m virtualenv .venv
	( \
	   source .venv/bin/activate; \
	   $(PIP3) install .; \
	   $(PIP3) install -r requirements.txt; \
	   $(MAKE) venv-test \
	);
	@echo -e "\n"
	@echo "To activate (venv)"
	@echo "try:"
	@echo ". .venv/bin/activate"
	@echo "or:"
	@echo "make venv-test"
	@echo -e "\n"
##:venv-test            source .venv/bin/activate; pip install -r requirements.txt;
venv-test:## 	test virutalenv .venv
	# insert test commands here
	test -d .venv || $(PYTHON3) -m virtualenv .venv
	( \
	   source .venv/bin/activate; \
	   $(PIP3) install .; \
	   $(PIP3) install -r requirements.txt; \
	   $(PYTHON3) bip85_cli.py -h; \
	   $(PYTHON3) NIP-0X.py -h; \
	);

install:init initialize## 	install from local repo
	$(PYTHON3) get-pip.py
	$(PYTHON3) -m pip install -r requirements.txt
	$(PYTHON3) -m pip install ./secp256k1-py      2>/dev/null
	$(PYTHON3) -m pip install ./p2p               2>/dev/null
	$(PYTHON3) -m pip install ./bip85-utils       2>/dev/null
	$(PYTHON3) -m pip install ./nostr_relay       2>/dev/null
	$(PYTHON3) -m pip install ./aionostr          2>/dev/null
	$(PYTHON3) -m pip install -r ./aionostr/requirements_dev.txt
	$(PYTHON3) -m pip install -r ./aionostr/requirements.txt
	$(PYTHON3) -m pip install . 2>/dev/null
	$(MAKE) venv
init:
	git config --global --add safe.directory $(PWD)
	chown -R $(shell id -u) *                 || echo
initialize:
	. scripts/initialize  #>&/dev/null

.PHONY:p2p
p2p:## 	install from local repo
	$(PYTHON3) ./p2p/setup.py install

submodules:## 	git submodule update --init --recursive
	@git submodule update --init --recursive
abandon-art:## 	unsecure demonstration seed

ifneq ($(index),)
	@[ "$(index)" -le "$(INDEX_LIMIT)" ] && \
		bip85-cli --mnemonic "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art" \
		-w $(WORDS) -i $(INDEX) || echo 'make help';exit;
else
	@bip85-cli --mnemonic "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art" -w $(WORDS)
endif
# Twelve x "awesome" is 128 bits
#Twenty-four x "bacon" is 256 bits
awesome:## 	unsecure demonstration seed

ifneq ($(index),)
	@[ "$(index)" -le "$(INDEX_LIMIT)" ] && \
		bip85-cli --mnemonic "awesome awesome awesome awesome awesome awesome awesome awesome awesome awesome awesome awesome" -w $(WORDS) -i $(INDEX) || echo 'make help';exit;
else
	bip85-cli --mnemonic "awesome awesome awesome awesome awesome awesome awesome awesome awesome awesome awesome awesome" \
	-w $(WORDS)
endif

bacon:## 	unsecure demonstration seed

ifneq ($(index),)
	@[ "$(index)" -le "$(INDEX_LIMIT)" ] && \
		bip85-cli --mnemonic "bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon" -w $(WORDS) -i $(INDEX) || echo 'make help';exit;
else
	bip85-cli --mnemonic "bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon bacon" -w $(WORDS)
endif

privkey:## 	generate privkey from mnemonic
	@bip85-cli --mnemonic "$(MNEMONIC)" -w $(WORDS) 2> make.log && echo -e "\n\n" && cat make.log || $(MAKE) help #&& echo -e "\n\n" && cat make.log

.ONESHELL:
docs:## 	generate README.md
	@cat README          > README.md
	@echo "### MAKE"    >> README.md
	@echo "\`\`\`sh"    >> README.md
	$(MAKE) help        >> README.md
	@echo "\`\`\`"      >> README.md
	@echo ""            >> README.md
	@echo "\`\`\`sh"    >> README.md
	$(MAKE) abandon-art >> README.md
	@echo "\`\`\`"      >> README.md
	@echo "\`\`\`sh"    >> README.md
	$(MAKE) awesome     >> README.md
	@echo "\`\`\`"      >> README.md
	@echo "\`\`\`sh"    >> README.md
	$(MAKE) bacon       >> README.md
	@echo "\`\`\`"      >> README.md
	bash -c "$($(DECOLORIZE) $(PWD)/README.md)"
-include nostr-relay.mk
