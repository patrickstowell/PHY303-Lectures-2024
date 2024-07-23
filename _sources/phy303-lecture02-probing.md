# Lecture 2 : Nuclear Probes

Nuclei as opposed to atoms, have a net charge, from the sum of the proton charges. Neutrons can be considered essentially neutral, as the name suggests. However, in fact we know both neutrons and protons have an internal structure. Neutrons are composed of 3 quarks, (up, down, down for neutrons) that all have charge. The sum of the charges is zero but the structure does mean that charge-like phenomena exist for neutrons arising from their internal charge distribution. For example the neutron has a non-zero magnetic moment.

Of course Nuclei also have finite size, but it's impressively small when compared to the size of the electron orbitals in an atom. 


:::{figure-md} nuclear-size
<img src='figures/FiguresSlides.003.png' width="70%" alt="Nucleus Size">

Atomic versus Nuclear versus Proton size comparisons
:::

**Example scales of Aluminium**
Atomic Radius of Aluminium = $1.3 \times 10^{-10}~\textnormal{m}$
Nuclear Radius of Aluminium = $3.6 \times 10^{-15}~\textnormal{m}$


## 2.3 Nuclei Charge Density
Given that Nuclei have mass and charge then there is obviously going to be a density of mass and charge in nuclei, with some distribution. We'll consider this in more detail later. For now we can ask what is the average mass and charge density of the nuclear material.

To estimate this simply assume that nuclei are made of nucleons (protons and neutrons) that are something like **Hard Spheres** of radius $r_{0}$.

```{math}
:label: massdensity
\begin{equation}
\rho_{m} = \frac{M}{V} = \frac{3m_{n}}{4\pi r^{3}_{0}}
\end{equation}
```

```{math}
:label: chargedensity
\begin{equation}
\rho_{c} = \frac{Q}{V} = \frac{3Ze}{4\pi r^{3}_{0} A}\\
\end{equation}
```

$m_{n}$ = mass of neutron
$e$ = charge of electron


Note how the average nuclear and charge densities can be expressed independent of the Atomic Mass Number, $A$.

## 2.4 Measuring Nuclear Size
To get a better idea of the actual size, charge, and matter distribution, physicists use **Scattering Experiments**. The typical approach is to fire beams of particles at a fixed target and see what has happened to the particles on the othere side.

Typical experiments are : (i) electron scattering, (ii) alpha particle scattering, (iii) proton scattering, and (iv) neutron scattering and absorption.

For best results the *de Broglie Wavelength* of the probing nuclei must be a smaller than the nucleus, some typical beam energy values for nuclear probe experiments:
- alphas $>$ 2 MeV
- protons $>$ 8 MeV
- electrons $>$ 120MeV 

```{note}
Remember the de Broglie Wavelength is the wavelength of the probing beeam of particles which can be calculated from the momentum via $\lambda = h/p$.
```

A vital concept in such experiments is the notion of **Interaction Cross Sections**. This quantifies the probability an interaction occurs using the notion of a **Cross Sectional Area** for the nucleus.

## 2.5 Cross Sections
The Cross Section $\sigma$, quantifies the probability of a collision (or reaction) occurring between a beam particle and a target particle. It can be defined as an area around the centre of one of the particles within which the centre of second must fall if they are to collide as illustrated below.


:::{figure-md} particle-radius
<img src='figures/FiguresSlides.004.png' width="80%" alt="Nucleus Size Calculation">

Cross-section calculation based on assuming interacting bodies are hard spheres.
:::


Normally we can assume the particles are simple Hard Spheres such that if they all have radius R then the cross-sectional area is just . 

```{math}
:label: crosssectionarea
\begin{equation}
\sigma = \pi (2R)^{2}
\end{equation}
```

