(unit7:problems)=
# Unit 7 : Worked Problems


## Worked Example : Reaction Notation

**Write out the following reactions in the form $ a + A \to B + b $:**

1. $ ^{63}Cu(p,n)^{63}Zn $
2. $ ^{63}Cu(p,\alpha)^{60}Ni $
3. $ ^{112}Cd(d,3n)^{111}In $
4. $ ^{11}B(d,n)^{12}C $
5. $ ^{59}Co(d,2n+d)^{57}Co $
6. $ ^{19}F(\alpha,n)^{22}Na $

```{admonition} Solution
:class: note, dropdown

This is a straightforward question. All that you have to remember is that anything before the comma inside the brackets is on the left-hand side, and anything after the comma is on the right-hand side.

1. $ ^{63}Cu + p \to ^{63}Zn + n $
2. $ ^{63}Cu + p \to ^{60}Ni + \alpha $ (or $ ^{60}Ni + ^{4}He $)
3. $ ^{112}Cd + d \to ^{111}In + 3n $  
   (LHS could also be written as $ ^{112}Cu + ^{2}H $)
4. $ ^{11}B + d \to ^{12}C + n $  
   (LHS could also be written as $ ^{11}B + ^{2}H $)
5. $ ^{59}Co + d \to ^{57}Co + 2n + d $  
   (or $ ^{59}Co + ^{2}H \to ^{57}Co + ^{2}H + 2n $)
6. $ ^{19}F + \alpha \to ^{22}Na + n $  
   (LHS could be written as $ ^{19}F + ^{4}He $)

*As an additional exercise, check that all of these reactions are properly balanced, i.e., that they conserve charge and number of nucleons.*

```

## Worked Example : p-p Chain 

Write out the the three reactions that make up the pp chain in the Sun in nuclear physics notation:

1. $ p + p \to d + e^+ + \nu_e $
2. $ d + p \to ^{3}He + \gamma $
3. $ ^{3}He + ^{3}He \to ^{4}He + 2p $

```{admonition} Solution
:class: note, dropdown

```

## Worked Example : Alpha Reactionss

**If an $ (\alpha,n) $ reaction takes place on the following nuclei, what is the final nucleus in each case?**

1. $ ^{7}Li $
2. $ ^{12}C $
3. $ ^{63}Cu $

```{admonition} Solution
:class: note, dropdown
```

## Worked Example : Particle Physics Notation

**Write out the following reactions in particle physics notation:**

1. $ ^{63}Cu(\alpha,2n)^{65}Ga $
2. $ ^{53}Cr(\alpha,p)^{56}Mn $
3. $ ^{34}S(\gamma,p)^{33}P $


```{admonition} Solution
:class: note, dropdown
```

## Worked Example : Q-Values

**Calculate the Q-values for:**

1. $ ^{63}Cu(p,\alpha)^{60}Ni $
2. $ ^{112}Cd(d,3n)^{111}In $
3. $ ^{11}B(d,n)^{12}C $

```{admonition} Solution
:class: note, dropdown

(Note that tables of atomic masses can easily be found online. I used the NIST table for most of these, and Krane for isotopes not listed by NIST.)

Tabulated atomic masses are for the neutral atom. To avoid any risk of mismatched electron numbers, the safest course is to subtract off $ Zm_e $, where $ Z $ is the atomic number of the isotope in question and $ m_e = 0.00054858 \, u $ is the electron mass. This will give you the nuclear mass.

**1. $ ^{63}Cu(p,\alpha)^{60}Ni $**

- Mass of $ ^{63}Cu $: $ 62.929598 - 29m_e = 62.913689 \, u $
- Mass of proton: $ 1.007276 \, u $
- Total initial mass: $ 63.920966 \, u $ [there’s a rounding error here]
- Mass of $ ^{60}Ni $: $ 59.930786 - 28m_e = 59.915426 \, u $
- Mass of $ \alpha $-particle: $ 4.001506 \, u $ [looked up separately]
- Total final mass: $ 63.916932 \, u $

**Q-value:**
$$
Q = 63.920966 - 63.916932 = 0.004034 \, u = 3.758 \, \text{MeV}
$$

---

**2. $ ^{112}Cd(d,3n)^{111}In $**

- Mass of $ ^{112}Cd $: $ 111.902763 - 48m_e = 111.876431 \, u $
- Mass of deuteron: $ 2.013553 \, u $
- Total initial mass: $ 113.889984 \, u $
- Mass of $ ^{111}In $: $ 110.905109 - 49m_e = 110.878229 \, u $
- Mass of neutron: $ 1.008665 \, u $ [looked up separately]
- Total final mass (3 neutrons): $ 113.904224 \, u $

**Q-value:**
$$
Q = 113.889984 - 113.904224 = -0.014240 \, u = -13.26 \, \text{MeV}
$$

---

**3. $ ^{11}B(d,n)^{12}C $**

- Mass of $ ^{11}B $: $ 11.009305 - 5m_e = 11.006562 \, u $
- Mass of deuteron: $ 2.013553 \, u $
- Total initial mass: $ 13.020115 \, u $
- Mass of $ ^{12}C $: $ 12.000000 - 6m_e = 11.996709 \, u $
- Mass of neutron: $ 1.008665 \, u $
- Total final mass: $ 13.005374 \, u $

**Q-value:**
$$
Q = 13.020115 - 13.005374 = 0.014741 \, u = 13.73 \, \text{MeV}
$$

```


