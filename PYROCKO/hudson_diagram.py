from __future__ import print_function
from matplotlib import pyplot as plt
from pyrocko.plot import hudson, beachball, mpl_init, mpl_color
from pyrocko import moment_tensor as mtm
import sys

m = mtm.MomentTensor(
    mnn = 2.31,
    mee = -2.63,
    mdd = 0.395,
    mne = 1.69,
    mnd = 0.232,
    med = -0.935)

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

u, v = hudson.project(m)
print(u, v)
try:
    beachball.plot_beachball_mpl(
        m, axes,
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

