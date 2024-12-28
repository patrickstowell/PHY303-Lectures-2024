So there is strong evidence for shell structurte in Nuclei. This is compatible with a QM descriptioon with Nucleons occupying Energy Levels determined by a Central Nuclear Potential Well. We will discuss the form of this potential and the Nuclear Force between nucleons that determines its nature later. 


To deetermine the enrgy levels in the shell modeel we need to solve the full time-independent 3D Schrodingeer Equatin for particle mass $m$ and wavfunction $\psi$ which has the form:

$$
\frac{-\hbar^{2}}{2m} \nabla^{2} \psi(r,\theta,\phi) + V(r,\theta,\phi) \psi(r,\theta,\phi) = E \psi(r,\theta,\phi)
$$

For a given nucleeon, the forces acting on it by all the other nucleeons in thee nucleeus can be presented to firsst approximation by an average potential $V(r)$ whhich only depends on distancee frmo the core. We call this the Shell Theory Potential.


The origin of this potential $V(r)$ lise in the force that holds individual nucleeons toogether, the Nucleaer Force or N-N potential. So it is rasonabl to assum that the form and depth of $V(r)$ should reflecet the oveerall density distribution of the nucleons in the nucleus.



Right now we take the mass distribution given previously from the Saxon Woods

$$
\rho(r) = \frac{\rho(0)}{1+\textnormal{exp}(\frac{r-b}{a})}
$$

and invert it to get the potential $V(r)$. It is this function that goes into the Schrodinger equation to get the Eneregy Levels.


$$
V(r) = \frac{-V_{0}}{1+\textnormal{exp}(\frac{r-b}{a})}
$$

TODO : Add image of Saxon Woods.

The basis of this nuclear potential shape, for instance its spatial radius, is the force between nucleonos, the Nucleaer Force, that keeps nucleoons bound together. The "average" potential has a radius of the nucleus ($A^{1/3}$), which is much bigger in general than the range of the Nuclear Force, about $1.4~\textnormal{fm}$. Anyway for now we will just start to describe the QM result, the Shell Model in more detail, and how this helps explain many of the observed properties of Nuclei.


This guves us our **Average Potential** with radius sof the nucleus ($A^{1/3}$), much bigger than the rangee of the NUclear Force (aboutt 1.4 or so fm...)

In the shell model now since we are assuming spherical symmetry in our potential and the nuclus, we can simplify the spherical coordinates, splitting $\psi(r,\theta,\phi) = \Psi(r)\Theta(\theta)\Phi(\phi)$, means we can consider different possible spherical harmonics.

$$
\frac{-\hbar^{2}}{2m} \frac{d^{2}\Psi(r)}{dr^{2}} + V(r) \Psi(r) = E \Psi(r)
$$

TODO: Add solving schrodinger for nucleus.

https://web-docs.gsi.de/~wolle/TELEKOLLEG/KERN/LECTURE/Fraser/L6.pdf




A Majoor point is to realise that although Nuclei are composed of Nucleons they largely act as an isolated single entity. In particular they have a well defined Total Angular Momentum called Nucleer Spin $I$. But nucleons also have Angular Momentum ($l$) and Intrinsic Spin ($s$). The vital point in our QM shell model is that the $l$ and $s$ of all the nucleons together determines thee Total Nuclear Spin $I$.



The result of treating the nucleus in this way we will see is the ability to now predict
- Nuclear Magic Numbers
- Nuclear Spin $I$
- Nuclear Parity $\pi$
  
And quite good, but not prefect, predictions of
- Nuclear Magnetic Moments
- Nuclear Electric Quadrupole Moments
- Excited States

The key to this is to work out the Shell Energy Levels and then determine how many nucleons are allowed to occupy each level as determined by QM and the Exclusion Principle.


## Shell Model Quantum Mechanics

We start by considering the QM behaviour of an individual nucleon (p or n) in the Central Potential Well of the nucleus. 

When we invoke QM to solve the problem, by applying the Schrodinger equation, we end up with an Angular Momentum Quantum Number, $l$, that tells us about the spatial behaviour of wave function of the nucleon.

Tthe magneteidue is given by $\langle l^{2} \rangle  = \hbar^{2}(l+1)$

The angular motion is a constant of the mition and the uncerttainty principle gives us certain allowed "Substates"

$$
\langle l_{z} \rangle = \hbar m_{z} ~~~~\textnormal{where}~~~~ m_z=0,\pm1,\pm2,...,\pm l
$$

But nucleons also have an Intrinsic Angular Momemntum called Spin $s$ such that

$$
\langle s^{2} \rangle = \hbar^{2} s(s+1)
$$

This also has certain allowed spin substates

$$
\langle s_z\rangle  = \hbar m_{s} ~~~~\textnormal{where}~~~~ m_{s} = \pm \frac{1}{2}.
$$


The two quantities $l$ and $s$ can vector couple to give a new quantum number $j$, known as the Total Angular Momentum Quantum Number for the nucleon. In nuclear systems it is the $j$ that is the "good" quantum number.

```{note}
Remember a good quantum number is a quantity that remains constant and is conserved during a particular physical process or set of operations. 
```


We have seen that $l$ is always integer and $s$ is always half-integer +1/2 or -1/2. o the vector coupling means $j$ is als ging to be half-integer, as below for the example of $l=1$.

:::{figure-md} semf1
<img src='figures/FiguresSlides.011.png' width="100%" alt="Rutherford Form">

:::


- $l$ - from orbital angular momentum number *[Integer]*
- $s$ - from orbital angular momentum number *[Half-Integer]*
- $j$ - from orbital angular momentum number *[Half-Integer]*
  