## Unworked Example : Additional Q-Values 

**Calculate the Q-values for:**

1. $ ^{63}Cu(p,n)^{63}Zn $
2. $ ^{59}Co(d,2n+d)^{57}Co $
3. $ ^{19}F(\alpha,n)^{22}Na $

**Calculate the Q-values for:**

1. $ ^{22}Na(n,p)^{22}Ne $
2. $ ^{23}Na(n,p)^{23}Ne $
3. $ ^{12}C(n,\gamma)^{13}C $
4. $ ^{13}C(n,2n)^{12}C $

**If you took samples of these isotopes ($ ^{22}Na, ^{23}Na, ^{12}C, ^{13}C $) and irradiated them with thermal neutrons ($ \sim 0.025 \, \text{eV} $), which reactions would take place?**



### Unworked Problem : Medical Isotope Reactions

**The medical isotopes $ ^{32}P $ and $ ^{89}Sr $ are produced in reactors by $ (n,p) $ processes. In each case:**

1. Identify the target nucleus.
2. Estimate the minimum neutron energy required to initiate the reaction.



### Worked Example: Types of Nuclear Reactions

**Two common reaction types are $ (d,p) $ and $ (\alpha,n) $. Which of these would you expect to go mainly through a direct interaction and which mainly via a compound nucleus? Justify your answer.**

```{admonition} Solution
:class: note, dropdown

1. You would expect the $ (d,p) $ reaction to be direct, and the $ (\alpha,n) $ to go through a compound nucleus.

2. The $ (d,p) $ reaction is a stripping reaction: the incoming deuteron has a neutron stripped off during the reaction. It seems reasonable that this could happen in an interaction involving relatively small momentum transfer to one or two nucleons in the target nucleus—the deuteron is very weakly bound (looking at the Q-value example, we see that $ m_p + m_n - m_d = 1.007276 + 1.008665 - 2.013553 = 0.002388 \, u = 2.22 \, \text{MeV} $), so losing its neutron does not seem unlikely. Furthermore, if this went through a compound nucleus, the compound nucleus would have to de-excite by emitting a proton. This is not very probable, because of the Coulomb barrier.

3. In contrast, in the $ (\alpha,n) $ reaction, we are asking the incoming $ \alpha $ particle (a much more tightly bound nucleus than the deuteron: $ 2m_p + 2m_n - m_\alpha = 0.030376 \, u = 28.3 \, \text{MeV} $) to lose three of its four nucleons by interacting directly with one or two nucleons on the surface of the nucleus. This seems inherently unlikely. On the other hand, the idea that a compound nucleus would de-excite by emitting a neutron is not unreasonable—there is no Coulomb barrier in this case.

4. We could test this reasoning by measuring the angular distribution of the proton and neutron. If the $ (d,p) $ reaction is dominated by a direct component as we expect, we should find that the proton angular distribution is forward peaked, i.e. it tends to be emitted at a small angle to the direction of the incoming deuteron. A compound-nucleus reaction, such as we believe to be responsible for $ (\alpha,n) $, should produce a fairly isotropic angular distribution (it may not be exactly isotropic, because of angular momentum effects, but it should not be forward peaked).

```


## Worked Example: Energy Loss in Elastic Scattering


**A neutron of kinetic energy $ E $ scatters elastically from a target atom at rest. Find the maximum energy lost by the neutron if the target is:**

1. $ ^{2}H $
2. $ ^{12}C $
3. $ ^{238}U $

