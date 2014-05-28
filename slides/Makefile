TARGET=slides.html
SOURCE=index.txt
SRCS=numpy.txt netcdf.txt n4py.txt
MATH=mathml # Use mathjax with python 2

all: $(TARGET)

$(TARGET): $(SOURCE) $(SRCS)
	rst2s5 --link-stylesheet --math-output=$(MATH) $< $@

clean:
	rm -rf $(TARGET) ui
