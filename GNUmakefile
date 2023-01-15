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
PYTHON3                                 := $(shell which python3)
export PYTHON3

PIP                                     := $(shell which pip)
export PIP
PIP2                                    := $(shell which pip2)
export PIP2
PIP3                                    := $(shell which pip3)
export PIP3

python_version_full := $(wordlist 2,4,$(subst ., ,$(shell python3 --version 2>&1)))
python_version_major := $(word 1,${python_version_full})
python_version_minor := $(word 2,${python_version_full})
python_version_patch := $(word 3,${python_version_full})

my_cmd.python.3 := $(PYTHON3) some_script.py3
my_cmd := ${my_cmd.python.${python_version_major}}

PYTHON_VERSION                         := ${python_version_major}.${python_version_minor}.${python_version_patch}
PYTHON_VERSION_MAJOR                   := ${python_version_major}
PYTHON_VERSION_MINOR                   := ${python_version_minor}

export python_version_major
export python_version_minor
export python_version_patch
export PYTHON_VERSION

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
.PHONY: - all
-:
	#NOTE: 2 hashes are detected as 1st column output with color
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	#sed -n 's/^###//p' ${MAKEFILE_LIST} | column -t -s ':' |  sed -e 's/^//'

.PHONY: help
help:## 	print verbose help
	echo 'make [COMMAND] [EXTRA_ARGUMENTS]	'
	echo ''
	echo 'help            	print verbose help'
	echo 'report          	print environment arguments'
	echo 'all             	init venv'
	echo 'venv            	create python3 virtualenv .venv'
	echo 'venv-test       	test virutalenv .venv'
	echo 'init            	basic setup'
	echo 'initialize      	install libs and dependencies'
	echo 'submodules      	git submodule update --init --recursive'
	echo 'abandon-art     	unsecure demonstration seed (default 12)'
	### :make abandon-art words=24
	### :make privkey mnemonic="<string> ... <string>"
	echo ''
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
	@echo '        - BIP85_CLI=${BIP85_CLI}'
	@echo '        - WORDS=${WORDS}'
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

all: init venv## 	init venv
.PHONY: venv
venv:## 	create python3 virtualenv .venv
	test -d .venv || $(PYTHON3) -m virtualenv .venv
	( \
	   source .venv/bin/activate; $(PIP3) install -r requirements.txt; \
	);
	@echo "To activate (venv)"
	@echo "try:"
	@echo ". .venv/bin/activate"
	@echo "or:"
	@echo "make venv-test"
##:venv-test            source .venv/bin/activate; pip install -r requirements.txt;
venv-test:## 	test virutalenv .venv
	# insert test commands here
	test -d .venv || $(PYTHON3) -m virtualenv .venv
	( \
	   source .venv/bin/activate; $(PIP3) install -r requirements.txt; \
	);
.PHONY: init
.SILENT:
init:initialize## 	basic setup

	git config --global --add safe.directory $(PWD)
	chown -R $(shell id -u) *                 || echo

	# $(PYTHON3) -m pip install ./p2p 2>/dev/null
	#$(PYTHON3) -m pip install --upgrade pip 2>/dev/null
	#$(PYTHON3) -m pip install -q -r requirements.txt 2>/dev/null
	# pushd scripts > /dev/null; for string in *; do sudo chmod -R o+rwx /usr/local/bin/$$string; done; popd  2>/dev/null || echo

install:## 	install from local repo
	$(PIP3) install .
.PHONY:p2p
p2p:## 	install from local repo
	$(PYTHON3) ./p2p/setup.py install

.PHONY: initialize
initialize:## 	install libs and dependencies
	./scripts/initialize  #>&/dev/null

submodules:## 	git submodule update --init --recursive
	@git submodule update --init --recursive
abandon-art:## 	unsecure demonstration seed

ifneq ($(index),)
	@$(shell if [ "$(index)" -le "2147483647" ] && echo || echo "$(shell make help)")
	@echo $(INDEX)
	@bip85-cli --mnemonic "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art" -w $(WORDS) -i $(INDEX)
else
	@bip85-cli --mnemonic "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon art" -w $(WORDS)
endif
privkey:## 	generate privkey from mnemonic
	@bip85-cli --mnemonic "$(MNEMONIC)" -w $(WORDS) 2> make.log && echo -e "\n\n" && cat make.log || $(MAKE) help #&& echo -e "\n\n" && cat make.log
