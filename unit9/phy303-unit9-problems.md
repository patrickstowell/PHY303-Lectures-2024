(unit9:problems)=
# Unit 9 : Worked Problems


### Worked Problem : Lithium-6 Capture

A thermal neutron beam with a flux of $ \Phi = 1 \times 10^6 \, \text{n/cm}^2/\text{s} $ is incident on a lithium-6-doped scintillator. The scintillator is a flat sheet with a thickness of $ d = 0.5 \, \text{cm} $, and it contains lithium-6 at a concentration of 5% by weight. The density of the scintillator material is $ \rho = 2.5 \, \text{g/cm}^3 $. Assume all lithium in the scintillator is in the form of $ ^6\text{Li} $ (i.e., 100% isotopic purity for simplicity). The microscopic cross section for thermal neutron capture on $ ^6\text{Li} $ is $ \sigma = 940 \, \text{barns} $ (1 barn = $ 10^{-24} \, \text{cm}^2 $).

**a)** Calculate the number density of $ ^6\text{Li} $ nuclei in the scintillator (in $ \text{atoms/cm}^3 $).

**b)** Determine the macroscopic cross section $ \Sigma $ (in $ \text{cm}^{-1} $) for neutron capture on $ ^6\text{Li} $.

**c)** What is the probability that a neutron will be captured while passing through the scintillator of thickness $ d = 0.5 \, \text{cm} $?

**d)** Calculate the reaction rate (number of neutron captures per second per cm²) in the scintillator.

---

```{admonition} Solution
:class: note, dropdown

### **Given:**
- Neutron flux $ \Phi = 1 \times 10^6 \, \text{n/cm}^2/\text{s} $  
- Scintillator thickness $ d = 0.5 \, \text{cm} $  
- Lithium-6 concentration: 5% by weight  
- Scintillator density $ \rho = 2.5 \, \text{g/cm}^3 $  
- Molar mass of scintillator $ M = 100 \, \text{g/mol} $  
- Microscopic cross section $ \sigma = 940 \, \text{barns} = 940 \times 10^{-24} \, \text{cm}^2 $  
- Avogadro’s number $ N_A = 6.022 \times 10^{23} \, \text{mol}^{-1} $

---

### **a) Number density of $ ^6\text{Li} $ nuclei**

We are told lithium-6 is 5% by weight of the scintillator.

So, mass of $ ^6\text{Li} $ per cm³ is:

$$

m_{^6\text{Li}} = 0.05 \times \rho = 0.05 \times 2.5 = 0.125 \, \text{g/cm}^3

$$

The molar mass of lithium-6 is approximately $ 6 \, \text{g/mol} $, so:


$$

n_{^6\text{Li}} = \frac{0.125}{6} = 0.02083 \, \text{mol/cm}^3

$$

Now convert to number of atoms:


$$

N_{^6\text{Li}} = n_{^6\text{Li}} \times N_A = 0.02083 \times 6.022 \times 10^{23} \approx 1.25 \times 10^{22} \, \text{atoms/cm}^3

$$

---

### **b) Macroscopic cross section $ \Sigma $**


$$

\Sigma = N \cdot \sigma = 1.25 \times 10^{22} \cdot 940 \times 10^{-24}

$$

$$

\Sigma \approx 11.75 \, \text{cm}^{-1}

$$

---

### **c) Probability of neutron capture in the slab**

The transmission probability through a material of thickness $ d $ is:

$$

T = e^{-\Sigma d}

$$
So the **absorption** probability is:

$$

P = 1 - T = 1 - e^{-\Sigma d} = 1 - e^{-11.75 \times 0.5} = 1 - e^{-5.875}

$$


$$

P \approx 1 - 0.0028 = 0.9972

$$

So, **approximately 99.72%** of neutrons are captured.

---

### **d) Reaction rate per cm²**


$$

R = \Phi \cdot (1 - e^{-\Sigma d}) = 1 \times 10^6 \cdot 0.9972 \approx 9.972 \times 10^5 \, \text{reactions/s/cm}^2

$$

```


### Worked Problem : Lithium Scintillator

When a thermal neutron is captured by a lithium-6 nucleus in a scintillator, the following exothermic reaction occurs:


$$

^6\text{Li} + n \rightarrow \alpha + ^3\text{H}

$$

This reaction has a Q-value of 4.78 MeV, which is entirely converted into kinetic energy shared between the alpha particle and the triton (³H). Assume the incident neutron is thermal and has negligible kinetic energy.

- The mass of the alpha particle can be approximated as 4 u, and the mass of the triton is 3 u in the relative mass distribution calculations.
- The scintillator produces 10,000 photons per MeV of alpha energy deposited.
- The light collection efficiency is 30%, and the photodetector quantum efficiency is 25%.

