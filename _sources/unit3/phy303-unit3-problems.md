(unit3:problems)=
# Unit 3 : Worked Problems

(unit3:problem:example1)=
## Example 3.1 : Carbon Mass Calculation
Given the mass of a carbon-12 atom is $12u$, estimate the binding energy of the carbon nucleus.
```{admonition} Solution
:class: note, dropdown

First we start with the mass of the proton, neutron, and electrons in the atomic mass units. Since the mass if that of a carbon-12 atom, we include the electrons in our 
calculation.
```




# PHY303: Nuclear Physics - Examples

---

## 1.1 Example: Nickel Radius

In this example, we use Figure 2.4 of the textbook by *Martin* to estimate the radius of the \( ^{58}Ni \) nucleus.

### Assumptions

- The scattering is elastic, i.e., the energy of the outgoing electron equals the energy of the incoming electron. This is justified because the electron energy (\( 450 \, \text{MeV} \)) is much smaller than the rest mass of the nucleus (around \( 55 \, \text{GeV} \)).
- The momentum transfer \( q \) is given as:
  $$
  |q|^2 = |p_i - p_f|^2 = 4p^2 \sin^2 \frac{\theta}{2},
  $$
  where \( p_i \) and \( p_f \) are the initial and final momenta of the electron.

- The nucleus is approximated as a solid sphere with uniform density. The form factor \( F(q) \) is:
  $$
  F(q) = 3 \frac{\sin b - b \cos b}{b^3}, \quad b = \frac{qR}{\hbar}.
  $$

### Steps

1. **Determine the Momentum Transfer \( q_c \):**

   Using the first minimum in the cross-section (\( \theta_1 \approx 24^\circ \)):
   $$
   q_c = 2p \sin \frac{\theta}{2} = 2 \times 450 \, \text{MeV} \times \sin 12^\circ = 187 \, \text{MeV}.
   $$

2. **Calculate the Nuclear Radius \( R \):**

   The first zero of the form factor corresponds to \( b_1 = 4.49 \). Using:
   $$
   R = \frac{b_1 \hbar c}{q_c} = \frac{4.49 \times 197 \, \text{MeV} \cdot \text{fm}}{187 \, \text{MeV}} = 4.8 \, \text{fm}.
   $$

   Using the empirical formula \( R = 1.21 A^{1/3} \), we find \( R \approx 4.7 \, \text{fm} \), which is remarkably close.

---

## 1.2 Example: Nuclear Radius and Root-Mean-Square

The root-mean-square (RMS) of the nuclear matter radius is parameterized as:
$$
\sqrt{\langle r^2 \rangle} = 0.94 A^{1/3} \, \text{fm}.
$$

Under the approximation of a uniform sphere:
$$
\rho_M(r) = 
\begin{cases} 
\frac{M}{\frac{4}{3} \pi R^3}, & \text{if } r < R, \\
0, & \text{otherwise.}
\end{cases}
$$

The RMS is calculated as:
$$
\langle r^2 \rangle = \frac{3}{5} R^2, \quad \text{thus } R = \sqrt{\frac{5}{3} \langle r^2 \rangle}.
$$

Substituting, we derive:
$$
R = 1.21 A^{1/3} \, \text{fm}.
$$

---

## 1.3 Example: Nucleons Momentum

Using the Heisenberg uncertainty principle:
$$
\Delta x \Delta p \gtrsim \frac{\hbar}{2}.
$$

With \( \Delta x \approx 5 \, \text{fm} \), the momentum is estimated as:
$$
p c \approx \frac{\hbar c}{2 \Delta x} \approx \frac{200 \, \text{MeV} \cdot \text{fm}}{2 \times 5 \, \text{fm}} = 20 \, \text{MeV}.
$$

The speed is:
$$
\beta = \frac{v}{c} \approx 0.02,
$$
indicating that nucleons are non-relativistic.

---

## 1.4 Example: Nuclear Matter Density

Using the charge density \( \rho_\text{ch} \) from the Saxton-Woods distribution, the nucleon density is:
$$
\rho_\text{nucl} = \frac{A}{Z e} \rho_\text{ch}.
$$

For \( ^{12}C \):
$$
\rho_\text{nucl} = \frac{12}{6 e} \times 0.08 e = 0.16 \, \text{nucleons/fm}^3.
$$

For \( ^{208}Pb \):
$$
\rho_\text{nucl} = \frac{208}{82 e} \times 0.06 e = 0.15 \, \text{nucleons/fm}^3.
$$

---

## 1.5 Example: Carbon Binding Energy

Binding energy of \( ^{12}C \):
$$
B = 6 m_p + 6 m_n - M(^6_6C).
$$

Numerical calculation:
$$
B = 0.09894 \, u \cdot 931.5 \, \text{MeV/u} = 92.16 \, \text{MeV}.
$$

Binding energy per nucleon:
$$
\frac{B}{A} = \frac{92.16}{12} = 7.42 \, \text{MeV/nucleon}.
$$

---

## 1.6 Example: Coulomb Term in the SEMF

Electrostatic energy of a uniformly charged sphere:
$$
E = \frac{3}{5} \frac{Z^2 e^2}{4 \pi \epsilon_0 R}.
$$

Substituting \( R = 1.2 A^{1/3} \, \text{fm} \):
$$
E = 0.72 \frac{Z^2}{A^{1/3}} \, \text{MeV}.
$$

---

## 1.7 Example: SEMF Calculations

Python code snippet to calculate SEMF terms for various isotopes:

```python
# Constants
p_av = 15.56
p_as = 17.23
p_ac = 0.697
p_aa = 93.14
p_ap = 12.0

# Binding energy terms
B_v = p_av * A
B_s = -p_as * A**(2/3)
B_c = -p_ac * Z**2 * A**(-1/3)
B_a = -p_aa * (Z - A/2)**2 / A
B_p = -p_ap / A**(1/2)

# Pairing term
if (Z % 2 + (A - Z) % 2) == 0:
    B_p = -B_p
elif (Z % 2 + (A - Z) % 2) == 1:
    B_p = 0

# Total binding energy
B = B_v + B_s + B_c + B_a + B_p
