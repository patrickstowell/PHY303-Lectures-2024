### Combined Equation Sheet

**Atomic Mass Unit**
```{math}
\begin{equation}
u = 1.66056\times 10^{-27}~\textnormal{kg} = 931.5 \textnormal{MeV/c}^2.
\end{equation}
```

**Nuclear Mass Deficit**
```{math}
\begin{equation}
\Delta M(A,Z) = M(A,Z) - ZM_{p} + NM_{n}.
\end{equation}
```

**Binding Energy Equation**
```{math}
\begin{equation}
-\Delta M(A,Z) = B
\end{equation}
```

**Nuclear Mass Density**
```{math}
\begin{equation}
\rho_{m} = \frac{M}{V} = \frac{3m_{n}}{4\pi r^{3}_{0}}
\end{equation}
```

**Nuclear Charge Density**
```{math}
\begin{equation}
\rho_{c} = \frac{Q}{V} = \frac{3Ze}{4\pi r^{3}_{0} A}\\
\end{equation}
```

**Cross-sectional Area**
```{math}
\begin{equation}
\sigma = \pi (2R)^{2}
\end{equation}
```

**Mean Free Path**
```{math}
\begin{equation}
\lambda = \frac{1}{n\sigma}.
\end{equation}
```

**Beam Intensity Reduction in Target**
```{math}
\begin{equation}
N = N_0 e^{-x/\lambda}
\end{equation}
```

**N Collisions in Target**
```{math}
\begin{equation}
C=N_0-N=N_0(1-e^{-x/\lambda}).
\end{equation}
```

**Rutherford Scattering**
```{math}
\begin{equation}
\frac{d\sigma}{d\Omega_{R}} = \frac{z^{2}Z^{2}\alpha^{2}\hbar^{2}c^{2}}{4E^{2}} \frac{1}{sin^{4}(\theta/2)} \\
\end{equation}
```
- $z$ is the charge of the projectile.
- $Z$ is the charge of the scatterer.
- $E$ is kinetic energy of the particle
- $\theta$ is the scattering angle
- $\alpha$ is the **fine structure constant**

**Mott Scattering Form**
```{math}
\begin{equation}
\frac{d\sigma}{d\Omega_{M}} = \frac{d\sigma}{d\Omega_{R}} \times [1-\beta^{2} sin^{2} (\theta/2)]
\end{equation}
```

**Form Factor Modification**
```{math}
:label: distxsec
\begin{equation}
\left(\frac{d\sigma}{d\Omega}\right)_{\textnormal{distributed}}  = |F({\bf q}^{2})|^{2}\times \left(\frac{d\sigma}{d\Omega}\right)_{\textnormal{point-like}},
\end{equation}
```

**Relation between Form Factor and Charge Distribution**
```{math}
:label: formfactor
\begin{equation}
F(q) = \int_{-\infty}^{\infty} e^{i~{\bf q} \cdot {\bf r} / \hbar} ~\rho({\bf r})~d^{3} {\bf r}
\end{equation}
```

**Saxon Woods Distribution**
```{math}
:label: saxonwoods
\begin{equation}
\rho(r) = \frac{\rho_0}{1+{\textnormal{exp}}[\frac{r-a}{d}]}
\end{equation}
```

**Typical Values For the charge density distribution**
```{math}
:label: chargedist
\begin{equation}
\rho_{\textnormal{charge}}^{0} = \frac{\rho^0_{\textnormal{charge}}}{1+\textnormal{exp}[\frac{r-a}{d}]}
\end{equation}
```

**Typical Values For the mass density distribution**
```{math}
:label: massdist
\begin{equation}
\rho_{\textnormal{mass}}(r) = \frac{\rho^0_{\textnormal{mass}}}{1+\textnormal{exp}[\frac{r-a}{d}]}
\end{equation}
```

**Liquid Drop Model Binding Energy Estimate per Nucleon**
```{math}
:label: simpledropcombined_totalequationperA
\begin{align}
B(A,Z)/A = a_{v} - a_{s}A^{-1/3} - a_{c} Z(Z-1) A^{-4/3} - a_{a}(A-2Z)^{2}A^{-2} \pm \delta A^{-1}
\end{align}
```
- $a_{v} = 15.5 \textnormal{MeV}$, 
- $a_{s} = 16.8 \textnormal{MeV}$, 
- $a_{c} = 0.72 \textnormal{MeV}$, 
- $a_{a} = 23.0 \textnormal{MeV}$, 
- $a_{p} = 12.0 \textnormal{MeV}$.

