(unit11:problems)=
# Unit 11 : Worked Problems


# Unit 5B: Examples and Problems

---

## Fission

### Example

**The cross sections for thermal neutron absorption and fission on \( ^{235}U \) are \( 97 \, b \) and \( 584 \, b \) respectively, and for \( ^{238}U \) 0 and \( 2.75 \, b \). How many fast neutrons are produced per incoming thermal neutron, on average, for (a) natural uranium, 0.72% \( ^{235}U \), and (b) enriched uranium, 4.0% \( ^{235}U \)?**

---

### Answer (Verbatim)

The fraction of incoming neutrons that will cause fission is:
$$
f_f = \frac{\sigma_f}{\sigma_a + \sigma_f},
$$
where \( \sigma_f \) is the fission cross section and \( \sigma_a \) is the absorption cross section.

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

For enriched uranium, the corresponding numbers are \( 23.4 \, b \), \( 6.5 \, b \), and \( 1.9 \). This demonstrates the advantage that we gain from enriching the fuel in fission reactors.

---

### Problems

1. Fill in the blanks in these fission reactions and calculate their Q-values:
   a. \( ^{235}U + n \to ^{90}Kr + ^{144}Ba + ? \);
   b. \( ^{239}Pu + \gamma \to ^{92}Sr + ? + 3n \);
   c. \( ^{252}Cf \to ^{106}Nb + ? + 4n \).

2. \( ^{252}Cf \) has a half-life of \( 2.64 \, \text{years} \) and a branching ratio for spontaneous fission of \( 3.09\% \). On average, each fission produces \( 3.76 \, \text{neutrons} \). How many neutrons per second are emitted by \( 1 \, \text{mg} \) of \( ^{252}Cf \)?

3. The distribution of the actual number of neutrons emitted per fission is remarkably Gaussian (see Krane, figure 13.7) with a standard deviation of \( 1.08 \). If the mean number of neutrons produced in the fission of \( ^{235}U \) is \( 2.42 \), what is the probability that a fission of \( ^{235}U \) will produce no neutrons?

4. Which of the following heavy nuclei would you expect to have large thermal neutron cross sections? Justify your answers:
   a. \( ^{251}Cf \);
   b. \( ^{253}Es \);
   c. \( ^{255}Fm \);
   d. \( ^{250}Bk \).

---

## Fusion

### Example

**In stars heavier than the Sun, hydrogen fusion proceeds via the CNO cycle, which consists of the following six reactions:**

1. \( ^{12}C + p \to ^{13}N + \gamma \);
2. \( ^{13}N \to ^{13}C + e^+ + \nu_e \);
3. \( ^{13}C + p \to ^{14}N + \gamma \);
4. \( ^{14}N + p \to ^{15}O + \gamma \);
5. \( ^{15}O \to ^{15}N + e^+ + \nu_e \);
6. \( ^{15}N + p \to ^{12}C + \alpha \) (note that this last step regenerates the original \( ^{12}C \)).

**Calculate the Q-values of each of these reactions, and show that they add up to \( 24.7 \, \text{MeV} \) (or \( 26.7 \, \text{MeV} \) including positron annihilations).**

---

### Answer (Verbatim)

The relevant nuclear masses (subtracting off the electron masses in each case) are:
- \( ^{12}C: 11.996709 \)
- \( ^{13}C: 13.000064 \)
- \( ^{13}N: 13.001899 \)
- \( ^{14}N: 13.999234 \)
- \( ^{15}N: 14.996269 \)
- \( ^{15}O: 14.998676 \).

The particle masses are:
- \( e^+: 0.00054858 \)
- \( p: 1.00727647 \)
- \( \alpha: 4.00150618 \).

Therefore, the Q-values are:
1. \( 11.996709 + 1.00727647 - 13.001899 = 0.002086 \, u = 1.94 \, \text{MeV} \);
2. \( 13.001899 - (13.000064 + 0.00054858) = 0.001286 \, u = 1.20 \, \text{MeV} \);
3. \( 13.000064 + 1.00727647 - 13.999234 = 0.008106 \, u = 7.55 \, \text{MeV} \);
4. \( 13.999234 + 1.00727647 - 14.998676 = 0.007834 \, u = 7.30 \, \text{MeV} \);
5. \( 14.998676 - (14.996269 + 0.00054858) = 0.001858 \, u = 1.73 \, \text{MeV} \);
6. \( 14.996269 + 1.00727647 - (11.996709 + 4.00150618) = 0.005330 \, u = 4.97 \, \text{MeV} \).

The total is \( 24.7 \, \text{MeV} \), as expected.

---

### Problems

5. Repeat the above calculation for the pp-III chain, which is a minor branch of the pp chain consisting of the following reactions:
   a. \( p + p \to d + e^+ + \nu_e \);
   b. \( d + p \to ^{3}He + \gamma \);
   c. \( ^{3}He + \alpha \to ^{7}Be + \gamma \);
   d. \( ^{7}Be + p \to ^{8}Be + e^+ + \nu_e \);
   e. \( ^{8}Be \to 2\alpha \).

   **This is a very minor branch of the pp chain in the Sun, accounting for only about 0.0015% of the helium produced, but is very important in solar physics. Suggest why this might be true.**

6. **Calculate the Q-values for the two d-d reactions, \( ^{2}H(d,n)^{3}He \) and \( ^{2}H(d,p)^{3}H \), and deduce the kinetic energies of the produced particles.**

7. **It was noted above that the CNO cycle dominates helium production in stars heavier than the Sun (more precisely, in stars heavier than about 1.1 solar masses, though this does depend on the star’s carbon content), whereas the pp chain dominates in lower-mass stars. Suggest a reason why this might be the case.**



## Question 3: Proton-Boron Fusion Reaction

The reaction \( p + ^{11}B \to 3\alpha \) is sometimes considered for commercial fusion. Its advantages include all charged products and \( ^{11}B \) being stable and abundant (80% of natural boron). 

1. What is the \( Q \)-value of this reaction?
2. What is the Gamow energy for this reaction?
3. Compare the Gamow energy for this reaction with that of d-t fusion.
4. Explain, as quantitatively as possible, why this reaction is unlikely to be used in commercial fusion reactors in the foreseeable future.

Relevant atomic mass:
- \( ^{11}B \): 11.0093052 u

Relevant particle masses:
- Proton (\( p \)): 1.0072765 u
- Neutron (\( n \)): 1.0086649 u
- Deuterium (\( d \)): 2.0135532 u
- Tritium (\( t \)): 3.0155007 u
- Alpha particle (\( \alpha \)): 4.0015062 u.

---




