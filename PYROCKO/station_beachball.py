import numpy as num
from matplotlib import pyplot as plt
from pyrocko import moment_tensor as pmt, cake, orthodrome
from pyrocko.plot import beachball
from pyrocko import moment_tensor as mtm

km = 1000.

# source position and mechanism
slat, slon, sdepth = 43, 32, 21*km

magnitude = 6.5
strike = 231
dip = 43
rake = 22

m0 = mtm.magnitude_to_moment(magnitude)  # Convert MW to M0 [Nm]
mt = mtm.MomentTensor (strike=strike, dip=dip, rake=rake, scalar_moment=m0)  # Create Moment tensor
m6 = [mt.mnn, mt.mee, mt.mdd, mt.mne, mt.mnd, mt.med]  # Six identical components
Mt = (m6/mt.scalar_moment())   # Normalize the six identical components

# receiver positions
rdepth = 0.0
rlatlons = [(35, 45),  (33, 48),  (32, 45), ]

# earth model and phase for takeoff angle computations
mod = cake.load_model('prem.f')
phases = cake.PhaseDef.classic('p')

# setup figure with aspect=1.0/1.0, ranges=[-1.1, 1.1]
fig = plt.figure(figsize=(4., 4.))  # size in inch
fig.subplots_adjust(left=0., right=1., bottom=0., top=1.)
axes = fig.add_subplot(1, 1, 1, aspect=1.0)
axes.set_axis_off()
axes.set_xlim(-1.1, 1.1)
axes.set_ylim(-1.1, 1.1)

projection = 'lambert'

beachball.plot_beachball_mpl(
    mt, axes,
    position=(0., 0.),
    size=2.0,
    color_t=(0.3, 0.3, 0.8),
    projection=projection,
    size_units='data')

for rlat, rlon in rlatlons:
    distance = orthodrome.distance_accurate50m(slat, slon, rlat, rlon)
    rays = mod.arrivals(
        phases=cake.PhaseDef('P'),
        zstart=sdepth, zstop=rdepth, distances=[distance*cake.m2d])

    if not rays:
        continue

    takeoff = rays[0].takeoff_angle()
    azi = orthodrome.azimuth(slat, slon, rlat, rlon)

    # to spherical coordinates, r, theta, phi in radians
    rtp = num.array([[1., num.deg2rad(takeoff), num.deg2rad(90.-azi)]])

    # to 3D coordinates (x, y, z)
    points = beachball.numpy_rtp2xyz(rtp)

    # project to 2D with same projection as used in beachball
    x, y = beachball.project(points, projection=projection).T

    axes.plot(x, y, '+', ms=10., mew=2.0, mec='black', mfc='none')

#fig.savefig('beachball-example04.png')
plt.show()
