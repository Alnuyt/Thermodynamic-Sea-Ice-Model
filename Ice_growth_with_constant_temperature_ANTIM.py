"""

@author: Alexandre Nuyt

Partie 1 : Ice growth with constant temperature and ocean heat flux

This script models the evolution of sea ice thickness over time under 
constant atmospheric temperature conditions, taking into account 
the effect of different ocean heat fluxes. The ice growth is determined 
using the energy balance at the ice-ocean interface, and results are 
compared with the analytical solution given by Stefan's law.

"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants 
L_fus = 3.35e5  # Latent heat of fusion for water (J/kg)
rho_i = 917  # Density of ice (kg/m^3)
k_i = 2.2  # Thermal conductivity of ice (W/m*K)
k_s = 0.31  # Thermal conductivity of snow (W/m*K)
spd = 86400  # Seconds in one day
Kelvin = 273.15 
T_bo = -1.8 + Kelvin # Bottom temperature (Celsius)
T_su = -10 + Kelvin # Air temperature
days = 30

#Ocean Heat Flux
Qo_values = [0, 5, 180.4]

# Initial conditions
hi = np.zeros(days)  # Ice thickness array
hi[0] = 0.1  # Initial ice thickness
hs = 0 # Initial snow thickness (reamains constant)

# We define the conductive flux thanks to the Fourier's law : \vec(q) = k*\grad(T)
def Cond_flux(hi, hs):
    if hs == 0 :
        Qc = k_i*((T_bo - T_su)/hi)
    else : 
        Qc = ((k_i*k_s)/(k_i*hs + k_s*hi))*(T_bo - T_su)
    return Qc

# We calculate the energy balance at the bottom
def Energy_balance(hi, hs, Qo): 
    # Multiplication d'un flux de chaleur par un lapse de temps : énergie
    E_minus = Cond_flux(hi, hs)*(spd)
    E_plus_ocean = Qo*spd
    if Qo == 0:
        Etot = E_minus
    else :
        Etot = E_minus - E_plus_ocean 
    return Etot

# Evolution of the ice thickness
for Qo in Qo_values :
    for i in range(1, days):
        # Energy balance for one day
        Etot = Energy_balance(hi[i-1], hs, Qo)
        # new ice formed by Qtot
        New_ice = Etot/L_fus
        # gain of ice thickness
        dh = New_ice/rho_i
        # Evolution of ice thickness
        hi[i] = hi[i-1] + dh
    # Print the final thickness
    print("----------------------------------------------------------------------")
    print(f"The final thickness for a Ocean heat flux of {Qo} W/m^2 is {hi[-1]} m")
    print("----------------------------------------------------------------------")
    # We plot the evolution of hi
    plt.plot(range(0, days), hi)
    plt.xlabel('Days')
    plt.ylabel('Ice thickness')
    plt.title(f"Ice thickness evolution for {days} days")
    plt.show()

# Evolution of the ice thickness according to the Stefan'law (Analytical solution)
hi_a = np.zeros(days)
for i in range(1, days):
    hi_s = np.sqrt(0.1**2 + (2*k_i*(T_bo - T_su)*days*spd)/(rho_i*L_fus))
    hi_a[i] = hi_s

print("-------------------------------------------------------------------------")
print(f"The final thickness for a Ocean heat flux of 0 W/m^2 is {hi_a[-1]} m")
print("-------------------------------------------------------------------------")
# We plot the evolution of hi
plt.plot(range(0, days), hi_a)
plt.xlabel('Days')
plt.ylabel('Ice thickness')
plt.title(f"Ice thickness evolution according to the Stefan's law for {days} days")
plt.show()



    
    
        
