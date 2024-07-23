# Lecture 3 : Liquid Drop Model

So what might the charge and mass distribution be like in Nuclei and how is the Hosftadter experiment interpreted to tell us about it?

We know from Rutherford that nucleons in nuclei are likely incompressible. So based on this the smallest model would be a so called Top-Hat Distribution. That is, constant uniform density, falling to zero at the "edge" of the nucleus.


However, experimental data suggest that nuclei have a more "fuzzy" form at the edges. To get the fit correct we need to introduce a so called Form-Factor, $F$,


$$
\left(\frac{d\sigma}{d\Omega}\right)_{\textnormal{distributed}}  = |F({\bf q}^{2})|^{2}\times \left(\frac{d\sigma}{d\Omega}\right)_{\textnormal{point-like}},
$$
where ${\bf q}$ is the four-momentum transfer of the interaction, calculated from the incoming electron momentum, ${\bf p}_{1}$, and outgoing electron momentum, ${\bf p}_{2}$, as ${\bf q} = {\bf p}_{1}-{\bf p}_{2}$.

A Form Factor, $F$, provides additional information on how the distributed structure of the nucleus modifies the interaction probability. Form factors are essentially the Fourier Transform of the density distribution, therefore more detailed measurements of the cross-section allow us to probe this distribution itself.

Electron scattering data at the time showed lots of bumps.





## 3.1 The Saxon-Woods Distribution
Details of the Form Factor here are beyond our scope now but the upshot is that a better model for the density distribution is given by the so called Saxon-Woods form.

This modifies the simple Top-Hat by introducing a smooth edge parameterised in terms of the radius, $r$, as follows:

$$
\rho(r) = \frac{\rho_0}{1+{exp}[\frac{r-a}{d}]}
$$


- Here $a$ is the "edge" of the nucleus and $d$ is the so-called Skin or Surface Thickness.
- The same form applies for both the charge and density distribution. 

The plot below shows the charge density vs distance r from the centre of the nucleus.


:::{figure-md} saxonwods
<img src='figures/saxton_woods.png' width="100%" alt="Saxon Woods Form">
Saxon Woods Form vs distance
:::


**Typical Values For the charge density distribution**

$$
\rho_{\textnormal{charge}}^{0} = \frac{\rho^0_{\textnormal{charge}}}{1+\textnormal{exp}[\frac{r-a}{d}]}
$$

- $a = 1.07 A^{1/3} ~\textnormal{fm}~~\textnormal{\it (radius)}$ 
- $d = 0.54~\textnormal{fm}~\textnormal{\it (skin thickness)}$ 
- $\rho^{0} = 0.06-0.08~e~\textnormal{fm}^{-3}~\textnormal{\it (average charge density)}$
- Note: We expect $\rho^{0}$ to be lower for heavier nuclei.


**Typical Values For the charge density distribution**

$$
\rho_{\textnormal{mass}}(r) = \frac{\rho^0_{\textnormal{mass}}}{1+\textnormal{exp}[\frac{r-a}{d}]}
$$

- $a = 1.2 A^{1/3} ~\textnormal{fm}~~\textnormal{\it (radius)}$ 
- $d = 0.75~\textnormal{fm}~\textnormal{\it (skin thickness)}$ 
- $\rho^{0} = 0.17~e~\textnormal{fm}^{-3}~\textnormal{\it (average charge density)}$

Key take-aways:
- Modifications are needed between mass distributions and charge distributions due to zero-charge neutrons.
- The parameter values are quite similar in both cases.
- The charge radius and mass radius both scale as $A^{1/3}$.
- The central denisties are constant, independent of how many nucleons there are in the nucleus.


## 3.2 The Liquid Drop Model

All the above early studies and information on the nucleus start to lead us towards some basic models to explain the behaviour of nuclei. The most basic is the Liquid Drop Model (LDM), based on a description of the nucleus as a drop of "Nuclear Fluid" analogoous to a water droplet.

The LDM arises from the following main observations:
- Nuclei are spherical (in general) with Central Density having a fixed value independet of radius. i.e. no matter how many nuclens you pile in to make your nucleus bigger, the density remains the same, the nuclear fluid is Incrompressible (like a water drop).
- This matches well the observation that the radius (size) of the nucleus goes as $R \sim A^{1/3}$ and tells us that the force binding the nucleons together is short tange - rather like the intramolecular force in liquids.
- The Binding Energy Curve suggests that whatever size of a nucleus, a nucleon situated inside has roughly the same binding energy as all other nucleons. It takes roughly the same energy to free it no matter how many other nucleons are present.
   