**Coulomb Energy Estimate**
```{math}
:label: simpledropmodel_energyintegralafter
\begin{equation}
E_{e} =
\frac{3}{5} \frac{Z^{2}e^{2}}{4\pi \epsilon_{0}R}
\end{equation}
```

**Coulomb Constant assuming spherical integration**
```{math}
:label: simpledropmodel_coloumbfinalterm
\begin{equation}
a_{c} = \frac{3}{5} \times \frac{e^{2}}{4\pi \epsilon_{0} r_{0}} \approx 0.7~\textnormal{MeV}
\end{equation}
```

**Nucleon Pairing Term**
```{math}
:label: simpledropcombined_terms
\begin{align}
\delta_{\textnormal{pair}} &= +a_{p}A^{-1/2} ~~~~\textnormal{for N odd AND Z odd}\\
\delta_{\textnormal{pair}} &= 0 ~~~~~~~~~~~~~~~~~~~\textnormal{for N even OR Z even} \\
\delta_{\textnormal{pair}} &= -a_{p}A^{-1/2} ~~~~\textnormal{for N even AND Z even}\\
\end{align}
```

**Nucleon Asymmetry Term**
```{math}
:label: simpledropcombined_assymn
\begin{align}
B_{A} = -a_{a} (A-2Z)^{2}A^{-1}
\end{align}
```

**MAGIC NUMBERS**
```{math}
:label: shellmodelnuclei
\begin{equation}
\bf \textnormal{Magic Nuclei -}~ Z~\textnormal{or}~N=2, 8, 20, 28, 50, 82, 126...
\end{equation}
```


**BINDING ENERGY SOLVING**

```{math}
:label: BindingEnergyParabolaDif
\begin{equation}
\frac{dM(A,Z)}{dZ} \rightarrow 0\\
\end{equation}
```

**SHELL MODEL POTENTIAL**
```{math}
:label: simpledropcombined_extraterms2
\begin{equation}
V(r) = \frac{-V_{0}}{1+\textnormal{exp}(\frac{r-b}{a})}
\end{equation}
```


**SHELL QUANTUM NUMBERS AND PROJECTIONS**
```{math}
:label: shellmdoelam
\begin{equation}
\langle l^{2} \rangle  = \hbar^{2}l(l+1)
\end{equation}
```

```{math}
:label: shellmodelamproj
\begin{equation}
\langle l_{z} \rangle = \hbar m_{z} ~~~~\textnormal{where}~~~~ m_z=0,\pm1,\pm2,...,\pm l
\end{equation}
```


```{math}
:label: shellmodelspin
\begin{equation}
\langle s^{2} \rangle = \hbar^{2} s(s+1)
\end{equation}
```

```{math}
:label: shellmodelproj
\begin{equation}
\langle s_z\rangle  = \hbar m_{s} ~~~~\textnormal{where}~~~~ m_{s} = \pm \frac{1}{2}.
\end{equation}
```

**SHELL MODEL SIMPLE STATES**

$$
n_{\textnormal{states}} = 2(2l+1)
$$


**SPIN ORBIT COUPLING POTENTIAL OPERATOR**

$$
V=V(r) \hat{L} \cdot \hat{S}.
$$


**PARITY COMBINATION**

```{math}
:label: paritycombination
\begin{equation}
\pi_{total}=\pi_{1}\pi_{2}\pi_{3}\pi_{4} = \prod_{A}(-1)^{l} = + (\textnormal{even})~~\textnormal{or}~~-(\textnormal{odd})
\end{equation}
```

**Magnetic Moment Free Nucleon**
```{math}
:label: giprojection
\begin{equation}
\mu = g_{I} \frac{e\hbar}{2m_{p}} I = g_{I} I \mu_{N}
\end{equation}
```

**Nuclear Magneton**
```{math}
:label: nuclearmagneton
\begin{equation}
\mu_{N} = \frac{e\hbar}{2m_{p}} = 5.05\times 10^{-27}\textnormal{J/T} = 3.25 \times 10^{-8} \textnormal{eV/T}
\end{equation}
```

**Magnetic Moment and Projection**
```{math}
:label: magneticmoment
\begin{equation}
\mu = g_{j}~j~\mu_{N}
\end{equation}
```

```{math}
:label: magneticmoment_obs
\begin{equation}
\mu_{obs} = g_j j_z \mu_N
\end{equation}
```


**Magneton Estimates**

```{math}
:label: gyromnagneticratio
\begin{equation}
g = g_{l} \frac{j(j+1)+l(l+1)-s(s+1)}{2j(j+1)} + g_s \frac{j(j+1)+s(s+1)-l(l+1)}{2j(j+1)}
\end{equation}
```

