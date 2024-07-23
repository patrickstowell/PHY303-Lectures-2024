
# Lecture 1 : Introduction

The path to modern nuclear physics is long and complex. It dates back to ancient Greece with the idea of elemental particles, and then much later Dalton and the notion of indivisible atoms. These concepts are basically atomic physics.


The modern field of nuclear physics really began however with the first detection of radioactivity by Becquerel, who observed that photographic plates fogged up in proximity to uranium ore. Eventually this was determined to be due due to spontaneous decay of nuclei in the ore. Rutherford went on and categorized emissions of radioactive substances, working to understand the properties of alpha, beta, and gamma ray particles. 


The major figure in nuclear physics however was Marie Curie. She and husband Pierre where the first to isolate and characterize radium. Marie Curie's ground breaking work led to the Nobel Prize in 1903. Her research was conducted in a time when the dangers of radiation were less well known, and Marie Curie's lab equipment and notebooks are still highly radioactive to this day.

```{note}
"I am one of those who think like Nobel, that humanity will draw more good than evil from new discoveries." - Marie Curie
```


In this course we will learn about the fascinating field of nuclear physics, covering the structure of individual nuclei, predicting the properties of different radioactive decays, and both the practical applications and dangers of nuclear radiation. 


## 1.1 Nuclear Isotopes

Isotopes are nuclei of a given element with a specific number of nucleons. They are commonly referred to by their atomic mass number, $A$, atomic number $Z$, and elemental symbol, $\textnormal{\bf S}$. For example:
- $\bf ^{238}_{92}U~$is an isotope of Uranium with $A=238$ nucleons ($Z=92$ protons and $N=146$ neutrons),
- $\bf ^{56}_{26}Fe~$ is an isotope of Iron with $A=56$ nucleons ($Z=26$ protons and $N=30$ neutrons).


Since the elemental symbol is determined by the number of protons typically we ignore the bottom number to save writing it every time. For example for uranium the following three terms are identical $^{238}_{92}\textnormal{\bf U} = \bf ^{238}U~ = \textnormal{U-238} = \textnormal{Uranium-238}$. 

Similarly we don't need to specify the number of neutrons, $N$, explicitly each time as this can be determined from $A=Z+N$.

Throughout this course the short hand form of $^{A}{\bf S}$ or $\textnormal{S-A}$ will be used to refer to nuclei so you should familiarise yourself with it.

## 1.2 Radium, Radon, and the U-238 Chain

Radioactive decay of nuclei can transmute one isotope into another with the emission of some form of radiation. The most common forms of radioactive decay for nuclei are spontaneous alpha emission, or beta-decay where a neutron decays into a proton releasing a gamma ray. As shown in the figure below we can represent one nucleus decaying into another by considering where each nucleus lies on a chart of $N$ versus $Z$.The most common forms of decay, alpha and beta decay, have their own characteristic steps through this $Z-N$ space.

:::{figure-md} transitiondiagram
<img src='figures/FiguresSlides.001.png' width="100%" alt="Transitions of N and Z for alpha and beta decays between nuclei">

Example how to interpret a decay chain transition diagram. Nuclei are plotted as a function of $N$ and $Z$. Different types of nuclear decays move around the chart in a characteristic way like chess pieces on a board.
:::


The resultant nuclei from a radioactive nuclei are not necessarily always stable. When one nuclei decays into another nuclei which may at some later time also decay, these are called **Decay Chains**. Radium, $^{226}{\bf Ra}$, is one radioactive isotope in a very import chain of isotopes that starts with $^{238}{\bf U}$ and ends with $^{206}{\bf Pb}$. As you can see in the figure below the decay chain can span 20 different nuclei if left long enough before finally ending at lead $(^{206}{\bf Pb})$ which is a stable end product that does not decay.


:::{figure-md} udecaychain
<img src='https://www.mdpi.com/toxics/toxics-02-00050/article_deploy/html/images/toxics-02-00050-g002.png' width="100%" alt="Decay chain transition diagram for the U-238 chain">

Decay chain diagram for the U-238 chain. The approximate half-lives for each element are shown underneath them.
:::


