# Lecture 5 : Shell Model Evidence

 We've seen how study of the binding energy curve for nuclei and basic features like the chart of stability has led to an empirical formula for the binding energy and the mass of nuclei through the semi empirical mass formular.

However notice how this derivation was only possible by merging two different concepts for nuclei. Firstly, regarding the nucleus as a single drop of Nuclear Material which acts as a Collective Body.  Secondly a concept that starts at to look at the quantum beehaviour of individual nucleonts and that they somehow lie in specific (and restricted) Energy LEvels.

So we have two sorts of model, a Collective Body Model, and an Individual particle Model coming together. They Assymetry Term and Pairing Term in the SEMF can only be explained assuming this second concept.

The SEMF or Binding Energy Equation gives a good  fit to the overall shape of the Binding Energy Curve and starts to give us the basis of a model for nuclei and how they behave. However, it has some failings. When we delve further into nuclei we find that this basis on which the SEMF is built is still not enough to explain many of the properties observed. 



**SEMF Advantages**
1. It makes good predictions of the masses and binding energies of most nuclei and explains the basic shape of the Binding Energy (BE) Curve
2. It allows predictions of the energy releasae in nuclear decay (or energy input needed to make a reaction occur)
3. It tells us why, for instance, fission can occur in nature.
   
**SEMF Disadvantages**
1. It does not explain why there are spikes in the BE curve at certain nuclei.
2. It does not explain their shape (why some are not spherical).
3. It doesn't provide information on Nuclei properties like Nuclear Spin, Parity, Magnetic Moment.


## 5.1 Shell Model Concept

We find evidence not only that we need to account for the preference for pairing and balance between neutrons and protons, but also that specific numerical N & Z combibnations have very different properties.

This crystallises in observation of Magic Number Nuclei, nuclei with Z or N=2, 8, 20, 28, 50, 82, 126... that have particularly stable properties, and mark a transition point for nucleei such that thoose with Z or N below a given Magic Number have very different behaviour to thooose above.

This leads to the idea that nucleons in nuclei somehow lie in Concentric Shells, analogous (but very different) to the way electrons lie in shells in atoms and similarly that a "filled" outer shell produces a more stable configuration.

## 5.2 Nuclear Shell Model Concept
This shell model idea is of course tied up with introoducing Quantum Mechanics to ouor nucleus. The basis of QM here as seen before, is that we introduce a Nuclear Potential Well. It is the QM treatment of this Well that will determine (1) the energy levels (shells) that nucleons are allowed to occupy, and (2) how many nucleons can occupy each level.


As an example the simplest model for the Nuclear Well might be that associated with a Harmonic Oscillator, resulting in equally spaced energy levels, More on this later.

TODO : IMage of nuclear model.

But first notice how off the idea is. The nucleons are somehow orbiting in a potential of their own making. Can this reaelly work? The nucleons are tightly bound in the nucleus with a radius much smaller than the case for electron orbitals. Why don't they collide if they are orbiting in shells? 



This looks like big step to take away from our SEMF so first let's start by looking at what real evidence we have for a shell-like structure anyway. In fact we can list 8 things starting with a few charts we have already covered.


## 5.2 Shell Model Evidence

### 5.2.1 Magic Numbers
   The SEMF does a good joob oon the basic shape, but a closer look reveals certain nuclei have much higher, or lower B/A than predicted These are most obvious at low A where peaks appear in multiples of 4 nucleons (e.g. 12C, 18O). In general also nuclei with Magic Number N and/or Z have a higher B/A indicating they are more tightly bound.

### 5.2.2 Odd-Even Parabolas
 A closer look at the chart of Nuclides showos that even nuclei with N&Z away from the major numbers are more likely to be unstable. If we plot nuclei that lie on a line of a constant A, for example A=121 we find that odd and even A nuclei sit on two seperate parabola. Whilst our delta term in the SEMF can account for some of this it cannot account for the difference across all nucleir.
   

Image of odd-even nuclei for the delta term.

Based on this we can make a prediction of which isotope of the given A is most stable against Nuclear Decay. From a parabola fit to the data shown of the form

$$
M(A,Z) = aA + bZ + cZ^{2}
$$
where $a$, $b$, and $c$ are free parameters that are nuclei dependent. We can determine the minima by finding the case where
$$
\frac{dM(A,Z)}{dZ} \rightarrow 0\\
$$

Whatever the nearest integer value of Z is at the minimum will be the isotope we are after. Notice hw the curves are symmetric about the minimum. This leads to the concept of **Mirror Nuclei**. This refers to a pair of nuclei that have the same $A$ but where the $N$ and $Z$ values are ereversed. An example is nitrogen-15 (7 protons and 8 neutrons) and oxygen-15 (8 protons and 7 neutrons).