```{math}
:label: magnetonestimate
\begin{equation}
\frac{\mu}{\mu_N} = (j-\frac{1}{2})g_l + \frac{1}{2}g_s \rightarrow (stretched)
\end{equation}
```

```{math}
:label: jackknifeestimate
\begin{equation}
\frac{\mu}{\mu_N} = ((j+\frac{3}{2})g_l - \frac{1}{2}g_s))\frac{j}{j+1} \rightarrow (jackknife)
\end{equation}
```


**G Factors**
```{math}
:label: gyromagneticfactors
\begin{equation}
g_l = 1~~\textnormal{(proton)} ~~~~~~~ g_l = 0 ~~\textnormal{(neutron)}\\
g_{s} = 5.85 ~~\textnormal{(proton)} ~~~~~~ g_{s} = -3.826 ~~\textnormal{(neutron)}
\end{equation}
```


**Quadrupole Operations**

```{math}
:label: quadrupoleoperation
\begin{equation}
eQ_{EQM} = e\int \psi^{*} (3z^{2} - r^{2})\psi dV
\end{equation}
```

Calculations to find the expectation value $< \psi >^{2}$ end up giving as values for $Q$ for single particle missing/addition states of:

```{math}
:label: quadrupolecalculation
\begin{equation}
Q_{EQM} = - < r^{2} > \frac{2j-1}{2(j+1)}
\end{equation}
```


For unfilled shells with more than one particle missing:

```{math}
:label: quadrupoleunfilled
\begin{equation}
< Q_{EQM} > = < Q_{sp} > \left [ 1-2\frac{n-1}{2j-1} \right ]
\end{equation}
```


**NUCLEAR SURFACE BASED ON BETA**

$$
R(\theta, \phi) = R_{av} [Y_{00}+\beta Y_{20} (\theta, \phi)]
$$

**BETA BASED ON ELONGATION**

$$
\beta = \frac{4}{3} \sqrt{\frac{\pi}{5}} \frac{\Delta R}{R_{av}}
$$

**INTRINSIC ELECTRIC QUADRUPOLE MOMENT**

$$
Q_{0} = \frac{3}{\sqrt{5\pi}} R_{av}^{2} Z \beta (1+0.16\beta)
$$


**ENERGY LEVELS ROTATIONAL SPIN J**

$$
\frac{\hat{L}^{2}}{2I} \psi = E_{J} \psi
$$
$$
\hat{L}^{2} Y_{JM}(\theta,\phi) = J(J+1) \hbar^{2} Y_{JM} (\theta, \phi)
$$
$$
E_{J} = \frac{\hbar^{2}}{2I}J(J+1)~~~~~J=0,2,4,\ldots
$$

Note that $I$ here is the moment of inertia of the perturbed nucleus.

**ENERGY PREDICTION USING E2 State**

$$
E_{J} = \frac{1}{6} J(J+1)E_{2}~~~~~~~~~J=0,2,4,\ldots
$$

**VIBRATIONAL VARIATIONS**

$$
R(t, \theta,\phi) = R_{av} + \sum_{\lambda>1}^{\lambda=\infty} \sum_{\mu=-\lambda}^{\mu=+\lambda}  \alpha_{\lambda \mu}(t) Y_{\lambda \mu} (\theta, \phi)
$$

**VIBRATIONAL ENERGY LEVELS**

$$
E_{N} = \hbar \omega_{l} \left(\frac{2l+1}{2} +N \right)
$$

Here $N$ is the number of oscillator quanta, and $l$ is the quantized oscillator state (0-monopole, 1-dipole, etc). 

**GAMMA RULES**

- If $\vec{J_i}$ (initial spin vector) is equal to $\vec{J_f}$ (final spin vector) then the transition can't take place. Here the $J$ terms correspond to the vector components of the nuclear spin. When we say that the an equal $\vec{J}_{i}$ and $\vec{J}_{f}$ state mean that the transition can not take place we mean it in terms of the vector components since $\vec{J}_{i} = \vec{J}_{f} + \vec{L}$. We can however have cases where the overall nuclear spin $I$ is identical before and afterwards, in this case we expect the allow magnitude of $\vec{L}$ to be

$$
| I_{f} - I_{i} | \leq L \leq|I_{f} + I_{i}|
$$

- Parity is conserved. Electric multipole radiation has parity $(-1)^l$, while magnetic multipole radiation has parity $(-1)^{(L+1)}$.