```{admonition} Solution
:class: note, dropdown

We did not cover reaction kinematics explicitly in the lectures because there is nothing new in it: it’s simply an application of first-year (or A level!) classical mechanics. However, it is obviously necessary to be able to do such calculations to interpret the results of nuclear reaction experiments. Recall that nuclear physics experiments tend to involve MeV energies, so unless the projectile is an electron we can safely treat it as non-relativistic.

In this case, since the scattering is elastic, both kinetic energy and momentum should be conserved. It is reasonably clear that the energy loss of the neutron is maximised for a head-on collision, in which it is reflected back along its original path (see the expression in Q10(b) if this is not obvious to you).

The easiest way to work this out is to consider the centre of mass frame. As the total momentum of the system is $ m v $, where $ m $ is the mass of the neutron and $ v $ is its initial velocity, the velocity of the centre of mass must be given by:

$$
u = \frac{mv}{m + M}
$$

where $ M $ is the mass of the nucleus. The initial speed of the neutron in the centre of mass frame is therefore:

$$
u_n = v - u = \frac{M}{M + m} v
$$

In the COM frame, the speeds of the two objects don’t change in an elastic collision—only their directions do. The maximum energy loss corresponds to the case where $ u'_n = -u_n $: in the COM frame the neutron simply reverses direction. Converting back to the lab frame gives us:

$$
v' = u'_n + u = -\frac{M - m}{M + m} v
$$

Since the energy is equal to $ \frac{1}{2}mv^2 $, we have:

$$
E' = \frac{1}{2} m v'^2 = \frac{1}{2} m v^2 \left( \frac{M - m}{M + m} \right)^2 = E \left( \frac{M - m}{M + m} \right)^2
$$

To a reasonable approximation, we can take $ M = A m $, where $ A $ is the mass number of the nucleus. For the three cases (a), (b) and (c), this gives us:

- $ ^{2}H: E' = 0.11E $
- $ ^{12}C: E' = 0.72E $
- $ ^{238}U: E' = 0.98E $

The point to note here is that the neutron loses much more energy if it scatters off a target of similar mass (indeed, if it scatters off $ ^{1}H $, i.e. a proton, it can lose all its kinetic energy in one collision). This is important if you wish to moderate neutrons from MeV energies down to thermal energies, e.g., in a reactor: the process will be much more efficient if the neutrons scatter off some light nucleus (the ones commonly used are hydrogen (in the form of water), deuterium (as heavy water, $ D_2O $), and carbon). Scattering off the reactor’s uranium fuel will not have the desired effect.

```

## Unworked Problem : Thermal Neutrons

**Thermal neutrons have energies of order $ 0.025 \, \text{eV} $. If a target is irradiated by such neutrons, are the resulting reactions likely to be direct or compound-nucleus? Explain your reasoning.**


### Unworked Problem : Independence Hypothesis

**A study of the independence hypothesis compares the reactions $ ^{46}Ti(\alpha, pn)^{48}V $, $ ^{34}S(^{16}O, pn)^{48}V $, and $ ^{28}Si(^{22}Ne, pn)^{48}V $:**

1. Based on compound-nucleus theory, what do you expect this study to find?
2. The cross section for $ ^{46}Ti(\alpha, pn)^{48}V $ peaks at an $ \alpha $-kinetic energy of $ 32 \, \text{MeV} $ (in the lab frame). At what $ ^{16}O $ and $ ^{22}Ne $ kinetic energies would you expect the other two cross sections to peak, based on your answer to part (a)?
3. The magnitude of the cross section for $ ^{46}Ti(\alpha, pn)^{48}V $ is found to be much higher than for $ ^{34}S(^{16}O, pn)^{48}V $. Does this invalidate compound-nucleus theory? Explain your reasoning. (*Hint: consider the charges of the nuclei involved in the reactions.*)



### Unworked Problem : Reaction Resonances

**The diagram shows a resonance in the reaction $ ^{13}C(n, \gamma)^{14}C $:**

1. Calculate the momentum of the neutron at the peak of the resonance. (*Hint: recall that a neutron with a kinetic energy of order $ 150 \, \text{keV} $ is not relativistic.*)
2. Hence calculate the kinetic energy of the $ ^{14}C $ nucleus after the collision (but before the $ \gamma $-emission).
3. Determine the energy of the excited state corresponding to this resonance. Compare your answer with the known energy levels of $ ^{14}C $ (see, for example, the Triangle Universities Nuclear Laboratory website).
4. Estimate the lifetime of this state.

