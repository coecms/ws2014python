#!/usr/bin/env python
import sys

ver = {
    'major' : sys.version_info.major,
    'minor' : sys.version_info.minor,
    'micro' : sys.version_info.micro
    }


padlength = 32

def print_no_linefeed(s):
    """ (str) -> None

    Prints the string s out without linefeed. 

    """
    # Can't use print, because python v2's "print s," causes errors when run in v3,
    # and v3's "print( s, end="" )" causes errors in v2.
    sys.stdout.write(s)

def element_sum(a, b):
    """ (list of num, list of num) -> list of num

    Prerequisite: len(a) == len(b)
    
    sums the lists a and b element-wise.
    
    >>> element_sum([0, 1, 2], [2, 3, 4])
    [2, 4, 6]
    """
    assert(len(a) == len(b))
    return [a[i] + b[i] for i in range(len(a))]
    

def check_version():
    print( "Python version {}.{}.{} found".format(ver['major'],ver['minor'],ver['micro'] ))
        
    if ver['major'] == 3 :
        print("We will be using 2.7.x, so be aware that some things might be different")
        return [0, 1]
    elif ver['major'] == 1 :
        print("Where did you find such an old python version? We are using 2.7.x, and you really should upgrade")
        return [1, 0]
    elif ver['minor'] != 7 :
        print("We will be using 2.7.x, so there might be a few minor differences")
        return [0, 1]
    print("We will be using 2.7.x, so you are fine here")
    return [0,0]
        
def check_numpy():
    print_no_linefeed("Checking for numpy...".ljust(padlength)) 
    try:
        import numpy
    except ImportError:
        print("fail")
        return [1, 0]
    print("success")
    return [0, 0]

def check_scipy():
    print_no_linefeed("Checking for scipy...".ljust(padlength))
    try:
        import scipy
    except ImportError:
        print("fail")
        return [1, 0]
    print("success")
    return [0, 0]
        
def check_netcdf4():
    print_no_linefeed("Checking for netcdf4-python...".ljust(padlength))
    try:
        from netCDF4 import Dataset
    except ImportError:
        print("fail")
        print("""
        You can use Scipy to read/write NetCDF files, but netcdf4-python is
        far superior both in reliability and ease-of-use
        """)
        return [0, 1]
    print("success")
    return [0, 0]
        
def check_matplotlib():
    print_no_linefeed("Checking for matplotlib...".ljust(padlength))
    try:
        import matplotlib
    except ImportError:
        print("fail")
        return [1, 0]
    print("success")
    return [0, 0]

def check_basemap():
    print_no_linefeed("Checking for basemap...".ljust(padlength))
    try:
        from mpl_toolkits.basemap import Basemap
    except ImportError:
        print("fail")
        return [1, 0]
    print("success")
    return [0, 0]

if __name__ == '__main__':
    
    result = [0, 0]  # First is the number of errors, second of warnings
    result = element_sum( result, check_version())
    result = element_sum( result, check_numpy())
    result = element_sum( result, check_scipy())
    result = element_sum( result, check_netcdf4())
    result = element_sum( result, check_matplotlib())
    result = element_sum( result, check_basemap())

    print("Check finished with {} errors and {} warnings".format(result[0], result[1]))
