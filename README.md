# Single-Domain-Magnetic-Nanoparticle-Simulation
Statistical Ensemble Modelling of Dynamic Hysteresis Loops  in Single-Domain and Non-interacting Magnetic Nanoparticles by using a Double-Well Rate Equation Approach
# Magnetic Nanoparticle Ensemble Simulation

This project implements a rate-equation model for the study of magnetic nanoparticle ensembles under an external magnetic field.

The code describes the magnetic behavior of single-domain nanoparticles by taking into account realistic distributions of particle size, magnetic anisotropy, and easy-axis orientation. Log-normal distributions are used to represent the statistical variability of nanoparticle properties, while average magnetic parameters such as particle volume, anisotropy constant, and anisotropy field are calculated from these distributions.

The magnetic energy landscape is evaluated through the competition between anisotropy energy and Zeeman energy, allowing the determination of stable and metastable magnetic states as well as the corresponding energy barriers. Magnetization reversal is modeled as a thermally activated process, with transition rates calculated using Arrhenius statistics.

Instead of solving the full Landau–Lifshitz–Gilbert (LLG) dynamics for every individual nanoparticle, the model employs a kinetic rate-equation approach. This significantly reduces computational cost while preserving the essential physics of thermally activated switching.

## Main Advantages

- **Ensemble-scale modeling:** Capable of representing experimentally realistic systems containing up to 10¹²–10¹⁵ nanoparticles through statistical averaging.
- **Computational efficiency:** Orders of magnitude faster than explicit LLG simulations of large nanoparticle assemblies.
- **Natural inclusion of distributions:** Particle size, anisotropy, and orientation distributions are incorporated directly into the calculations.
- **Thermal activation:** Magnetization reversal due to thermal fluctuations is explicitly described through Arrhenius transition rates.

## Applications

The model is suitable for studying:

- Magnetization reversal mechanisms
- Thermal stability of magnetic nanoparticles
- Superparamagnetic behavior
- Effects of particle-size and anisotropy distributions
- Large-scale nanoparticle ensemble dynamics
