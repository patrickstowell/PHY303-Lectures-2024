(unit2:problems)=
# Unit 2 : Worked Problems

(unit2:problem:example1)=
### Example 2.1 : Form Factor Nuclear Size
Considering Elastic Scattering data for Nickel shown in the lecture notes, estimate the nuclear size.

```{admonition} Solution
:class: note, dropdown
In this example we use Figure 2.4 of the textbook by Martin to estimate the radius of the 58Ni nucleus.

The figure shows the differential cross section for the scattering of electrons of energy Ee = 450 MeV off a Nickel target as a function of the scattering angle. The plot shows a few dips that are not consistent with the scattering off a point-like particle, as the scattering off a point-like particle is described by the Mott formula, which is a monotonic function of the angle. Such behaviour is attributed to the presence of a form factor.

For this estimate we make the following assumptions:
• The scattering is elastic, e.g. the energy of outgoing electron is equal to the energy of the incoming electron. This is justified, as the energy of the electron (450 MeV) is much smaller than the rest mass of the nucleus (around 55 GeV). Because of this the momentum transfer $q$ is written as

$$
|q^{2}| = |\vec{p}_{i} - \vec{p}_{f}|^{2} = 2p^{2} - 2p^{2} (1-\cos\theta) 
$$

where we've assumed that the initial and final momenta magnitude, $p$, is constant due to elastic scattering. This can be rearranged to get

$$
|q^{2}| = 4p^{2} \sin (\theta/2)
$$

We can therefore write that

$$
qc = 2pc \sin(\theta/2)
$$

The shape of the nucleus is approximated as a solid sphere with uniform density. Using this approximation the form factor $F(q)$ is written as

$$
F(q) = 3(\sin b - b\cos b) b^{-3}
$$

with $b=qR/\hbar$. This standard formula is derived in the Martin textbook. Under this approximation the form factor and the cross-section will be zero for a few values of b. The fact that we do not observe a vanishing cross section means that the uniform density approximation is not exact. We can, however, take the position of the first minimum in the cross section as an indication of where the form factor would go to zero if the distribution was perfectly uniform. The first zero of the form factor correspond to the value $b_{1} = 4.49$.


**Step 1**
The momentum transfer in a collision can be related to the scattering angle using the formula above

$$
qc = 2pc \sin(θ/2).
$$

The first minimum can be read off the plot and correspond to $θ ≈ 24^{◦}$. Which means

$$
qc=2×450~\textnormal{MeV}× \sin(12^{◦}) =187~\textnormal{MeV}.
$$


**Step 2**
The first zero in the form factor function corresponds to the value of $b = 4.49$, using the definition of b we have

$$
R=b\frac{\hbar c}{qc} = 4.49 \times \frac{197~\textnormal{MeV fm}}{197~\textnormal{MeV}} = 4.8~\textnormal{fm}
$$

Note that if we ue the formula for the nuclear radius we would have

$$
R=1.21 A^{1/3}~\textnormal{fm} = 4.7~\textnormal{fm}
$$

which is remarkably close.
```

(unit2:problem:example2)=
### Example 2.2 : Nuclear Charge Distributions
Considering measurements of the charge distribution of nucleons for several nuclei shown in the lecture notes, determine an estimate of the mean nucleon density in nuclei.

```{admonition} Solution
:class: note, dropdown
The graph presented in the lectures shows the Saxton-Woods distribution of
the charge inside the nucleus. In this example we evaluate the density of nucleons inside the nuclear region for two nuclei: 12C and 208Pb.

We assume that the density of nucleons is proportional to the charge density and is given by

$$
\rho_{nucl} = \frac{A}{Ze} \rho_{ch}
$$

where we indicated with $ρ_{nucl}$ the density of nucleons and with $ρ_{ch}$ the charge density. We can read the plateau value of ρch off the graph for the two elements under consideration.

For 12-C we have $ρ_{ch} ≈ 0.08~e$ which gives

$$
\rho_{nucl} = \frac{12}{6e} \times 0.08~e = 0.16~ \textnormal{nucleon/fm}^{3}
$$


For 208-Pb we have $ρ_{ch} ≈ 0.06~e$ which gives

$$
\rho_{nucl} = \frac{208}{82e} \times 0.06~e = 0.15~ \textnormal{nucleon/fm}^{3}
$$


The average value is roughly constant throughout the $A$ spectrum and is

$$
\rho_{nucl} = 0.17~\textnormal{nucleon/fm}^{3}
$$
```

