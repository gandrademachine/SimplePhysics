from cinematic import position
import numpy as np
# Sinoid position model:

sinef = "t**3+t**2+t"
t = np.arange(-2*np.pi,2*np.pi,1e-2)

sine = position(t, sinef)
print(sine.Acceleration(np.round(np.pi,2)))
sine.Plot(np.round(np.pi,2))
