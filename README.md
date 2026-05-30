Notebook 1:
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
Notebook 2:
Monodisperse / Mean-Particle Model
Single-Domain Magnetic Nanoparticle Simulation (Monodisperse Model)

This Mathematica notebook implements a rate-equation model for the simulation of dynamic magnetic hysteresis loops in single-domain, non-interacting magnetic nanoparticles.

Unlike the ensemble model, all nanoparticles are assumed to possess identical magnetic properties. A single particle volume, anisotropy constant, saturation magnetization, and easy-axis orientation are used throughout the calculations. This approach allows the investigation of the intrinsic magnetic response of an idealized nanoparticle system without the influence of statistical distributions.

The magnetic energy landscape is determined from the competition between anisotropy and Zeeman energies. Stable and metastable magnetic states are identified, and thermally activated transitions between these states are described using Arrhenius transition rates. The resulting rate equations are solved to obtain the time-dependent magnetization and dynamic hysteresis loops under alternating magnetic fields.

Main Advantages
Simple and computationally efficient implementation
Direct investigation of intrinsic nanoparticle behavior
Clear interpretation of thermal activation effects
Useful benchmark for comparison with distributed ensemble models
Fast calculation of dynamic hysteresis loops
Applications

The model is suitable for studying:

Magnetization reversal mechanisms
Dynamic hysteresis loop formation
Thermal activation effects
Frequency-dependent magnetic response
Benchmarking against ensemble-based simulations
Python Script:
Hysteresis Loop Analysis and SLP Calculation
Magnetic Nanoparticle Simulation and Analysis Toolkit

This repository contains Mathematica notebooks and Python scripts for the simulation and analysis of magnetic nanoparticle ensembles under alternating magnetic fields.

Contents
1. Magnetic Nanoparticle Ensemble Simulation

This Mathematica notebook simulates the magnetic response of an ensemble of nanoparticles considering:

Saturation magnetization distribution
Anisotropy constant distribution
Particle size distribution
Energy landscape calculations
Thermal activation effects
Magnetization dynamics under alternating magnetic fields

The code calculates energy minima and maxima, transition rates between magnetic states, and the time-dependent magnetization of the nanoparticle ensemble.

2. Hysteresis Loop Processing and Unit Conversion

This Python script:

Reads hysteresis loop data from text files
Converts magnetic field and magnetization units
Calculates:
Saturation magnetization (Ms)
Remanent magnetization (Mr)
Coercive field (Hc)
Initial susceptibility (slope)
Hysteresis loop area
Specific Loss Power (SLP)
Optionally saves the converted dataset to a new file
3. Magnetic Hyperthermia Analysis

This code evaluates the heating performance of magnetic nanoparticles under AC magnetic fields by analyzing hysteresis losses and power dissipation.

Calculated quantities may include:

Energy losses per cycle
Specific Loss Power (SLP)
Dependence on field amplitude and frequency
Effects of particle size and anisotropy distributions
Requirements
Mathematica
Wolfram Mathematica 12 or later
Python
Python 3.8+
tkinter (included in most standard Python installations)
Input Data

Input files should contain two hysteresis branches separated by a blank line.
Output Parameters

The analysis provides:

Hc1, Hc2, Hc
Mr1, Mr2, Mr
Ms1, Ms2, Ms
Initial slope
Hysteresis loop area
Specific Loss Power (SLP)
Applications

The codes are intended for research in:

Magnetic nanoparticles
Magnetic hyperthermia
Nanomagnetism
Magnetic characterization
Biomedical applications of magnetic materials


Author
Developed for the simulation and analysis of magnetic nanoparticle systems and magnetic hyperthermia experiments.
