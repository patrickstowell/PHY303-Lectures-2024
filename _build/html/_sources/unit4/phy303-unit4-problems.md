(unit4:problems)=
# Unit 4 : Worked Problems

(unit4:problem:example1)=
#### Example 4.1 : Carbon Mass Calculation
Given the mass of a carbon-12 atom is $12u$, estimate the binding energy of the carbon nucleus.
```{admonition} Solution
:class: note, dropdown

First we start with the mass of the proton, neutron, and electrons in the atomic mass units. Since the mass if that of a carbon-12 atom, we include the electrons in our 
calculation.
```


# PHY303: Nuclear Physics - Examples from Unit 2

---

## 2.1 Example: Binding energy of $ ^{48}Ca $

In this example, we evaluate the binding energy of $ ^{48}Ca $ using the SEMF and compare with the measured value.

(The mass of $ ^{48}Ca $ is $ 47.9525229 \, u $.)

$ ^{48}Ca $ is made of 20 protons and 28 neutrons and is an isotope with a very long lifetime of about $ 6.4 \times 10^{19} $ years. It is unusually neutron-rich for such a light nucleus. It is a double-magic isotope, having a magic number of both protons and neutrons and hence a large binding energy.

The measured binding energy is given by the mass difference between its constituents and the mass of the isotope:
$$
B(48, 20) = 20 \times (m_p + m_e) + 28 \times m_n - M(48, 20) = 416.00 \, \text{MeV}.
$$

The SEMF can be used to calculate the binding energy value as $ 413.28 \, \text{MeV} $. Therefore, the SEMF underestimates the binding energy by $ 2.72 \, \text{MeV} $. For example, the nucleus is more "bound" than the model would tell us due to the fact that all the shells are complete.

We can repeat the same calculation for other calcium isotopes and plot the difference between the measured (experimental) value of the binding energy and the value calculated using the SEMF as a function of the atomic number $ A $. We observe how the double-magic number affects the results.

**Figure: Calcium Binding Energy Measured - SEMF** (See the graph on page 2 of the document.)

---

## 2.2 Example: Spectroscopic Notation

In nuclear physics, we use the same spectroscopic notation used in atomic physics.

In atomic physics, electrons are placed in shells identified by:

| Quantum Number | Symbol                   | Value                                  |
|----------------|--------------------------|----------------------------------------|
| Principal      | $ n $                 | Any integer $ n > 0 $               |
| Orbital        | $ \ell $              | Integer up to $ n-1 $ (atomic physics) |
| Magnetic       | $ m_\ell $            | Integer from $ -\ell $ to $ \ell $ |
| Spin           | $ m_s $               | $ \pm \frac{1}{2} $                 |

In the spectroscopic notation, rather than the number $ \ell $, we use a "name" for the orbital corresponding to the orbital quantum number, as shown below:

| Orbital | $ \ell $ | $ m $ Values          |
|---------|------------|-------------------------|
| $ s $ | 0          | 0                       |
| $ p $ | 1          | $ -1, 0, 1 $          |
| $ d $ | 2          | $ -2, -1, 0, 1, 2 $   |
| $ f $ | 3          | $ -3, -2, -1, 0, 1, 2, 3 $ |

As an example in atomic physics, the electron configuration of $ Na $ ($ Z=11 $) is written as:
$ 1s^2 2s^2 2p^6 3s^1 $, indicating how many electrons are present in each of the shells.

In nuclear physics, the same convention is used with two major differences:
- The limitation for $ \ell < n-1 $ is no longer in place. Such limitation derives from the solution of the Schrödinger equation for a central potential.
- The interaction between spin and angular momenta breaks the degeneracy between levels and further complicates the model.

---

## 2.3 Example: Adding Spin and Orbit Angular Momenta

Let us consider the angular momentum operator $ \vec{L} $ and the spin operator $ \vec{S} $. Any given quantum state can be expressed as a sum of eigenstates of the two operators.

For simplicity, let us consider the case when the orbital quantum number is $ \ell = 1 $ and the spin is $ \frac{1}{2} $. We can generalize later for different values of $ \ell $.

