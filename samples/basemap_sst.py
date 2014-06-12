import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid

sst_nc = nc.Dataset('SSTK_6hrs_sfc_2000_01.nc', 'r')

sst = sst_nc.variables['SSTK_GDS0_SFC'][0,:,:]
lon_ax = sst_nc.variables['g0_lon_2'][:]
lat_ax = sst_nc.variables['g0_lat_1'][:]

lon, lat = np.meshgrid(lon_ax, lat_ax)

omap = Basemap(projection='ortho',
               lat_0=-24.25, lon_0=133.5)

omap.drawmapboundary()
omap.drawcoastlines()
omap.fillcontinents(color='coral')

x, y = omap(lon, lat)

omap.contourf(x, y, sst, 60)
plt.show()

#-------------------------

merc_map = Basemap(projection='merc',
               llcrnrlat=-80., urcrnrlat=80.,
               llcrnrlon=-280., urcrnrlon=80.)

merc_map.drawmapboundary()
merc_map.drawcoastlines()
merc_map.fillcontinents(color='coral')

sst_s, lon_ax_s = shiftgrid(80., sst, lon_ax, start=False)
lon_s, lat_s = np.meshgrid(lon_ax_s, lat_ax)

x_s, y_s = merc_map(lon_s, lat_s)
merc_map.pcolormesh(x_s, y_s, sst_s)
plt.show()

#--------------------------

lon_r = np.ma.concatenate([lon, lon[:, np.newaxis, 0]], axis=-1)
lat_r = np.ma.concatenate([lat, lat[:, np.newaxis, 0]], axis=-1)
sst_r = np.ma.concatenate([sst, sst[:, np.newaxis, 0]], axis=-1)

#lon_r[:, -1] += 360.

polar_map = Basemap(projection='spstere',
                    boundinglat=-40., lon_0=90.)

polar_map.drawmapboundary()
polar_map.drawcoastlines()
polar_map.fillcontinents(color='coral')

#x, y = polar_map(lon, lat)
#polar_map.contourf(x, y, sst, 60)
x_r, y_r = polar_map(lon_r, lat_r)
polar_map.pcolormesh(x_r, y_r, sst_r)
plt.show()
