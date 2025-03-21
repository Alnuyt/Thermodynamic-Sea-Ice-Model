"""

@author: Alexandre Nuyt

Partie 2 : Freezing surface temperature

This script simulates the evolution of sea ice thickness and surface temperature 
over time. It accounts for heat fluxes from solar and non-solar radiation, 
thermal conduction, and ocean heat flux. The surface temperature is computed 
by solving a heat balance equation, and the ice growth is determined 
based on energy conservation principles.

"""


import numpy as np
import matplotlib.pyplot as plt

# Physical constants 
L_fus = 3.35e5  # Latent heat of fusion for water (J/kg)
rho_i = 917  # Density of ice (kg/m^3)
k_i = 2.2  # Thermal conductivity of ice (W/m*K)
k_s = 0.31  # Thermal conductivity of snow (W/m*K)
spd = 86400  # Seconds in one day
Kelvin = 273.15 # Conversion celcius to kelvin
T_bo = -1.8 + Kelvin # Bottom temperature (Celsius)
T_su = -10 + Kelvin # Air temperature
epsilon = 0.99  # surface emissivity
sigma = 5.67e-8  # Stefan-Boltzman constant
alb = float(input("input the value of the albedo :"))  # surface albedo
N_years = int(input("input the duration of of the simulation in year :"))
N_days = 365*N_years
h = 0.5 # Ice thickness for the resolution of the equation for T_su

#Ocean Heat Flux
Qo_values = [int(input("input the value of the ocean heat flux :"))]

# Initial conditions
hi = np.zeros(N_days)  # Ice thickness array
hi[0] = 0.1  # Initial ice thickness
hs = float(input("input the height of snow in [m] :")) # Initial snow thickness (reamains constant)

def solar_flux(i):
    # Calculation of the day of the year 
    doy = i % 365
    Q_sol = 314 * np.exp((-(doy-164)**2)/4608)
    return Q_sol

def non_solar_flux(i):
    # Calculation of the day of the year 
    doy = i % 365
    Q_nsol = 118 * np.exp((-0.5*(doy-206)**2)/53**2) + 179
    return Q_nsol

def Surface_temperature(h, i):
    # Polynomial coefficients
    a = -epsilon * sigma
    b = 0
    c = 0
    d = -k_i / h
    e = solar_flux(i) *(1-alb) + non_solar_flux(i) + (k_i/h)*T_bo
    # Roots of the 4th° polynome using np.roots and we take only the real part
    T_su = min([273.15, np.roots([a, b, c, d, e]).real[3]])
        
    # Flux from the atmosphere
    F_f_a = solar_flux(i)*(1-alb) + non_solar_flux(i) - epsilon*sigma*T_su**4 -(k_i/h)*(T_su - T_bo)
    if F_f_a > 0:
        E_a_m = F_f_a*spd # We calculate the energy for merging with F_f_a
    else :
        E_a_m = 0
        
    return T_su, E_a_m

# We define the conductive flux thanks to the Fourier's law : \vec(q) = k*\grad(T)
def Cond_flux(hi, hs, T_su):
    if hs == 0 :
        Qc = k_i*((T_bo - T_su)/hi)
    else : 
        Qc = ((k_i*k_s)/(k_i*hs + k_s*hi))*(T_bo - T_su)
    return Qc

# We calculate the energy balance at the bottom
def Energy_balance(hi, hs, Qo, T_su): 
    # Multiplication d'un flux de chaleur par un lapse de temps : énergie
    E_minus = Cond_flux(hi, hs, T_su)*(spd)
    E_plus_ocean = Qo*spd
    if Qo == 0:
        Etot = E_minus
    else :
        Etot = E_minus - E_plus_ocean 
    return Etot

"""-------------------------------SIMULATIONS-------------------------------"""
    
for Qo in Qo_values :
    T_su_values = np.zeros(N_days)
    for i in range(1, N_days):
        T_su, E_a_m = Surface_temperature(hi[i-1], i)
        # we fill values of T_su
        T_su_values[0] = 273.15
        T_su_values[i] = T_su
        # Energy balance for one day
        Etot = Energy_balance(hi[i-1], hs, Qo, T_su)
        # Mass of new ice formed by Etot
        New_ice = Etot/L_fus
        # gain of ice thickness
        dhi_new = New_ice/rho_i
        # Mass of ice lost due to the E_a_m
        Lost_ice = E_a_m/L_fus
        # Lost of ice thickness
        dhi_lost = Lost_ice/rho_i
        # Evolution of ice thickness
        hi[i] = hi[i-1] + dhi_new - dhi_lost

    """ Surface Temperature Evolution """
    plt.plot(range(0, N_days), T_su_values)
    plt.xlabel('N_days')
    plt.ylabel('Surface Temperature')
    plt.title("Evolution of the surface temperature")
    plt.show()
    
    """ Ice Thickness Evolution """
    plt.plot(range(0, N_days), hi)
    plt.xlabel('N_days')
    plt.ylabel('Ice thickness')
    plt.title(f"Ice thickness evolution for {N_days} N_days")
    plt.show()   
    
"""----------------------------Surface Heat Fluxes--------------------------"""
year = np.arange(1, N_days +1)
Q_sol = solar_flux(year)
Q_nsol = non_solar_flux(year)
# Q_sol :
plt.plot(year, Q_sol, label="Q_sol")
plt.title("Evolution of the solar heat flux")
plt.xlabel("Days")
plt.ylabel("Solar Flux")
plt.show()
# Q_nsol :
plt.plot(year, Q_nsol, label="Q_sol")
plt.title("Evolution of the non solar heat flux")
plt.xlabel("Days")
plt.ylabel("Non Solar Flux")
plt.show()