Due to the small sizes of nuclei, $\sigma$, is often expressed in units of Fermi squared $(10^{-30}m^{2})$ or barns $(10^{-28}m^{2}$) or even pico-barns$~(10^{-40}m^{2})$. In reality, as we will see, nuclei are not hard-edged and so cross-sections cannot be defined so geometrically, but it is a reasonable approximation for now.

## 2.6 Cross-section Targets
If we consider a material (a "Target") with $n$ particles per unit volume, then we can use the total cross-section, $\sigma$, to find the Mean Free Path for an interaction by a given particle fired at that material. For a Thin Target (or Foil) this is given by

```{math}
:label: crosssectionarea
\begin{equation}
\lambda = \frac{1}{n\sigma}.
\end{equation}
```

The mean free path or cross-section can be used to determine the reduction in beam particles for a given target. Consider we have a beam of $N_0 ~\textnormal{particles/s}$  impinging on a target so that a flux $N$ emerges.

- If the target has thickness $x$ then 
```{math}
:label: nthick
\begin{equation}
N = N_0 e^{-x/\lambda}
\end{equation}
```
    and the number of collisions in distance x is
```{math}
:label: cthick
\begin{equation}
C=N_0-N=N_0(1-e^{-x/\lambda}).
\end{equation}
```

- For thin targets ($x << \lambda$) instead the exponential term in the can be reduced to 
```{math}
:label: nthin
\begin{equation}
N=N_0\left(1+\frac{x}{\lambda}\right)
\end{equation}
```
    meaning the number of collisions becomes
```{math}
:label: cthin
\begin{equation}
C=\frac{xN_0}{\lambda} = N_{0}n\sigma x.
\end{equation}
```

We can see from Eq. {eq}`nthick` that given accurate prior knowledge of our starting beam flux and the thickness of our target, we can determine the cross-section of the total particles inside simply by measuring the change in intensity of our beam.




## 2.7 Partial and Differential Cross Sections

So far the Cross Section we have considered has really been the Total Cross Section, $\sigma_{T}$, referring  to the sum of all possible interactions involving the beam and target particles. In practice, there may be different types of interaction, or **Interaction Channels**, that happen each with their own seperate probability. The sum of all the cross-sections for each possible channel gives the total cross-section for the target. We introduce the term **Partial Cross Section** to distinguish these from the total cross-section, for instance $\sigma_{e}$.

In the previous sums we have also not said anything about where a given scattered particle goes, i.e. the angle through which it is scattered. It could be that all scattering angles are equally likely. This would be Isotropic Scattering. In practice however some angles end up being more likely than others due to various kinematic constraints depending on the interaction. To account for this we use the **Differential Cross-Section**:

$$
\frac{d\sigma}{d\Omega}
$$

Consider a finite element of slid angle $\Delta \Omega$ at angle $\theta$ as shown in Fig. {fig}`scatteringcone`. There is a part of $\sigma_e$ called $\Delta \sigma_{e}$ which corresponds to a probability of scattering into that cone. The Differential Cross Section for elastic scattering at angle $\theta$ is thus 

$$
\frac{d\sigma_{e}}{d\Omega} = (lim \Delta\Omega \rightarrow 0) \frac{\Delta \sigma_{e}}{\Delta \Omega}
$$

If we integrate $d\sigma/d\Omega$ over all possible scattering angles then we get back to the total cross section for that particular channel. 

:::{figure-md} scatteringcone
<img src='figures/FiguresSlides.005.png' width="80%" alt="Beam Direction">

Scattering angle cone used to define $\Delta \Omega$ in beam scattering experiments.
:::


Here we have considered a differential cross-section in terms of a solid angle, but in practice this can be given in terms of any kinematic variables derived from the interaction. For example the differential cross-section for electron scattering calculated in terms of the beam energy may be expressed as
$d\sigma/dE$, and a double differential cross-section in terms of beam energy and scattering angle may be expressed as $d^{2}\sigma/(dEd\theta)$.




## 2.8 Rutherford Scattering