### Putting Nucleons in Shells

It is tthe $j$ value that is going to tell us how to fill up the Shell Energy Levels.

For instance, in the example shown where we chose level $l=1$, we find we are allowed total $j$ values = $\pm\frac{1}{2}$ and $\pm\frac{3}{2}$. 

Each nucleon must have its own allowed state of $m_z$ and $m_s$ when considering possible values of $j$. As shwn in the figure ebelow this results in six possible states $3/2, 1/2, -1/2, -3/2$ for $j=3/2$, and $1/2, -1/2$ for $j=1/2$.


:::{figure-md} semf1
<img src='figures/FiguresSlides.010.png' width="100%" alt="Rutherford Form">
SESMF
:::


Similarly if we repeated the same process for $l=2$, would have possible $j$ values of $5/2, 3/2, 1/2$ implying a total of 10 nucleon statets allowed.

The sequence can be expressed as 
$$
n_{\textnormal{states}} = 2(2l+1)
$$

It is importtant to remember when calculating these state that protons and neutrons are counted seperately here. So for intance the $l=2$ level can have up to 10 protons **AND** 10 neutrons inside the shell.



### Nucleon and Level Notation

Based on this a notation for labelling levels has been developed in Nuclear Physics as below. This is annoyingly similar looking to that used for electrons in atomic orbits but is actually very different so be careful not to mix them up.


:::{figure-md} semf1
<img src='figures/FiguresSlides.012.png' width="100%" alt="Rutherford Form">
SESMF
:::


Note that we just state here a futher label n fr the basic energy level. Details of thiss are outside our scope here. However we can now easily label each of our states. For example for $n=2$, $l=1$ we have $2\textnormal{p}_{3/2}$ (4 nucleon states) and $2\textnormal{p}_{1/2}$ (2 nucleon states).


### First Model Predictions

We can now attempt a first prediction with this model, i.e. can we account for the Magic Numbers? The result is here:
The plot shows the energy level positions. See how for a given n value, e.g. n=1, the s, p, d, f values for l go in order of increasing energy. However, there is overlap between high n values with lw l and low n values with high l. e.g. 1f is below 2p.

The exact position of the levels is oouotside out scroopoe. What is important here is how they get filled with nucleons, in relation to the main gaps. This determines the Magic Numbers.

We find: $2, 8, 20, 40, 58, 92...!!$

What we find however is that although we get the first few Magic Numbers correct $(2, 8,$ and $20)$, the higher levels are completely wrong. The next two shells suggested by nature are actually at $28$ and $50$. The nuclear potential well used as the basis appears reasonable though. Trying modifications to the potential can help a bit but not enough to makee new shells so low, instead an extra term is needed.

### SPIN ORBIT CORRECTIONS
The answer turns out to be a so-called **Spin orbit Coupling** term. The propoosal of this critical extra term in the Nuclear Potential was made in 1949 by Maria Goeppert Mayer and Johannes Jense, recognised by award of the Nobel Prize in 1963 - together with Eugene Wigner.

The basis is to introduce a further contribution to the internuclear force and hence the potential $V(r)$ that depends on the orientation of the spin $s$ and angular momentum $l$. I.e. it turns out this extra factor causes a re-ording of the energy levels 
$$
V=V(r)l\cdot s.
$$

The effect of this term is illustarted below. Recall how the Nuclear Potential Well shape (we said it comes from the Saxon Woods distribution of matter above) determines the energy levels. The Spin Orbit Correction changes this shape. The potential is deeper (nucleons are more strongly attracted) if the $l$ and $s$ are aligned parallel, and less deep (nucleons repulsed more) if they are aligned anti-parallel.

Insert figuree efor spin orbit correctino.


If the nucleon is well inside the nucleus then it encounters as many other nucleons with **Spin-Up** as **Spin-Down** and so the effect will average out, but it does not average everywhere.


### Energy Levels with Spin-Orbit

The effect of this is to break the Degeneracy in the assignment of nucleons t energy levels by introducing new energy levels depending on the $j$ value.

For instance, considere the l=1 level. Previusly this had 6 nuclenos, 3/2, 1/2, -1/2, -3/2 (for the j=3/2) and 1/2, -1/2 (for the j=1/2) all in the same level. Now the j=3/2 nuclenos (parrallel l and s) geet their own new, lower, energy level. The j=1/2 nucleonss (anti-parallel $l$ and $s$) get their own neew, higher, energy level.


So the former degeneracy in which we had to consider all these 6 nucleons in one level is broken, and the previus single energy level becomes two, at different levels.

:::{figure-md} semf1
<img src='figures/FiguresSlides.013.png' width="100%" alt="Rutherford Form">
SESMF
:::

This effeect applies for all the $l$ levels, they all get split into two levels, except for $l$=0 (the $\textnormal{s}$ sharp) one becaue that only has one $j$ assignmeent, $j=1/2$ $($with values $1/2, -1/2$$)$.

### Modifiede Shell Model

The effect of the Energy Levels splitting is dramatic. As shown below it changes the position of the gaps, and also makes neighburing $j$ states jump over one another.

Impoortantly this one small change to the model nw gives us the right Magic Number squence: 2, 8, 20, 28, 50, 82, 126.

Seee how this gives the necessary extra splitting in the figure below. THe enumbere of states for each $l$ remains, we ejust break the degeneracy, creaeting more levels. We see a different clustering of levels, and different majoor "gaps" correspoonding to our magic numbers.


Notice for instance how the $1\textnormal{g}$ level splits. All the $1g_{1/2}$ nucleons get moveed down and the $1\textnormal{g}_{7/2}$ ones go up, creating a new gap when the total of 50 nucleons is reached.
