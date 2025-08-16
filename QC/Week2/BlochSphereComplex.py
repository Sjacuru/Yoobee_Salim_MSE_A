import numpy as np
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt  # Required to display the plot

#plot_bloch_vector([1, np.pi/2, np.pi/2], coord_type='spherical') # positive y axis
plot_bloch_vector([1, np.pi/2, np.pi], coord_type='spherical') # negative x axis
#plot_bloch_vector([1, np.pi, np.pi/2], coord_type='spherical') # negative z axis = 1
#plot_bloch_vector([1, np.pi, np.pi], coord_type='spherical') # negative z axis = 1


plt.show()