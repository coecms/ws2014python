TARGET=slides.html
SOURCE=index.txt
SRCS=numpy.txt netcdf.txt n4py.txt more_numpy.txt vector.txt mpl.txt basemap.txt
MATH=mathjax # mathml for python2, mathjax for python3

all: $(TARGET)

$(TARGET): $(SOURCE) $(SRCS)
	rst2s5 --link-stylesheet --math-output=$(MATH) $< $@

clean:
	rm -rf $(TARGET) ui
