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


