# Thermodynamic Sea Ice Model
Global warming has a major impact on the evolution of Arctic sea ice. This project, carried out as part of the LPHYS2265 course, aims to model these changes by simulating ice thickness using a one-dimensional thermodynamic model. Based on the laws of heat diffusion and energy balance, we have developed and improved several successive approaches:
1. **Thermal model of sea ice:** evolution with constant heat flux, addition of surface temperature, consideration of snow and ocean currents.
2. **Thermodynamic ice model:** adjustment of physical parameters, addition of experimental control and improvement of albedo representation.
3. **Multi-model analysis:** comparative study and 100-year climate projections with different radiative forcing scenarios.

## Part 1: Thermodynamic Model of Sea Ice
In this first part, we modelled the evolution of ice thickness as a function of conductive heat fluxes and temperature variations. The main steps are:

- Simulation of ice growth with a constant heat flux from the ocean.
- Integration of surface temperature evolution into the model.
- Addition of a snow layer and ocean mixture for greater realism.

The results show that the final ice thickness correlates well with theoretical predictions and depends strongly on ocean flow.

## Part 2: Improved Thermodynamic Model
In this second phase, we refined the model by adding:

- An experimental control comparing our simulation with reference models (hiMU71).
- A correction of ice thickness values to ensure better correspondence with observed data.
- Improved consideration of albedo for different surface conditions (dry snow, bare ice, etc.).

The seasonal evolution of ice thickness shows realistic dynamics with significant annual variation.

## Part 3: Multi-Model Analysis
In this final stage, a collaborative approach was used to compare several student models. We made 100-year projections taking into account different radiative forcing assumptions (increase in downward infrared radiation) with three scenarios:

- PR03 (+3 W/m²)
- PR06 (+6 W/m²)
- PR12 (+12 W/m²)

The main results are:

- A general trend towards a decrease in ice thickness over the years.
- More pronounced melting in summer when the surface temperature exceeds the melting threshold.
- Increased sensitivity of the model to variations in input parameters, particularly albedo and snow cover.

## Conclusion
The results confirm the strong influence of radiative forcing on sea ice evolution. Our simulations show that even with low forcing (PR03), ice thickness gradually decreases. Under a more severe scenario (PR12), ice loss reaches 50% in a century. This trend is consistent with current climate observations and highlights the urgency of limiting greenhouse gas emissions.

Improvements to the model could include the interaction between ice and ocean currents, as well as the integration of more detailed atmospheric dynamics. Future research could also focus on the impacts of this melting on the Arctic ecosystem and global climate.

## Use 
Run the code scripts for:
- Thermodynamic Model of Sea Ice: [Ice_growth_with_constant_temperature_ANTIM.py](Ice_growth_with_constant_temperature_ANTIM.py)
- Improved Thermodynamic Model: [Freeing_surface_temperature_ANTIM.py](Freeing_surface_temperature_ANTIM.py)