**a)** Calculate the kinetic energy of the alpha particle using conservation of momentum and energy.

**b)** Estimate the number of scintillation photons produced per neutron capture.

**c)** Determine the number of photons reaching the photodetector per capture, after applying the light collection efficiency.

**d)** Calculate the number of photoelectrons generated per second per cm² of scintillator, using the quantum efficiency and the capture rate from the previous question.


```{admonition} Solution
:class: note, dropdown

### a) Kinetic energy of the alpha particle

From conservation of momentum:


$$

m_\alpha E_\alpha = m_t E_t
\quad \text{and} \quad
E_\alpha + E_t = Q = 4.78 \, \text{MeV}

$$

Substituting $ m_\alpha = 4 $, $ m_t = 3 $, and solving:


$$

4 E_\alpha = 3 (4.78 - E_\alpha)
\Rightarrow 4 E_\alpha = 14.34 - 3 E_\alpha
\Rightarrow 7 E_\alpha = 14.34
\Rightarrow E_\alpha = \frac{14.34}{7} \approx 2.05 \, \text{MeV}

$$

The triton energy is $ E_t = 4.78 - 2.05 = 2.73 \, \text{MeV} $.

### b) Scintillation photons per capture


$$

\text{Photons} = E_\alpha \times (\text{light yield}) = 2.05 \, \text{MeV} \times 10,000 \, \frac{\text{photons}}{\text{MeV}} = 20,500 \, \text{photons}

$$

### c) Photons reaching the photodetector

Applying light collection efficiency of 30%:


$$

\text{Detected photons} = 20,500 \times 0.30 = 6,150 \, \text{photons}

$$

### d) Photoelectrons generated per second per cm²

Applying quantum efficiency of 25%:


$$

\text{Photoelectrons per capture} = 6,150 \times 0.25 = 1,537.5

$$


$$

\text{Total photoelectrons per second per cm}^2 = 1,537.5 \times 9.97 \times 10^5 \approx 1.53 \times 10^9

$$

```



## Worked Problem : Uranium Fission
Neutrons from uranium fission are emitted with typical energies of 2 MeV or so. In nuclear reactors, it is desirable to moderate these to thermal energies (0.025 eV), because thermal neutrons are much more efficient at inducing further fissions. If a reactor uses graphite ($ ^{12}C $) as a moderator, estimate how many times a neutron needs to scatter off a graphite nucleus in order to thermalize.


```{admonition} Solution
:class: note, dropdown


This is elastic scattering, so $ Q = 0 $. We can assume non-relativistic speeds since $ K_n \ll m_n c^2 $ (where $ K_n $ is the initial neutron kinetic energy).

The easiest way to tackle this is to consider the centre-of-mass frame. The velocity of the centre-of-mass frame is given by:

$$
V_{CM} = \frac{p_n}{m_n + M} = \frac{m_n v_n}{m_n + M},

$$
where $ M $ is the mass of the carbon nucleus, $ 12 - 6m_e = 11.996709 \, u $, and $ v_n $ is the initial velocity of the neutron in the lab frame.

The initial speed of the neutron in the centre-of-mass frame is:

$$
u_n = v_n - V_{CM} = v_n \left( 1 - \frac{m_n}{m_n + M} \right) = v_n \frac{M}{m_n + M}.

$$

Since this is elastic scattering, in the CM frame the magnitude of the velocities do not change—only the direction does. The maximum kinetic energy the neutron could have is the same as its initial energy $ K_n $: this represents a glancing blow with negligible energy transfer. The minimum energy would be when the neutron scatters back along its initial path. In this case, the speed of the neutron in the lab frame is:

$$
v_n' = V_{CM} - u_n = v_n \frac{M - m_n}{m_n + M},

$$
so the minimum kinetic energy is:

$$
K_n' = \frac{1}{2} m_n v_n'^2 = \frac{1}{2} m_n v_n^2 \left( \frac{M - m_n}{m_n + M} \right)^2 = 0.714 K_n.

$$

As a reasonable estimate, let’s therefore assume that on average the kinetic energy after the collision is $ K_n' = 0.86 K_n $ (halfway between the minimum and the maximum). Now, this doesn’t depend on what $ K_n $ actually is, so after $ N $ collisions the kinetic energy is:

$$
K_n^{(N)} = 0.86^N K_n.

$$

Therefore, if we take logs we can rearrange for N given a final target energy.

$$
\ln \left( \frac{K_n^{(N)}}{K_n} \right) = N \ln(0.86).
$$

Putting in the numbers:

$$
\frac{K_n^{(N)}}{K_n} = \frac{0.025}{2 \times 10^6} = 1.25 \times 10^{-8},
$$

so:

$$
N = \frac{\ln(1.25 \times 10^{-8})}{\ln(0.86)} = 120.
$$


```
