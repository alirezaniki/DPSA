from pyrocko import moment_tensor as mtm

magnitude = 5.1
exp = mtm.magnitude_to_moment(magnitude)  # convert the mag to moment in [Nm]  
print(exp) 