These four arguments allow us to build a simple model of the nucleus that satisfies all constraints - The Liquid Drop Model. The assumptions of the model are:

1. The forces between nucleons are; **Repulsive** at very short seperations, **Attractive** at seperations similar to particle size, and **Negligible** at larger distances. The collective attraction of nuclei is what keeps them bound together contributing a negative **Volume Energy**.
2. The centre of the nucleus is an **Incrompressible Nuclear Fluid** with constant density which is independent of radius, and having a positive **Surface Tension Energy**. Assuming the fluid is non-rotating, in absence of other forces, the shape adjusts to minimise the surface tension energy resulting in a spherical shape.
3. If the drop carries Electric Charge then this is uniformly distributed throughout the drop. This combined with the Repulsive Foorce leads to an additional positive **Coulomb Potential Energy** in the nucleus.

Putting this together mathematically in the Liquid Drop Moodel (LDM) leads to an equation for the binding energy for the nucleus as 

$$
B(A,Z) = a_{V}A - a_{s}A^{2/3} - a_{c}Z^{2}A^{-1/3}
$$

In line with our description you we have three terms:
$$
\textnormal{Volume Energy Term :}~~~a_{V}A
$$

$$
\textnormal{Surface Tension Energy Term :}~~~a_{s}A^{2/3}
$$

$$
\textnormal{Coulomb Potential Energy Term :}~~~a_{c}Z^{2}A^{-1/3}
$$

Note dividing B(A,Z) by the total nucleons A, gives us a prediction for the binding energy per nucleon plot we discussed in Lecture 1. 

By convention we talk about the binding energy as a positive value (e.g. 52MeV for Carbon-12) when in fact it's a negative value when considering all nucleons in the nucleus - **energy needs to be added** to the system for us to liberate a nucleon. Our **negative** volume potential energy term above therefore corresponds to a positive term in the binding energy estimate in the LDM equation.


To understand in a bit more detail the components f the SEMF lets go through them one by one seeing how they improve our fit to real data. We'll take the data frmo the IAEA database (here), and select only the most abundant nuclei with the highest binding energy for each possible value of $A$. This is how the figures you've already seen for binding energy are actually made.


:::{figure-md} semf1
<img src='figures/semf_goodness_dataonly.png' width="100%" alt="Rutherford Form">

SESMF
:::

### 3.2.1 The Volume Energy Term

This is the main term, its positive, associated with the short range forces between nucleeons pulling them teogether, its the same for all nucleons (a constant),hence the total for a nucleus is just propertional to the number of nuceons A. 

$$
B_{E} \propto A = +a_{V}A ~~~~~~~~ 
$$


The $a_{V}$ term sets the scale of the energies we are dealing with in nuclear physics. It is typically given as $a_{V} = 15.56~\textnormal{MeV}$. 

Once the other terms are included (subtracting from this Volume term) we find that a good typical value for the Binding Energy per Nucleon is about $8~\textnormal{MeV/nucleon}$. We therefore expect the other terms to reduce the binding energy by around $7-8~\textnormal{MeV}$.

:::{figure-md} semf1
<img src='figures/semf_goodness_uptovol.png' width="100%" alt="Rutherford Form">

SESMF
:::


### 3.2.2 The Surface Tension Energy Term
This is a correction to the Volume Term, subtracting fromit, to allow for the assumptiono that the Outer Nucleons near the surface will be less tightly bound. These nucleons make the nucleus weaker, so feel less of the Short Range Attractive Forces between nucleoons compared to those nucleons well inside the nucleus. It's like a Surface Tension Term. It's no surprise then that it is a proportional to the surface area which is proportional to $A^{2/3}$.

$$
B_{E} = -a_{s} A^{2/3} ~~~~ a_{s} = 17.23 MeV.
$$

See here the effect of the surface term. It has the greatest effect on small nuclei, because they have a greater fraction of their nucleons near the surface compared to inside. 


:::{figure-md} semf1
<img src='figures/semf_goodness_uptosurf.png' width="100%" alt="Rutherford Form">

SESMF
:::