The first scattering experiments, famously started by Rutherford, were performed using alpha particles. These experiments used a collimated polinium sample to create a beam of alpha particles which could be directed at a thin gold foil. A flourescent screen was used to determine the scattereing angle of the particles after the interaction. The cross-section measured in these interactions can then be used to determine the nuclear radius. Below is a sketch of Rutherfords original experiment using a gold thin foil as a target.


:::{figure-md} rutherfordexperimentt
<img src='http://hyperphysics.phy-astr.gsu.edu/hbase/nuclear/imgnuc/ruther.gif' width="100%" alt="Beam Direction">

Hyperbolic Trajectory of scattering in Rutherfrd scattering assuming charged deflection of the beam particles.
:::

Two important conclusions were drawn from the early electron scattering experiments:
- Nuclear have very small size, about $10^{-14}~\textnormal{m}$
- Nuclear Radii, $R$, are seen to increase with the total number of nucleons, $A$, such that $R\approx r_{0} A^{1/3}$, where $r_{0}$ is the nucleon radius. This suggests that nucleons are **Incompressible**.

Rutherford and others went further after these ground breaking experiments, to deduce an equation for the angle by which alpha particles scatter, known as the **Differential Cross Section for Rutherford Scattering**.


:::{figure-md} hyperbolic
<img src='figures/FiguresSlides.006.png' width="80%" alt="Beam Direction">

Hyperbolic Trajectory of scattering in Rutherfrd scattering assuming charged deflection of the beam particles.
:::



$$
\frac{d\sigma}{d\Omega_{R}} = \frac{z^{2}Z^{2}\alpha^{2}\hbar^{2}c^{2}}{4E^{2}} \frac{1}{sin^{4}(\theta/2)} \\
$$
$z$ is the charge of the projectile.
$Z$ is the charge of the scatterer.
$E$ is kinetic energy of the particle
$\theta$ is the scattering angle
$\alpha$ is the **fine structure constant**

```{note}
The fine structure constant defines the strength of electromagnetic interactions.
$$
\alpha = \frac{e^{2}}{\hbar c 4\pi \epsilon_0}
$$
```

Figure {img}`rutherfordform` predicts a form the cross section vs scattering as shown opposite.

:::{figure-md} rutherfordform
<img src='figures/rutherford_form.png' width="70%" alt="Rutherford Form">

Rutherford Cross-section Form for three different nuclei.
:::


## 2.9 Mott Differential Scattering

Unfortunately the Rutherford prediction has been found to give a poor fit to real data. The main reason being the assumption that alphas are point-like objects. An improvement, introduced by Mott, is to use electrons, that are indeed point-like and can also better probe the nucleus, if of sufficient energy. This requires taking account of the relativistic effects of high energy electrons, their Magnetic Moment and also the resulting Nuclear Recoil.

The result is a modification to the equation above, thus:
$$
\frac{d\sigma}{d\Omega_{M}} = \frac{d\sigma}{d\Omega_{R}} \times [1-\beta^{2} sin^{2} (\theta/2)]
$$

Hofstadter set up electron scattering experiments on nuclei to investigate the Mott scattering prediction, illustrated in the figures below. These experiments used electrons of 500 MeV to probe down to length scales of $2.5~\textnormal{fm}$.

:::{figure-md} Hofstadter
<img src='figures/FiguresSlides.008.png' width="100%" alt="Rutherford Form">

Hofstadter Data
:::


Hofstadter's experiments provided a stong constaint on the scattering cross-section of nuclei over a broad range of angles. Unfortunately however they showed that that the data still deviates even from the Mott prediction and more is needed to fully describe the nucleus. 

This deviation is now interpreted as telling us about the charge/matter distribution in the nucleus. That not only is the nucleus not point-like as assumed in the Mottt formula but it has a particular density profile and shape which can be further explicitly probed by electron scattering experiments.



## 2.10 Scattering Example









