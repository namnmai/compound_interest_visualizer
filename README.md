# Portfolio Website

![Python](https://img.shields.io/badge/Python-3.12.4-3670A0.svg)

This program calculates the compound interest earned over time (with monthly contributions) and returns a labeled plot and table illustrating investment growth.


## Table of Contents
- [Technologies Used](#technologies-used)
- [Background](#background)


## Technologies Used<a name="technologies-used"></a>
- Python (3.12.4)
- Plotly (5.24.1)
- Django (5.1.1)
- NumPy (2.1.1)
- Bootstrap (4.3.1)


## Background <a name="background"></a>
The calculations follow the formula below:

$P =$ Initial investment (in dollars)

$r =$ Annual interest rate (%)

$t =$ Length of time (in years)

$C =$ Monthly contributions (in dollars)

$n =$ Compounding periods

The initial investment is compounded for all $t$ periods, so the first part is:

<p align="center"> $P(1+r)^t \hspace{0.5cm} (1)$

The monthly contributions $C$ (times 12) are compounded from $t − 1$ to $0$ years:

<p align="center"> $12C \cdot (1+r)^{t-1} + 12C \cdot (1+r)^{t-2} + \cdots + 12C \cdot (1+r)^0$

The sum of that series is:

<p align="center"> $12C \cdot \dfrac{(1+r)^t-1}{(1+r)-1}$

Then simplify:

<p align="center"> $\dfrac{12C}{r} \ [(1+r)^t-1] \hspace{0.5cm} (2)$

Put together $(1)$ and $(2)$:

<p align="center"> $\underbrace{\ P(1+r)^t \ }_{\text{(1)}} \ + \ \underbrace{\ \dfrac{12C}{r} \left[ (1+r)^t - 1 \right] \ }_{\text{(2)}}$

Final equation:

<p align="center"> $\text{Compound Interest} = P(1+r)^t + \dfrac{12C}{r} \left[ (1+r)^t - 1 \right]$