The decay rate of radioactive nuclei is dependent on the isotope and as shown in the figure above can vary significantly. Decay half-lives between gigayears down to seconds are observed in the $^{238}{\bf U}$ chain. Radon occurs in the middle of the $^{238}\textnormal{U}$ chain. Radon has serious health implications - it is an alpha emitter so when outside our bodies it can't cause much harm. However, since it is commonly a gas, it can enter the lungs and cause damage to cells. With a half life of 3 days it is a particular problem in underground locations as it can manifest from the rock and hang around in the air for several days before it is inhaled.


## 1.2 Radiation Risk and Health

Radon is actually the major source of natural background radiation that can be harmful to us. Here is a chart showing the various contributions:

:::{figure-md} radon-gas
<img src='https://www.epa.ie/media/epa-2020/environment-amp-you/radon/6.-Radon---lungs.jpg' width="60%" alt="Radon gas damage to the lungs">

Radon gas typically emits alpha particles. Outside the body these cannot do much damage as they are not penetrating. Howevere when inhaled alpha particles can cause major damage to cells in the lungs.
:::

Radiation in general is quantified in various units. For experimental physics the source activity in Becquerels is often considered. For health the most important is the Gray and Sievert. 

- A Becquerel is a measure of source activity. It corresponds to the number of radioactive decays per second (so is correlated with the number of high energy particles leaving the source).

- A Gray is $1~\textnormal{J/kg}$ of deposited energy. This depends on the source and it's activity, but also the stand-off distance to the source itself as radiation intensity falls off based on the inverse square law.

- The Sievert is a Gray multiplied by a dimensionless quantity $Q$ with value depending in the type of particle. $Q$ represents the different levels of damage that different particles can do to human cells. An alpha has a high $Q$ Value because it does more damage tissue than say electrons of the same energy.

Whilst a measurement in Becquerel's tells us how active a source is, the most important measure throughout applied nuclear physics is the Sievert. **A dose of one Sievert is lethal**. The allowed dose for workers in the UK is 20 millisieverts per year.

Here is a summary of various units used throughout the nuclear physics field:

 | Tables   | Source Activity | Absorbed Dose | Effective Dose | Intensity
|----------|-------------|------|---|---|
| Old unit | Curie | Rad | Rem | Roentgen |
| SI unit  | Becquerel | Gray | Sievert | ... |


```{note}
You'll notice that there is no current SI unit for intensity anymore. This is because measurement of intensity of a source at some standoff distance is somewhat arbitrary. Roentgen's are sometimes still used for this but commonly the effective dose at some distance is the quantity of interest. In radiation detector development commonly "$y$ Becquerels at distance $x$" or "$y$ mCuries at distance $x$" is used to define a reference source intensity at a given position.
```


## 1.3 Basic Properties of Nuclei

Now we'll start with some basic nomenclature and properties of Nuclei. As we mentioned before nuclei can be described in terms of:
- Number of protons (atomic number): $Z$
- Number of neutrons : $N$
- Number of nucleons (atomic weight) : $A=Z+N$

Nuclei can also be grouped according to $Z$, $N$, and $A$:
- Nuclides with **same $Z$** are **Isotopes**
- Nuclides with **same $A$** are **Isobars**
- Nuclides with **same $N$** are **Isotones**

The known elements cover essentially everything from Hydrogen, H-1 to Oganesson-294. The light elements have a strong tendency for $N$=$Z$ whilst for heavier elements the line bends following something closer to $N=1.5\times Z$. 


The most stable elements run along a **"Line of Stability"**. Nuclei that deviate from this line decay rapidly to more stable nuclei, converting excess neutrons to protons.

```{note}
Remember : Unstable nuclei want to head towards more stable states - **towards** the line of stability.
```


Below is a chart showing the **line of stability**. Around 3000 different nuclei have so far been confirmed, each specified by the proton number $(Z)$ and neutron number $(N)$. This nuclide plot is one of the most important plots in nuclear physics.


:::{figure-md} chart-of-nuclideslarge
<img src='https://d20khd7ddkh5ls.cloudfront.net/screen_shot_2020-12-11_at_10.34.44_am_2.png' width="100%" alt="IAEA Chart of Nuclides">

