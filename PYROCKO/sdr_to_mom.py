from pyrocko import moment_tensor as mtm

magnitude = 6.3
strike = 123
dip = 54
rake = 32

m0 = mtm.magnitude_to_moment(magnitude)  # convert the mag to moment
mt = mtm.MomentTensor(strike=strike, dip=dip, rake=rake, scalar_moment=m0)
m6 = [mt.mnn, mt.mee, mt.mdd, mt.mne, mt.mnd, mt.med]  # The six MT components

print("     Mnn,        Mee,        Mdd,        Mne,         Mnd,        Med,   ")
print(m6/mt.scalar_moment())  # normalized MT components