**Relevant atomic masses:**
- $ ^{13}C: 13.0033548 \, u $
- $ ^{14}C: 14.0032420 \, u $
- $ n: 1.0086650 \, u $
- $ 1 \, u = 931.502 \, \text{MeV/c}^2 $



### Unworked Problem : Momentum Transfer

**A $ (d, p) $ scattering experiment on a $ ^{40}Ca $ target (i.e. $ ^{40}Ca(d, p)^{41}Ca $) finds a peak in the proton energy spectrum at a proton energy of $ 10.29 \, \text{MeV} $, measured at an angle of $ 67.5^\circ $ (in the lab frame) to the initial deuteron direction. The energy of the deuteron beam is $ 7.00 \, \text{MeV} $:**

1. Find the momenta of the incident deuteron and outgoing proton.
2. Show that, assuming that the target $ ^{40}Ca $ atom is stationary, the momentum of the $ ^{41}Ca $ atom is given by:
   $$
   p_{Ca}^2 = p_d^2 + p_p^2 - 2 p_d p_p \cos \theta
   $$
   where $ \theta $ is the angle between the incoming deuteron and outgoing proton directions, i.e., $ 67.5^\circ $. Hence calculate the momentum and kinetic energy of the $ ^{41}Ca $ atom.
   (*Hint: draw the triangle corresponding to the conservation of momentum, $ \vec{p}_d = \vec{p}_p + \vec{p}_{Ca} $. Recall that all the particles in this reaction are non-relativistic.*)
3. Calculate the Q-value of the reaction $ ^{40}Ca(d, p)^{41}Ca $.
4. Using your answers to parts (b) and (c), calculate the energy of the excited state of $ ^{41}Ca $ that produces this peak in the proton energy spectrum.

**Relevant atomic or particle masses:**
- $ ^{40}Ca: 39.9625909 \, u $
- $ ^{41}Ca: 40.9622779 \, u $
- Deuteron: $ 2.0135532 \, u $
- Proton: $ 1.0072765 \, u $


## Workde Example : Resonance in Neutron Cross-Section of $ ^{63}_{29}Cu $

The plot shows a resonance in the cross-section of neutrons incident on $ ^{63}_{29}Cu $. Calculate:

1. The branching fraction of the (n,γ) reaction.
2. The energy of the excited state.
3. The lifetime of the excited state.

Why is the line shape for (n, elastic) different from (n,γ)?

Atomic masses:
- $ ^{63}Cu $: 62.9295975 u
- $ ^{64}Cu $: 63.9297642 u
- $ n $: 1.0086649 u

Conversion: $ 1 u = 931.49 \, MeV $.

```{admonition} Solution
:class: note, dropdown


1. **Branching Fraction**: The branching fraction varies with energy. Using a reasonable approximation, the ratio of peak heights is 0.45.

2. **Energy of the Excited State**:  
   Using $ Q = m_i - m_f $,  
   $ Q = 0.0084982 \, u $ or $ 7.9160 \, MeV $.  
   Adding the neutron kinetic energy yields $ 7.9166 \, MeV $.

3. **Lifetime of the Excited State**:  
   The full width at half height is $ \Gamma = 2.3 \, eV $. Using the uncertainty principle $ \Gamma \tau \approx \hbar $,  
   $ \tau = \frac{1.05 \times 10^{-34}}{2.3 \times 1.6 \times 10^{-19}} = 2.9 \times 10^{-16} \, s $.

4. **Line Shape Difference**: The elastic scattering cross-section is affected by interference between direct and compound-nucleus components, while (n,γ) must occur via a compound nucleus.

```

## Worked Example: Neutron-Induced Fission of $ ^{235}U $

A possible reaction for the neutron-induced fission of $ ^{235}U $ is:


$$
 ^{235}_{92}U + n \to ^{139}_{52}Te + ^{94}_{40}Zr + X 
 $$


1. What is $ X $?
2. How much energy is released in this process?
3. Considering that $ ^{94}_{40}Zr $ is stable, but the stable isobar with $ A = 139 $ is $ ^{139}_{57}La $, how much additional energy is released by the decay of $ ^{139}_{52}Te $? If this takes place in a nuclear reactor, is this additional energy a useful contribution to the reactor's power output?
4. Using the Semi-Empirical Mass Formula (SEMF), which isobar with $ A = 139 $ would you expect to be stable? If it is not $ ^{139}_{57}La $, explain the apparent discrepancy.

Masses:
- $ ^{235}U $: 235.04393 u
- $ ^{139}Te $: 138.93473 u
- $ ^{94}Zr $: 93.90632 u
- $ ^{139}La $: 138.90635 u
- $ n $: 1.00866 u
- $ e^- $: 0.00055 u

