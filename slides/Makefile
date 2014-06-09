TARGET=slides.html
SOURCE=index.txt
SRCS=numpy.txt netcdf.txt more_numpy.txt mpl.txt basemap.txt
MATH=mathjax

all: $(TARGET)

$(TARGET): $(SOURCE) $(SRCS)
	rst2s5 --link-stylesheet --math-output=$(MATH) $< $@

clean:
	rm -rf $(TARGET) ui
