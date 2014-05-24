TARGET=pytut.html
SOURCES=$(wildcard *.txt)

all: $(TARGET)

$(TARGET): $(SOURCES)
	rst2s5 --link-stylesheet $(TARGET:.html=.txt) $@

#$(TARGETS): %.html: %.txt
#	rst2s5 --link-stylesheet $< $@

clean:
	rm -rf $(TARGET) ui