SEMF coefficients:
- $ a_v = 15.5 \, MeV $
- $ a_s = 16.8 \, MeV $
- $ a_c = 0.72 \, MeV $
- $ a_a = 23.0 \, MeV $.

```{admonition} Solution
:class: note, dropdown

1. **What is $ X $?**  
   The total $ A $ is 236, and the total $ Z $ is 92. Accounting for all protons and neutrons, $ X $ is **3 neutrons**.

2. **Energy Released**:  
   Using atomic masses, $ Q = 235.04393 + 1.00866 - (138.93473 + 93.90632 + 3 \times 1.00866) = 0.18556 \, u $,  
   which converts to $ 172.85 \, MeV $.

3. **Additional Energy**:  
   $ ^{139}_{52}Te $ decays to $ ^{139}_{57}La $ via five $ \beta^- $ decays.  
   $ Q = 138.93473 - 138.90635 = 0.02838 \, u = 26.44 \, MeV $.  
   About half of this energy is useful (the rest is carried by neutrinos).

4. **Stable Isobar Prediction**:  
   Using SEMF, the isobar predicted is $ Z = 58.3 $. However, the shell model prefers $ Z = 57 $ because $ 139 - 57 = 82 $, a magic number.

```


## Worked Example: Proton-Boron Fusion Reaction

The reaction $ p + ^{11}B \to 3\alpha $ is sometimes considered for commercial fusion. Its advantages include all charged products and $ ^{11}B $ being stable and abundant (80% of natural boron). 

1. What is the $ Q $-value of this reaction?
2. What is the Gamow energy for this reaction?
3. Compare the Gamow energy for this reaction with that of d-t fusion.
4. Explain, as quantitatively as possible, why this reaction is unlikely to be used in commercial fusion reactors in the foreseeable future.

Relevant atomic mass:
- $ ^{11}B $: 11.0093052 u

Relevant particle masses:
- Proton ($ p $): 1.0072765 u
- Neutron ($ n $): 1.0086649 u
- Deuterium ($ d $): 2.0135532 u
- Tritium ($ t $): 3.0155007 u
- Alpha particle ($ \alpha $): 4.0015062 u.

```{admonition} Solution
:class: note, dropdown

1. **Q-Value**:  
   Using nuclear masses: $ Q = 11.0065622 + 1.0072765 - 3 \times 4.0015062 = 0.0093201 \, u = 8.68 \, MeV $.

2. **Gamow Energy**:  
   Reduced mass = $ 0.922823 \, u = 859.6 \, MeV $.  
   Gamow energy = $ 22.6 \, MeV $.

3. **Comparison with d-t Fusion**:  
   Gamow energy for d-t fusion = $ 1.18 \, MeV $, which is significantly lower than $ 22.6 \, MeV $.

4. **Feasibility**:  
   The required temperature for $ p + ^{11}B $ fusion is about 10× higher than for d-t fusion, making it impractical for current commercial reactors.

```

## Worked Example: $ ^{125}I $ Brachytherapy for Lung Cancer

A clinical trial found that $ ^{125}I $ brachytherapy was more effective than conventional radiotherapy for treating inoperable lung cancer. $ ^{125}I $ decays by electron capture with a half-life of 59.4 days, emitting a 35.5 keV X-ray. 

Given that:
- Mean tumor volume = 312.7 cm³
- Mean radiation dose = 141.6 Gy
- Mean density of the human body = 985 g/cm³

Determine:
1. The average mass of $ ^{125}I $ implanted.
2. The activity of $ ^{125}I $ at the time of implantation.

State any assumptions made in the calculations.

```{admonition} Solution
:class: note, dropdown


1. **Mass of Tumor**:  
   $ 312.7 \times 0.985 = 308 \, g = 0.308 \, kg $.

2. **Energy Deposited**:  
   $ 0.308 \times 141.6 = 43.6 \, J $.

3. **Number of Decays**:  
   Each decay deposits $ 35.5 \, keV = 5.69 \times 10^{-15} \, J $.  
   Number of decays = $ 7.67 \times 10^{15} $.

4. **Mass of $ ^{125}I $**:  
   Assuming each atom of $ ^{125}I $ has a mass of $ 125 \, u $,  
   $ 1.6 \times 10^{-9} \, kg $.

5. **Activity**:  
   $ A = 7.67 \times 10^{15} \times \ln 2 / 5.13 \times 10^6 = 1.0 \, GBq $.

```