### 3.2.2 The Coulomb Potential Energy Term
This second correction to the Volume Term comes because nuclei contain positively charged protons that repel each other. This Electrosttatic Repulsion also weakens the nucleus, hence a negative term, reducing the overall binding strength.

By assuming the protons are distributed evenly in the spherical nucleus we can deduce the equation by considering the repulsion of a shell of protons of thickness $dr$ due to those inside the shell, and integrating over the entire nucleus size.

Recall first that the electric potential energy of a charge $q_{1}$ in the potential of $q_{2}$ distance $r$ away is:

$$
E(r) = \frac{1}{4\pi\epsilon_{0}} \frac{q_{1}q_{2}}{r}
$$

The Charge Density (it is uniform remeber) is given by : 

$$
\rho_{C} = \frac{Q}{V} \approx \frac{3Ze}{4\pi r^{3}_{0}A}
$$

Based on this we see that the Electrostatic Energy in the shell $dr$, we call $dE_{e}$, is given by:

$$
dE_{e} = {4\pi r^{2} dr \rho_c} \times \frac{4\pi r^{3} \rho_{C}}{3} \times \frac{1}{4 \pi \epsilon_{0} r}
$$
which reduces to
$$
dE_{e} = \frac{4\pi^{4}\rho_{c}^{2}}{3\epsilon_{0}} dr
$$


Intregating this out to the maximum radius of the nucleus, $r=0\rightarrow R$, gives the total Electrostatic Energy:
$$
E_{e} = \int_{0}^{R} \frac{4}{3} \frac{\pi r^{4}}{\epsilon_0}\rho_{c}^{2}dr = \frac{4}{3} \frac{\pi R^{5}}{5\epsilon_{0}}\rho_{c}^{2}
$$

If we substitute in the charge density given earlier we get

$$
E_{e} = \frac{4}{3} \frac{\pi R^{5}}{5\epsilon_{0}} \frac{Z^{2}e^{2}}{(4/3)^{2} \pi^{2} R^{6}} =
\frac{3}{5} \frac{Z^{2}e^{2}}{4\pi \epsilon_{0}R}
$$

If we remember that the nuclear size is given by $R=r_{0}A^{1/3}$ where $r_{0}$ is the Nucleon Effective Radius and we gather the constants out we get
$$
a_{c} = \frac{3}{5} \times \frac{e^{2}}{4\pi \epsilon_{0} r_{0}} \approx 0.7~\textnormal{MeV}
$$
and
$$
B_{E} = -a_{C} \frac{Z^{2}}{A^{1/3}}
$$

This is close to our contribution we showed in the equations above, however the analysis includes a slight approximation. As charge is quantized the integration over $r$ should really only start once a single charge has been enclosed. If this is accunted for the **Total Electrostatic Energy** is actually given by
$$
B_{E} = -a_{C} \frac{Z(Z-1)}{A^{1/3}}
$$

The effect this has on our distributin is shown below. We can see that the cooulomb term adds some noise to oour prediction as it now depends on $Z$ and at higher $A$ the most stable value of $Z$ can vary slightly from nuclei to nuclei.


:::{figure-md} semf1
<img src='figures/semf_goodness_uptocoul.png' width="100%" alt="Rutherford Form">
SESMF
:::

## Conclusion

Now that we have our final electroostatic term you'll see we have a model which is much closer to the data for higher atomic mass nuclei. 

$$
B(A,Z) = a_{V}A - a_{s}A^{2/3} - a_{c}Z^{2}A^{-1/3}
$$

Insert final image of full model comparison.

This change in shape due to the Columb Term is of fundamental importance in Nuclear Physics and has profound implications further on in this course.

We see that the effect of the Coulomb Term is to bend the B/A curve down at higher A yielding a peak in the B/A curve. One implication concerns the existince of Nuclear Fission in nature. 
- The gradient of the B/A curve tells us whether energy is released as we move along it. For light nuclei below iron, if nucleons are **added** to the system for example through fusion, then energy is realeased. 
- In contrast however at higher atomic numbers, for example U-235, then energy is only released if nucleons are **removed** from the nucleus, for example if the nucleus is split up through nuclear fission.

:::{figure-md} semf1
<img src='figures/semf_goodness_simple_ratio.png' width="100%" alt="Rutherford Form">
SESMF
:::