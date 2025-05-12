(unit11:problems)=
# Unit 11 : Worked Problems


## Worked Example : Fission Neutrons

The cross sections for thermal neutron absorption and fission on $ ^{235}U $ are $ 97 \, b $ and $ 584 \, b $ respectively, and for $ ^{238}U $ 0 and $ 2.75 \, b $. How many fast neutrons are produced per incoming thermal neutron, on average, for (a) natural uranium, 0.72% $ ^{235}U $, and (b) enriched uranium, 4.0% $ ^{235}U $?

---

```{admonition} Solution
:class: note, dropdown

The fraction of incoming neutrons that will cause fission is:

$$

f_f = \frac{\sigma_f}{\sigma_a + \sigma_f},

$$

where $ \sigma_f $ is the fission cross section and $ \sigma_a $ is the absorption cross section.

For natural uranium:

$$

\sigma_f = 0.0072 \times 584 = 4.20 \, b,

$$

and

$$

\sigma_a = 0.0072 \times 97 + 0.9928 \times 2.75 = 3.43 \, b.

$$


Therefore, the number of fast neutrons per thermal neutron, assuming 2.4 neutrons per fission, is:

$$

\eta = 2.4 \times \frac{4.20}{4.20 + 3.43} = 1.3.

$$


For enriched uranium, the corresponding numbers are $ 23.4 \, b $, $ 6.5 \, b $, and $ 1.9 $. This demonstrates the advantage that we gain from enriching the fuel in fission reactors.

```


## Worked Example : CNO Fusion Q-Values

In stars heavier than the Sun, hydrogen fusion proceeds via the CNO cycle, which consists of the following six reactions:

- $ ^{12}C + p \to ^{13}N + \gamma $;
- $ ^{13}N \to ^{13}C + e^+ + \nu_e $;
- $ ^{13}C + p \to ^{14}N + \gamma $;
- $ ^{14}N + p \to ^{15}O + \gamma $;
- $ ^{15}O \to ^{15}N + e^+ + \nu_e $;
- $ ^{15}N + p \to ^{12}C + \alpha $ (note that this last step regenerates the original $ ^{12}C $).

Calculate the Q-values of each of these reactions, and show that they add up to $ 24.7 \, \text{MeV} $ (or $ 26.7 \, \text{MeV} $ including positron annihilations).

---

```{admonition} Solution
:class: note, dropdown

The relevant nuclear masses (subtracting off the electron masses in each case) are:
- $ ^{12}C: 11.996709 $
- $ ^{13}C: 13.000064 $
- $ ^{13}N: 13.001899 $
- $ ^{14}N: 13.999234 $
- $ ^{15}N: 14.996269 $
- $ ^{15}O: 14.998676 $.

The particle masses are:
- $ e^+: 0.00054858 $
- $ p: 1.00727647 $
- $ \alpha: 4.00150618 $.

Therefore, the Q-values are:
1. $ 11.996709 + 1.00727647 - 13.001899 = 0.002086 \, u = 1.94 \, \text{MeV} $;
2. $ 13.001899 - (13.000064 + 0.00054858) = 0.001286 \, u = 1.20 \, \text{MeV} $;
3. $ 13.000064 + 1.00727647 - 13.999234 = 0.008106 \, u = 7.55 \, \text{MeV} $;
4. $ 13.999234 + 1.00727647 - 14.998676 = 0.007834 \, u = 7.30 \, \text{MeV} $;
5. $ 14.998676 - (14.996269 + 0.00054858) = 0.001858 \, u = 1.73 \, \text{MeV} $;
6. $ 14.996269 + 1.00727647 - (11.996709 + 4.00150618) = 0.005330 \, u$; 
   $0.005330 \, u= 4.97 \, \text{MeV} $.

The total is $ 24.7 \, \text{MeV} $, as expected.

```
---

### Extended Problems

3. Repeat the above calculation for the pp-III chain, which is a minor branch of the pp chain consisting of the following reactions:
- $ p + p \to d + e^+ + \nu_e $;
- $ d + p \to ^{3}He + \gamma $;
- $ ^{3}He + \alpha \to ^{7}Be + \gamma $;
- $ ^{7}Be + p \to ^{8}Be + e^+ + \nu_e $;
- $ ^{8}Be \to 2\alpha $.

   This is a very minor branch of the pp chain in the Sun, accounting for only about 0.0015% of the helium produced, but is very important in solar physics. Suggest why this might be true.

4. Calculate the Q-values for the two d-d reactions, $ ^{2}H(d,n)^{3}He $ and $ ^{2}H(d,p)^{3}H $, and deduce the kinetic energies of the produced particles.

5. It was noted above that the CNO cycle dominates helium production in stars heavier than the Sun (more precisely, in stars heavier than about 1.1 solar masses, though this does depend on the star’s carbon content), whereas the pp chain dominates in lower-mass stars. Suggest a reason why this might be the case.

