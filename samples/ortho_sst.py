import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

sst_nc = nc.Dataset('sst.nc', 'r')

sst = sst_nc.variables['SSTK_GDS0_SFC'][0,::-1,:]
lon = sst_nc.variables['g0_lon_2'][:]
lat = sst_nc.variables['g0_lat_1'][::-1]

omap = Basemap(projection='ortho',
              lat_0=-24.25, lon_0=133.5)

omap.drawmapboundary()
omap.drawcoastlines()
omap.fillcontinents(color='coral', lake_color='aqua')

lon_g, lat_g = np.meshgrid(lon, lat)
x, y = omap(lon_g, lat_g)

omap.contourf(x, y, sst, 60)

plt.show()