The nuclear properties of a given Mirror Nuclei pair like this are similar. The chemical propereties of the associated neutral atoms (dicated by the electrons determinede by the number of protons only) will be very different of course.


### 5.2.3 The Relative Abundance of Nuclei in Nature

A very important piece of evience for the Shell Model comes from a plot of the Relative Abundance of nuclei in nature vs A. Again we see peaeks of high abundance for nuclei with Magic Number values of N, Z, or both.


There are a larger number of isotopes, isotoones at particular values of Z, N.

The Magic Numbers

2, 8, (14), 20, 28, 50, 82, 126

Reelative abundance efor different even-even nuclides, plotted as a function of A.



### 5.2.4 The Neutron Binding Energy

Apart from the basic binding energy curve, we can look at for instance, the energy required to remove a single neutrn from the nucleus vs the neutrn number. The plot shows by hw much this differs from the SEMF preediction in MeV.

We see disconintuities up to 2MeV at the Magic Numbers (Shall Closuree) - it is harder to rmove a neutron from a closed shell.

This dependence of the energy to remove the outer neutron is strong evidence for a shall structure. A neutron just aboove a closed shelll looks to be less tighty bound, reminisicent of the alkali metals in the chemical shell structure.

TODO : Add image of binding energy

### 5.2.5 Neutron Capture Energy

Kind of oopposite too the Neutron Binding Energy plot just shown is to look at the Neutron Capture Cross-section oof nuclei vs N. This measures how likly a given nuceus is to absorb an eextra neutron fired at it as shown here.e

Again we see peaks and troughs. The lowest values are at the Magic Numbers corresponding to filled shells in our modele - it is harder to add a neutron when the outer shell is full.


```{note}
Note how the cross section is highest for nuclei well away from the Magic Numbers. An example is Cd, which is used widely as a Neutron Sheild in nuclear experiments.
```

TODO : Add image of capture energy


### 5.2.6 Electric Quadrupole Moments

As nuclei are charged then if this charge is not spherically distributed we might expect to measure a non-zero Electric Quadrupole Moment (we cover EQM later). For a shell model those nuclei with closed shells should be spherically symmetric and have no EQM. For nuclei that do not have a closed shell we indeed see large EQM.

In the ploot below the EQM have been normalized to the size and charge of each nucleus and these so called Reduced Quadrupole Moments are plototeeed agains the number of protnos or neutrons - depending upon which is odd. Some EQM are very large, suggesting shapes which are strongly non-spherical.



TODO : Add Image of reduced quadrupole moment.




### 5.2.7 Nuclear Excitation Energy

The relative stability of closed shell nuclei is also indiciated by measuring the energy required tto take a nucleus from the Ground State to its First Excited State.

Here is an example plot for the excitationo energies for the even-A isotopes of lead. The requried energy is dramatically larger for the isotope with a Magic Number of neutrons. This is strong evidence for a shell model of the nucleus.

The isotope leead-208 is particularly unique in beind Doubly Magic Z=82 and N=126. This is a Double Closed Shell Nucleus and it takeese more than 2MeV to raise it to the first excited state.

TODO : Add Image of quadrupole moment.


### 5.2.8 The existince of double magic nuclei
So nuclei which have both neutron number and proton number equal to one of the Magic Numbers can be called Doubl eMagic, and are found to be particularly stable.

An example is calcium. It has exceptionally stable Doubly Magic Nuclei - two of them. Compared to the binding energy calcualted from the SEMF, they both have much moore than the expected binding eneregy.

These isotopes have Z=20 and N = 20 and 28, all three being magic numbers.

TODOO : Add CALCIUM IMAGE


### 5.2.9 Decay Chains End with Magic Number Nuclei

Finally, there are several decay chain sequences in nature, particularly that starting U-235. Stable isotpoes come at the end of all these principle radiaoctive series, and all end pooints have a magic number of protons or neutrons.

Here is the example Dcay Chain of U-238 which ends in Pb-206 (which has a magic number of proton 82)

Note how from the start to finish of this chain results in emission of a total of 8 alpha particles.

There is a similar Decay Chain starting with Thorium.

TODO : Add decay chain image.


### 5.3 Shell Model Challenge

All these observatioons strongly point to a shell Like arrangement of nucleons in the nucleus, whereby we envisage Energy Levels in which the nucleonos sit, sepereatede by gaps corresponding to the Magic Numbers for both Z and N given by : 2,8,14,20,28,50,82,128.

TODO: Add Shell Model Pictture


Our shell model will need to explain these characteristic numbers using QM to produce the quantised energy levels (shells), filling them with the correct number of states (nucleons) to reprduce the Magic Numbers.

So oour basic aim is to explain the Magic Numbers, i.e. all the Nuclear Energy LEvels, and then hopefully make new predictions that can be testde.