Chart of all known nuclides. All observed nuclei are given a square based on their $N$ and $Z$ value. As we move away from the black line in both directions the nuclei become more and more unstable.
:::

The international atomic energy agency (IAEA) has gone to great lengths to catalogue information on nuclear physics and radioactive decays. They provide a full library of the properties each known nuclei in this plot. A link to the IAEA's interactive nuclei viewer can be found at the following link: https://www-nds.iaea.org/relnsd/vcharthtml/VChartHTML.html


### 1.5 Nuclear Decay 
As indiciated in the first of the two previous plots, nuclei sometimes decay, basically so that a more stable state is reached, with N and Z values somewhere along the Line of Stability. Whilst we've discussed the dominant decays in the U-238 chain, there are actually six types of nuclear decay we need to remember.
1. **Alpha Decay** - Spontaneous emission of an $\alpha$ particle, $\Delta Z=-2, \Delta N=-2$
2. **Beta Decay** - Spontaneous decay of a neutron into a proton, $\Delta Z=+1, \Delta N=-1$
3. **Neutron Emission** - Spontaneous ejection of a neutron from the nucleus, $\Delta Z=0, \Delta N=-1$
4. **Proton Emission** - Spontaneous ejection of a proton from the nucleus, $\Delta Z=-1, \Delta N=0$
5. **Positron Emission** - A proton emits a positron and turns into a neutron , $\Delta Z=-1, \Delta N=+1$
6. **Electron Capture** - A proton captures an orbiting electron, turning into a neutron and emitting a neutrino, $\Delta Z=-1, \Delta N=0$

:::{figure-md} chart-of-nuclides
<img src='figures/FiguresSlides.002.png' width="100%" alt="Possible decay steps in a chart of nuclides">

Possible decay steps in a chart of nuclides. Different decay channels correspond to different steps through the grid. The most common decays are still Alpha and Beta decay.
:::




### 1.6 Mass Calculations
Obviously Nuclei have Mass! But this turns out to be more complicated than you might think and we cannot simply add up the masses of the nucleons inside to get the total of the bound state.

It is also important to understand if we are considering Nuclear Mass or Atomic Mass. A nucleus is the part of an atom that is made only of protons and neutrons (Nucleons). If electrons are included, then we have an atom (neutral or ionised depending no the number of electrons).

The mass of an atom is dominated by the Nucleons so in many cases in nuclear physics it is a reasonable assumption to assume the atomic mass is the same as the nuclear mass. However, this is not always true, for instance in Beta Decay Calculations, as we will see later.Remember that in Nuclear Physics we tend to deal with energies (masses) in the MeV range. Whereas for electrons in orbitals (Atomic Physics) we consider eV and keV. 


To make our lives easier whn carrying around a lot of $\textnormal{MeV}$ terms in nuclear physics it is helpful to define a standard mass close to the nucleon mass. This is the Unified Mass Constant (u).

Nuclear masses are typically expressed in terms of unified mass constant ($u$). The mass of a $\textnormal{Carbon-12}$ atom is defined to be exactly $12u$, so that

```{math}
:label: atomicmassunit
\begin{equation}
u = 1.66056\times 10^{-27}~\textnormal{kg} = 931.5 \textnormal{MeV/c}^2.
\end{equation}
```

This results in the proton, neutron, and electron masses being defined as:
- $m_p$ = $1.672\times 10^{-27}~\textnormal{kg}$ = $1.007276~u$ = $938.28~\textnormal{MeV/c}^2$
- $m_n$ = $1.675\times 10^{-27}~\textnormal{kg}$ = $1.008665~u$ = $939.57~\textnormal{MeV/c}^2$
- $m_e$ = $9.109\times 10^{-31}~\textnormal{kg}$ = $0.000549~u$ = $0.511~\textnormal{MeV/c}^2$




#### 1.5 Nuclei have a Binding Energy
Once collections of nucleons are together inside a nuclei they generally want to stay together (at least for the most stable nuclei!). It takes additional energy to pull a nucleus apart - this is called the Binding Energy, and it is why we cannot simply add the mass of the nucleons together when determining the nuclear mass.

