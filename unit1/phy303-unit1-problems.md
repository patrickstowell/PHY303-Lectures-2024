(unit1:problems)=
# Unit 1 : Worked Problems

(unit1:problem:example1)=
## Example 1.1 : Carbon Mass Calculation
Given the mass of a carbon-12 atom is $12u$, estimate the binding energy of the carbon nucleus.
```{admonition} Solution
:class: note, dropdown

First we start with the mass of the proton, neutron, and electrons in the atomic mass units. Since the mass if that of a carbon-12 atom, we include the electrons in our 
calculation.

$$
m_{p} = 1.00728 u \\
m_{n} = 1.00866 u \\
m_{e} = 0.00055 u \\
$$

Now we can write the binding energy as

$$
B = M_{C12} - 6m_{n} - 6m_{p} - 6m_{e} \\
Bc^{2} = 0.09894 u = 0.09894 \times 931.5~\textnormal{MeV/u} = 92.16~\textnormal{MeV}
$$

If we want to get this per nucleon we just need to divide by the total nucleons in a carbon 12 nucleus.

$$
B/A = 92.16~\textnormal{MeV} / 12 = 7.42~\textnormal{MeV/nucleon}\\
$$

A key thing to remember is that the electron mass does contribute if we are working in **atomic** mass values, whilst if we have been given 
a **nuclear** mass value it does not. For heavy mass nuclei including the electrons  has a smaller effect as the number of protons relative to neutrons drop. 

Given that the mass of an electron is around $0.511~\textnormal{MeV/c}^{2}$ we can expect shifts in the total binding energy on the order of several MeV depending on the nuclei. 

```

(unit1:problem:example2)=
## Example 1.2 : Nucleon Momentum Estimate
Use the Heisenberg Uncertainty principle to estimate the momentum of nucleons inside the nucleus given that the nuclear radius is on the order of $5~\textnormal{fm}$.

```{admonition} Solution
:class: note, dropdown
The Heisenberg principle states that 

$$
\Delta x \Delta p \geq \frac{\hbar}{2}
$$

in the case of a solid sphere we can measure the nucleons position with an uncertainty similar to the nuclear radius, hence

$$
c\Delta p \approx \frac{\hbar c}{2\Delta x}
$$

as usual multiplying both terms by $c$ to make use of the simple to remember quantity of $\hbar c \approx 200~\textnormal{MeV}~\textnormal{fm}$. This implies that the momenta of 
the nucleons will be of the order of 

$$
pc \approx \frac{200~\textnormal{MeV}~\textnormal{fm}}{2 \times 5~\textnormal{fm}} = 20~\textnormal{MeV}.
$$

This 20 MeV momentum is considerable, however it is much smaller than the nucleons mass, which means that albeit fast, they will not be in the relativistic regime. Therefore the 
momentum can be written as 

$$
p = m v
$$

and the ratio $pc/E$ can be expressed as

$$
\frac{pc}{E} = \frac{mvc}{mc^{2}} = \frac{v}{c} = \beta
$$

which gives $\beta \approx 0.02$. Despite the fact that we consider the nucleus as a solid sphere of protons and neutrons tightly packed together, the quantum mechanical reality is 
quite different as the nucleons move quite quickly around the allowed space.

```

(unit1:problem:example3)=
## Example 1.3 : Shielding Cross-section Estimate
Consider a 1-TBq source of Cs-137 that produces an effective dose of 1.073 Sv/hr at a distance of 30cm (*Delecroix Handbook 2002*). The decay chain of Cs-137 produces a clear 
gamma ray peak at 662 keV. Assuming a cross-section of 662keV gamma rays on lead nuclei of $\sigma=4.3 \times 10^{-23} cm^{2}$ determine the lead shielding thickness required to 
reduce the dose rate to 1mSv/hr.

