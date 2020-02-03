import numpy as np

#--------------------------------------
fs = 8000	# sample freq in Hz
fn = fs/2
t_sim = 2 	# Simulation time in sec
fmod    = 11	 # Modulation freq in Hz (Bod)
fsignal = 1475	 # Generator freq in Hz
#--------------------------------------

sim_point = int(t_sim/(1.0/fs)) 
t = np.linspace(0, t_sim, sim_point) 