The mass of a given nucleus is always less that the sum of the masses of the individual nucleons inside. This is because the forces that hold nuclei together contribute additional negative energy, 

```{math}
:label: nuclearmass
\begin{equation}
M(A,Z) < ZM_{p} + NM_{n}.
\end{equation}
```

This nuclear mass deficit can be calculated as the difference beteween the nuclear mass, and the sum of individual nucleons.

```{math}
:label: nuclearmassdeficit
\begin{equation}
\Delta M(A,Z) = M(A,Z) - ZM_{p} + NM_{n}.
\end{equation}
```

The deficit shown in Eq. {eq}`nuclearmassdeficit` is related to the binding energy, $B$ of nuclei, corresponding to the energy required to split the nucleus apart into free nucleons
```{math}
:label: bindingenergyeq
\begin{equation}
-\Delta M(A,Z) = B
\end{equation}
```

Typically the binding energy is referred to as a positive value, but when considering its role in calculating the overall mass of the nucleus the change in mass is negative as shown in Eq. {eq}`bindingenergyeq`. As we discussed in the last lecture, stable nuclei have the highest binding energies. 

Since the neutrons and protons have different masses and properties, we expect that the binding energy for neutrons or protons to be slightly different. These individual binding energies are commonly referred to as Seperation energies. E.g. the neutron seperation energy for a Carbon-12 atom is calculated by taking the difference in binding energies between Carbon-12, and Carbon-11 (one less neutron) and is XXXX. Similarly the proton seperation energy for C-12 (difference between C-12 and N-12) is XXXX.


Below is the second most important plot in nuclear physics. It is a plot of the Average Binding Energy per total number of nucleons ($A=Z+N$) for all nuclei. 


:::{figure-md} binding-energy
<img src='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Binding_energy_curve_-_common_isotopes.svg/2560px-Binding_energy_curve_-_common_isotopes.svg.png' width="100%" alt="Plot of binding energy versus number of nucleons in the nucleus">

Plot of average binding energy per nucleon versus number of nucleons in the nucleus. A peak is observed at Fe-56, above which the binding energy reduces as larger nuclei become less tightly bound.
:::

There are some very important features here already that we should consider:
1. For heavy nuclei the binding energy is stable at around $8~\textnormal{MeV/nucleon}$.
2. The maximum binding energy is at $A=56$ which is Iron. $\textnormal{Fe-56}$ is one of the most stable well-bound nuclei.
3. Local peaks are visible when $A=4N$, e.g. $\textnormal{He-4}$. These features play important roles in how we build nuclear models as we will see later in the course.

You may have seen this plot already in second year nuclear physics, and may even understand the implications of these features, but in this course we are going to delve a bit deeper into actually where these features and look at how we construct models that can accurately describe this plot, and explain each of the decay phenomena we have discussed in this lecture in more detail.



#### Questions on Lecture 1
`````{note}
````{tab-set}
```{tab-item} Question 1
Compute the total binding energy and the binding energy per nucleon for (a) $^{7}Li$; (b) $^{20}Ne$; (c) $^{56}Fe$; (d) $^{235}U$.
```

```{tab-item} Hint
You can find the total mass for each nuclei online, you then just need to compare this to what you expect when summing individual nucleon masses in each one!
```

```{tab-item} Solution
```
````
`````



`````{note}
````{tab-set}
```{tab-item} Question 2
Compute the mass defects of (a) 32-S, (b) 20-F, (c) 238-U
```

```{tab-item} Hint
```

```{tab-item} Solution
```
````
`````


`````{note}
````{tab-set}
```{tab-item} Question 3
The proton sepeeration energy is the the amount of energy needed to remove a proton from the nucleus, equal to the difference in binding energies between $^{A}_{Z} X_{N}$ and $^{A-1}_{Z} X_{N-1}$. Calculate the proton seperation energy for the nucleus for 7-Li, 91-Zr, and 236-U.
```

```{tab-item} Hint
```

```{tab-item} Solution
```
````
`````


