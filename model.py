"This is a dummy model.  It doesn't really do anything."

" Import required python modules "
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt


" Input Parameters "
C_1 = 1.0   # Concentration in Reservoir 1 (kmol/m3)
C_2 = 2.0   # Concentration in Reservoir 2 (kmol/m3)

dy = 1.0    # Thickness
ny = 5      # Number of cells for discretization

D = 1.0     # Diffusion coefficent (m2/s)

t_sim = 10  # Time span over which to integrate:

method = 'RK45' # Integration method.  Popular choices are 'RK45' and 'BDF'

" End user input section"


" Initialize Solution vector and input parameters"
SV_0 = np.zeros(ny)  # Each control volume nas one variable (the concentration)

Params = {'C_1':C_1, 'C_2':C_2, 'Ny':ny, 'dyInv':ny/dy, 'D_k':D}

"Define time derivative function.  Right now this does nothing:"
def Derivative(t, SV, p):

    "Initizlize the derivative vector:"
    dSVdt = np.zeros_like(SV)
    
    for i in np.arange(p['ny'):
        print(i)

    return dSVdt

"Integrate:"
sol = solve_ivp(lambda t, y: Derivative(t, y, Params), [0, t_sim], SV_0, method=method)

plt.plot(sol.t, sol.y.T)
plt.show()
