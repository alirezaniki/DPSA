from pyrocko import moment_tensor as mtm

magnitude = 5.4

exp = mtm.magnitude_to_moment(magnitude)  # convert the mag to moment in [Nm]

# init pyrocko moment tensor
m = mtm.MomentTensor(
    mnn = 0.04*exp,
    mee = 0.6*exp,
    mdd = -0.63*exp,
    mne = 0.04*exp,
    mnd = 0.5*exp,
    med = 0.21*exp)

print(m)  # print moment tensor


