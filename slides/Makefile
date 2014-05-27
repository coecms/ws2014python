TARGET=slides.html
SOURCE=pytut.txt
SRCS=numpy.txt netcdf.txt n4py.txt

all: $(TARGET)

$(TARGET): $(SOURCE) $(SRCS)
	rst2s5 --link-stylesheet $< $@

clean:
	rm -rf $(TARGET) ui
