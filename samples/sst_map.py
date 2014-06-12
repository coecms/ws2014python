#!/usr/bin/python
# Load the NetCDF file and plot its data

import netCDF4
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os

dirname = os.curdir
filename = "SSTK_6hrs_sfc_2000_01.nc"

def main():
    f = netCDF4.Dataset(filename, 'r')
    lat_array = f.variables['g0_lat_1'][::1]
    print(lat_array[:])
    lon_array = f.variables['g0_lon_2'][::1]
    print(lon_array[:])
    #lat, lon = np.meshgrid(lat_array, lon_array)
    lon, lat = np.meshgrid(lon_array, lat_array)
    #sst = np.swapaxes(f.variables['SSTK_GDS0_SFC'][1,...].squeeze() - 273.15,
    #                  0, 1)
    sst = f.variables['SSTK_GDS0_SFC'][0] - 273.15
    fig = plt.figure()
    ax = fig.add_axes([0.05, 0.05, 0.9, 0.9])
    m = Basemap(projection='cyl',
                llcrnrlat=-90,urcrnrlat=90,
                llcrnrlon=0,urcrnrlon=360,resolution='c')

    m.drawcoastlines()
    m.fillcontinents(color='0.8', lake_color='aqua')

    im1 = m.pcolormesh(lon, lat, sst, shading='flat',
                       cmap=plt.cm.jet)
    m.drawparallels(np.arange(-90., 99., 30.))
    m.drawmeridians(np.arange(0.,360.,60.))
    cb = m.colorbar(im1,"bottom", size="5%", pad="2%")

    ax.set_title('Sea Surface Temperature')

    plt.show()

    f.close()

if __name__ == '__main__':
    main()
