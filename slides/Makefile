SOURCES=$(wildcard *.txt)

TARGETS=$(SOURCES:.txt=.html)

all: $(TARGETS)

$(TARGETS): %.html: %.txt
	rst2s5 --link-stylesheet $< $@

clean:
	rm -rf $(TARGETS) ui
