import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt

sst_nc = nc.Dataset('SSTK_6hrs_sfc_2000_01.nc', 'r')
t = sst_nc.variables['initial_time0_hours'][:]
sst = sst_nc.variables['SSTK_GDS0_SFC'][:]

# This is wrong, needs to be area-weighted
sst_mean = np.mean(sst.reshape(sst.shape[0], -1), axis=-1)

plt.plot(t - t[0], sst_mean - 273.15, 'x')
plt.show()
