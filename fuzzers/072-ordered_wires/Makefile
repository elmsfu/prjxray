
N := 1
SPECIMENS := $(addprefix build/specimen_,$(shell seq -f '%03.0f' $(N)))
SPECIMENS_OK := $(addsuffix /OK,$(SPECIMENS))
MAX_VIVADO_PROCESS ?= 4
MAX_PIPS_INSTANCE ?= 340000

database: $(SPECIMENS_OK)
	true

pushdb:
	true

$(SPECIMENS_OK):
	bash generate.sh $(subst /OK,,$@) -p=$(MAX_VIVADO_PROCESS) -t=$(MAX_PIPS_INSTANCE)
	touch $@

run:
	$(MAKE) clean
	$(MAKE) database
	$(MAKE) pushdb
	touch run.ok

clean:
	rm -rf build run.ok

.PHONY: database pushdb run clean