Since the operators $ \vec{L} $ and $ \vec{S} $ are independent, there will be 6 different eigenstates for different combinations of $ m_\ell $ and $ m_s $, e.g., there are 6 states indicated by $ |m_\ell, m_s \rangle $:

- $ | +1, +\frac{1}{2} \rangle, | +1, -\frac{1}{2} \rangle $
- $ | 0, +\frac{1}{2} \rangle, | 0, -\frac{1}{2} \rangle $
- $ | -1, +\frac{1}{2} \rangle, | -1, -\frac{1}{2} \rangle $

A quantum state can also be written as a sum of eigenstates of the combined operator $ \vec{J} = \vec{L} + \vec{S} $. Quantum mechanics rules tell us that the total angular momentum quantum numbers will be in the range:
$$
|\ell - s| \leq j \leq \ell + s.
$$

In this case, there will be two different angular momentum quantum states:
- $ j_1 = \frac{3}{2} $
- $ j_2 = \frac{1}{2} $

**Implications in Spectroscopic Notation:**
- $ 6p $: Split into $ 2p_{1/2} $ (2 levels) and $ 4p_{3/2} $ (4 levels).
- $ 10d $: Split into $ 4d_{3/2} $ and $ 6d_{5/2} $.
- etc.

---

For the remaining examples and problems, let me know if you want me to continue formatting the rest of the text into markdown or stop here!


# PHY303: Nuclear Physics - Examples from Unit 2

---

## 2.4 Example: Spin-Orbit Coupling

The spin-orbit potential can be expressed as:
$$
V_{\ell s}(r) \propto \vec{L} \cdot \vec{S}.
$$

The value of $ \vec{L} \cdot \vec{S} $ depends on the total angular momentum $ j $, which can take on two values:
- $ j = \ell + 1/2 $
- $ j = \ell - 1/2 $

The expectation value of $ \vec{L} \cdot \vec{S} $ for each case is given by:
$$
\langle \vec{L} \cdot \vec{S} \rangle = 
\begin{cases} 
\frac{\hbar^2}{2} (\ell + 1), & \text{if } j = \ell + 1/2, \\
-\frac{\hbar^2}{2} \ell, & \text{if } j = \ell - 1/2.
\end{cases}
$$

Thus, the spin-orbit interaction splits a single energy level into two:
1. $ j = \ell + 1/2 $: Lower energy.
2. $ j = \ell - 1/2 $: Higher energy.

This explains the splitting observed in nuclear energy levels. The magnitude of the splitting increases with larger $ \ell $.

---

## 2.5 Example: Magic Numbers in Nuclear Shell Model

Using the energy levels derived from the shell model, we find that the number of nucleons required to completely fill a shell corresponds to the so-called "magic numbers":
- $ 2, 8, 20, 28, 50, 82, 126 $.

These magic numbers correspond to nuclei with exceptional stability.

---

## Problems

### Problem 1

Determine the spin and parity of the ground states of the following nuclei, assuming the pairing hypothesis holds:
1. $ ^{16}_8O $
2. $ ^{17}_8O $
3. $ ^{33}_{16}S $
4. $ ^{39}_{20}Ca $

---

### Problem 2

**For $ ^{17}_9F $:**
1. Sketch the configuration of protons and neutrons in the ground state.
2. Use this configuration to predict the spin and parity of the ground state.
3. Explain the spin and parity of the $ (1/2)^+ $ and $ (1/2)^- $ excited states.

---

### Problem 3

Calculate the root-mean-square radius $ R $ of $ ^{16}O $, assuming:
1. A uniform sphere of radius $ R $ contains the entire nuclear charge density.
2. The RMS radius is related to $ R $ by $ R = \sqrt{\frac{5}{3} \langle r^2 \rangle} $.

---

### Problem 4

The binding energy per nucleon for $ ^{12}C $ is $ 7.68 \, \text{MeV/nucleon} $. Calculate the total binding energy of $ ^{12}C $. Compare this with the value calculated using the semi-empirical mass formula (SEMF).

---

### Problem 5

Consider $ ^{208}Pb $, a doubly magic nucleus with 82 protons and 126 neutrons.


