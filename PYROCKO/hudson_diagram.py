from __future__ import print_function
from matplotlib import pyplot as plt
from pyrocko.plot import hudson, beachball, mpl_init, mpl_color
from pyrocko import moment_tensor as mtm
import sys

magnitude = 4.6
strike = 334
dip = 34
rake = 33

m0 = mtm.magnitude_to_moment(magnitude)  # Convert MW to M0 [Nm]
mt = mtm.MomentTensor (strike=strike, dip=dip, rake=rake, scalar_moment=m0)  # Create Moment tensor
m6 = [mt.mnn, mt.mee, mt.mdd, mt.mne, mt.mnd, mt.med]  # Six identical components
Mt = (m6/mt.scalar_moment())   # Normalize the six identical components
MT = (Mt[0], Mt[1], Mt[2], Mt[3], Mt[4], Mt[5]) 

# setup plot layout

fontsize = 9.
markersize = fontsize
mpl_init(fontsize=fontsize)
width = 8.
figsize = (width, width / (4. / 3.))
fig = plt.figure(figsize=figsize)
axes = fig.add_subplot(1, 1, 1)
fig.subplots_adjust(left=0.03, right=0.97, bottom=0.03, top=0.97)

# draw focal sphere diagrams for the random MT

u, v = hudson.project(MT)
print(u, v)
try:
    beachball.plot_beachball_mpl(
        MT, axes,
        beachball_type='full',
        position=(u, v),
        size=30,
        color_t=mpl_color('skyblue3'),
        color_p=mpl_color('skyblue1'),
        alpha=1.0,  # < 1 for transparency
        zorder=1,
        linewidth=0.25)

except beachball.BeachballError as e:
	print(str(e), file=sys.stderr)

# draw the axes and annotations of the hudson plot
hudson.draw_axes(axes)

#fig.savefig('hudson_diagram.png', dpi=250)
plt.show()