(unit2:problem:example3)=
### Example 2.3 : Nuclear Radius
Based on the idea of a hard nuclear cutoff derive an expression that relates the radius of the nucleus with the total nucleon number

```{admonition} Solution
:class: note, dropdown
The graph presented in the lecture of the root-mean-square (RMS) of the nuclear matter as a function of the atomic mass number $A^{1/3}$ shows a fit to the data gives a parameterization

$$
\sqrt{<r>}=0.94 A^{1/3} \textnormal{fm}
$$

Under the assumption that the nucleus is a sphere or radius $R$ and uniform density, the density would be

$$
ρ(r)=M \frac{3}{4\pi R^{3}}~~\textnormal{for}~~r<R \\ 
$$

and

$$
ρ(r)=0~~\textnormal{for}~~r>R
$$

The quantity $< r^{2} >$ is calculated as

$$
<r^{2}> = \frac{1}{M} \int r^{2} \rho_{M}(r) d^{3}r = \frac{1}{M} \int^{R}_{0} r^{2} \rho_{M}(r) 4\pi r^{2} dr
$$

where the integration over the angular coordinate was carried out to give a factor of $4\pi$. Substituting the expression for $ρ_{M}(r)$ we have

$$
<r^{2}> = \frac{3}{R^{3}} \int_{0}^{R} r^{4}dr = \frac{3}{5} R^{2}
$$

Therefore the nuclear radius is

$$
R = \frac{5}{3} \sqrt{ <r^{2}>} = 1.21~A^{1/3} fm
$$

```

(unit2:problem:example4)=
### Example 2.4 : Mirror Nuclei
Consider the nuclei 15-O and 15-N. Evaluate the difference in mass energy between the two nuclei using the SEMF and comment on why such a difference is observed.

```{admonition} Solution
:class: note, dropdown
We note that for each nuclei we have $A=15$, it is just the number of protons or neutrons that are swapped as Oxygen has 8 protons, and Nitrogen has 7. These are therefore **Mirror Nuclei**.

If we want to evaluate the difference in mass energy between the two nuclei we can simply subtract the mass calculated for each one using the SEMF. Before we do this however it's worth evaluating which terms in the liquid drop model for binding energy actually contribute. The volume term and surface tension term only depend on $A$ so both these terms cancel out if we take the difference as $A$ is constant. Both nuclei are also Even-Odd (as $A$ is odd) so that means the delta term also goes to zero. Therefore only the Asymmetry and Coulomb correction term contribute. 

We can take this one step further because a quick evaluation of the Asymmetry term gives us 
- 15-O : $a_{a} (15 - 2 \times 8)^{2} = a_{a} (-1)^{2} = a_{a}$
- 15-N : $a_{a} (15 - 2 \times 7)^{2} = a_{a} (1)^{2} = a_{a}$

The result is therefore that the asymmetry term will also cancel out, so any differences between the nuclei will mainly be down to the Coulomb term.


If we evaluate the difference in binding energy we get

$$
M(8,15) - M(7,15) = \left[ 8 m_{p} + 7m_{n} - B(8,15) \right] - \left[ 7 m_{p} + 8 m_{n} - B(7,15) \right]
$$

Rearranging this it becomes

$$
\Delta M = \left[ m_{p} - m_{n} \right] + \left[ B(7,15) - B(8,15) \right]
$$

We expect our binding energy terms to just be dominated by the difference in coulomb terms we therefore get

$$
\Delta B = \frac{a_{c}}{15^{1/3}} (8(8-1) - 7(7-1)) = 4.08 \textnormal{MeV}
$$

Substituting this in with the difference in mass between protons and neutrons we get

$$
\Delta M = \left[ -1.29 \textnormal{MeV} \right] + \left[  4.08 \textnormal{MeV} \right] = 2.79 \textnormal{MeV}
$$

So we find that actually there is an increase in overall mass energy (so a lower binding energy) for oxygen compared to nitrogen despite the fact that there are more protons (which are lighter than neutrons). This is because our Coulomb repulsion term contributes much more than the mass difference of a proton and neutron reducing the overall stability of the nucleus as we add protons.

Note that its also possible to do this assuming the $Z^{2}$ instead of $Z(Z-1)$ Coulomb term that is sometimes considered in the literature instead. If you do so you'll end up with a different energy (by around 7%) but the conclusions are still the same.
```