```{admonition} Solution
:class: note, dropdown

To calculte the thickness of lead first we need to know the attenuation rate of our gamma rays in the lead shielding. We can estimate this based on the cross-section and the 
density of lead itself, $\rho$.

Given the density, $\rho=11.36 \textnormal{g/cm}^{3}$, and the mass of a lead atom to be $m_{Pb} = 207.293u$ we can estimate $n$ as 

$$
n = \frac{11.36 \textnormal{g/cm}^{3}}{207.293u \times 1.66056\times 10^{-24} \textnormal{g/u} } = 3.3 \times 10 ^{22} \textnormal{cm}^{-3}
$$

This leads to a mean free path of

$$
\lambda = \frac{1}{n\sigma} = 0.704 \textnormal{cm}^{-1}
$$

If we consider the intensity of our source passing through the lead shielding we get

$$
N = N_{0}~e^{-x/\lambda}
$$

Taking the natural log this gives

$$
x = -\lambda ~\textnormal{ln}\left( \frac{N}{N_{0}}\right)
$$

Now if we consider our known attenuation and drop required we get

$$
x = -0.704 ~\textnormal{ln} \left( \frac{1~\textnormal{mSv/hr}}{1.073~\textnormal{Sv/hr}}\right) = 4.91~\textnormal{cm}
$$

Note that this is an estimate based on just the 662keV peak, and neglects the $r^{2}$ fall-off for point radioactive sources, but it highlights how the cross-section has an effect 
on the result. If the cross-section's for gamma radiation were lower, we would expect much thicker shielding requirements.

```

(unit1:problem:example4)=
## Example 1.4 : Closest Approach Estimate
Considering Polonium-210 as an alpha emitter in Rutherford's gold foil experiment, estimate the minimum theoretical limit to which alpha scattering may be able place a limit on 
the size of the nucleus.

```{admonition} Solution
:class: note, dropdown


To consider the limit of the alpha scattering experiments we need to determine their distance of closest possible approach under the hyperbolic trajectory assumption.

Consider the case when an alpha particle is directed head-on towards the nucleus, so that when it reaches the distance of closest approach it turns around and travels back in the 
direction it came. At this turning point all of the alpha's kinetic energy has been transformed into electric potential energy.

The potential some distance, $r$, away is given by

$$
E_{Q} = \frac{1}{4\pi\epsilon_{0}} \frac{(2e)\cdot(Ze)}{r}
$$

where 2e is the charge of the alpha, and Ze is the charge of the gold nucleus.

At the distance of closest approach, $d$, this potential is equal to the starting kinetic energy of the alpha,

$$
K_{\alpha} =  \frac{1}{4\pi\epsilon_{0}} \frac{(2e)\cdot(Ze)}{d}.
$$

This means the distance is simply

$$
d =  \frac{1}{4\pi\epsilon_{0}} \frac{(2e)\cdot(Ze)}{K_{\alpha}}.
$$


Now to determine the energy of the alphe we need to consider the mass deficit of the decay that took place to produce it. 

$$
\textnormal{Po}_{210} \rightarrow \textnormal{Pb}_{206} + \alpha.
$$

The mass contributions from each of these are taken from the NIST material database as

$$
M(\textnormal{Pb}_{210}) = 209.9828u \\
M(\textnormal{Pb}_{206}) = 205.9794u \\
M(\alpha) = 4.0026u \\
$$

Note that here for the alpha mass contribution we have used the mass of a **Helium atom** as this encapsulates that the 2 extra electrons have to go somewhere.


This means the mass deficit energy, $Q$, is given by

$$
Qc^{2} = (209.9828u - 205.9794u - 4.0026u)c^{2} = 0.0058u ~c^{2}
$$

This energy will be split between the alpha and daughter nuclei, however if we assume that all the energy goes into the kinetic energy of the alpha given it has much smaller mass 
this gives the maximum kinetic energy of the alpha in standard units as

$$
K_\alpha = 5.40~\textnormal{MeV} = 8.65175 \times 10^{-13} J
$$

Subbing this maximum back into our equation for the distance gives

$$
d = 4.905 \times 10^{-14}~\textnormal{m}
$$

So our alpha particles only manage to get within $49 \textnormal{fm}$ from the nucleus and that is if they hit the gold nucleus head on. If we consider that typical $\alpha$ 
particle energies are between $0-11 \textnormal{MeV}$ this gives a minimum distance of closest approach of around $25~\textnormal{fm}$ still much bigger than the size of the gold 
nucleus ($6.6~\textnormal{fm}$). 

```