**GAMMA TRANSITIONS**

- **Electric Dipole (E1) Transitions:** These transitions involve $ΔL = 1$ and result in a parity change of π = $(-1)^1$ = -1 (parity-changing). Electric dipole transitions are more common than other multipole transitions and have relatively higher probabilities. 

 - **Magnetic Dipole (M1) Transitions:** These transitions involve $ΔL = 1$ and result in a parity change of π = $(-1)^{1+1}$ = 1 (parity-preserving). Magnetic dipole transitions are less common than E1 transitions but still occur in certain nuclear decays.

 - **Quadrupole (E2) Transitions:** Quadrupole transitions involve $ΔL = 2$ and result in a parity change of π = $(-1)^2$ = 1 (parity-preserving). Quadrupole transitions are less probable than E1 and M1 transitions and are associated with higher-order nuclear excitations.


**The time for half the sample to decay (half-life)**

$$T_{1/2} = \tau \textnormal{ln}(2) = 0.693\tau$$

**Mass Deficit**

```{math}
:label: massdeficit
\begin{equation}
Q = M(A,Z)^{2}c^{2} - [M(A-X,Z-Y)c^{2} + M(X,Y)c^{2}] > 0 
\end{equation}
```

**Q Value Beta- Decay**

```{math}
:label: betamqvalue
\begin{equation}
Q_{\beta^{-}} = [ M(A,Z) - M(A,Z-1) ]c^{2}
\end{equation}
```

**Q Value Beta+ Decay or EC**

```{math}
:label: betapqvalue
\begin{equation}
Q_{\beta^{+}} = [ M(A,Z) - M(A,Z-1) - 2m_{e}]c^{2}
\end{equation}
```

**Lambda and Matrix Element**

```{math}
:label: lambdacalc
\begin{equation}
\lambda = \frac{2\pi}{\hbar} ~| M_{if} |^{2} ~\frac{dn_{f}}{dE_{f}}
\end{equation}
```

```{math}
:label: matrixelement
\begin{equation}
|M_{fi}| = \int \psi^{*} \hat{H} \psi dV.
\end{equation}
```

**Beta Flux**

```{math}
:label: densityfinal
\begin{equation}
N(p) = \frac{C}{c^{2}} p^{2} (Q-T_{e})^{2}
\end{equation}
```


**Beta Superallowed Transition**

$$
 \Delta I = 0, \quad \Delta \pi = \textnormal{none}
 $$

**Beta Allowed Transition**

$$
 \Delta I = 0 \text{ or } \pm 1, \quad \Delta \pi = \textnormal{none}
 $$
 except for $0 \rightarrow 0$ transitions, which are forbidden.

**Beta Forbidden Transitions**

$$
 \Delta I = 0, \pm 1, \pm 2, \quad \Delta \pi = 1 
 $$
 
except for $0 \rightarrow 0$ transitions, which are still completely forbidden.

In general, the "n-th forbidden" transition is characterized by:

$$
 \Delta I = n, n \pm 1, n \pm 2, ..., \quad \Delta \pi = (-1)^{n}
 $$
 


**Alpha Decay Geiger Nutall**

$$
\log_{10} t_{1/2} = b_{1} \frac{Z}{Q^{1/2}} + b_{2}
$$

or

$$
\ln\lambda = -a_{1} \frac{Z}{Q^{1/2}} + a_2
$$


**Alpha Tunnelling Transmission Probability**

```{math}
:label: transmissionprob
\begin{equation}
X = Ae^{-αL}
\end{equation}
```



**Breit Wigner Form**
```{math}
:label: cross_section_compound
\begin{equation}
 \sigma_{(a,b)}B = \sigma_{a+A→C*} \times BR(C* → B + b), 
\end{equation}
```

**Breit Wigner Form**
```{math}
:label: breit-wigner
\begin{equation}
 \sigma_{BW}(E) = \frac{\pi}{(k)^2} \frac{(2J + 1)}{(2I_a + 1)(2I_A + 1)} \frac{\Gamma_a(E)\Gamma_b(E)}{(E - E_R)^2 + \Gamma(E)^2/4}, 
\end{equation}
```

**Compound Branching Ratio**
```{math}
:label: branching_ratio
\begin{equation} BR(C* \rightarrow b + B) = \frac{\Gamma_b}{\Gamma}.
\end{equation}
```

**Difference in timescales**
- Direct reactions are fast $(\sim10^{-22}~\textnormal{s})$ 
- Compound-nucleus reactions are slower ($~10^{-18} - 10^{-16} s$) 