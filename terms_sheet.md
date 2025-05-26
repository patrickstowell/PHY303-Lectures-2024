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
\Delta M(A,Z) = M(A,Z) - (ZM_{p} + NM_{n}).
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

**SHELL MODEL NUMBER OF STATES**

$$
n_{\textnormal{states}} = (2j+1)
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
\frac{\mu}{\mu_N} = ((j+\frac{3}{2})g_l - \frac{1}{2}g_s)\frac{j}{j+1} \rightarrow (jackknife)
\end{equation}
```


**G Factors**
```{math}
:label: gyromagneticfactors
\begin{equation}
g_{s} = 5.85 ~~\textnormal{(proton)} ~~~~~~ g_{s} = -3.826 ~~\textnormal{(neutron)}
\end{equation}
```

```{math}
:label: gyromagneticfactors2
\begin{equation}
g_l = 1~~\textnormal{(proton)} ~~~~~~~ g_l = 0 ~~\textnormal{(neutron)}
\end{equation}
```

**Quadrupole Operations**

```{math}
:label: quadrupoleoperation
\begin{equation}
eQ_{EQM} = e\int \psi^{*} (3z^{2} - r^{2})\psi dV
\end{equation}
```

```{math}
:label: quadrupolecalculation
\begin{equation}
Q_{EQM,sp} = - < r^{2} > \frac{2j-1}{2(j+1)}
\end{equation}
```

```{math}
:label: quadrupoleunfilled
\begin{equation}
< Q_{EQM, \textnormal{unfilled}} > = < Q_{EQM,sp} > \left [ 1-2\frac{n-1}{2j-1} \right ]
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


**GAMMA RULES**

$$
| I_{f} - I_{i} | \leq L \leq|I_{f} + I_{i}|
$$

- Electric multipole radiation $\pi=(-1)^l$.
- Magnetic multipole radiation $\pi(-1)^{(l+1)}$.

**Half Life**

$$T_{1/2} = \tau \textnormal{ln}(2) = 0.693\tau$$

**Mass Deficit**

```{math}
:label: massdeficit
\begin{equation}
Q = M(A,Z)^{2}c^{2} - [M(A-X,Z-Y)c^{2} + M(X,Y)c^{2}] > 0 
\end{equation}
```

**Q Value Beta- Decay in AMU**

```{math}
:label: betamqvalue
\begin{equation}
Q_{\beta^{-}} = [ M(A,Z) - M(A,Z-1) ]c^{2}
\end{equation}
```

**Q Value Beta+ Decay or EC in AMU**

```{math}
:label: betapqvalue
\begin{equation}
Q_{\beta^{+}} = [ M(A,Z) - M(A,Z-1) - 2m_{e}]c^{2}
\end{equation}
```

**Lambda and Matrix Element Relation**

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

**Beta Flux Relation**

```{math}
:label: densityfinal
\begin{equation}
N(p) = \frac{C}{c^{2}} p^{2} (Q-T_{e})^{2}
\end{equation}
```


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

**Reaction Kinetic Energy Calculation**
```{math}
:label: scattering_kbcancellation
\begin{equation}
K_b^{1/2} = \frac{\cos \theta \sqrt{m_am_bK_a} \pm [m_am_bK_a \cos^2 \theta + (m_b + m_B)((m_B - m_a)K_a + m_BQ)]^{1/2}}{m_b + m_B} 
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


**Fission Requirement**

$$ 
2a_s A^{2/3}\leq a_{C} \frac{Z^2}{A^{1/3}} \quad \Rightarrow \quad \left(\frac{Z^2}{A}\right)_{\text{crit}} \geq \frac{2a_s}{a_c} \approx 49 
$$

**Fission Four Factor Formula**

$$
k=ηϵpf
$$


**Fusion Coulomb Barrier Limit**

$$
 \frac{Z_1Z_2e^2}{4\pi\epsilon_0(R_1 + R_2)} = 1.44 \frac{Z_1Z_2}{R_1 + R_2} \text{ MeV}, 
$$


**Fusion Reaction Rate**

$$ 
R_{12} = n_1 n_2 ⟨σv⟩. 
$$

**Fusion Maxwell Boltzmann**

$$
 P(v)dv = \sqrt{\frac{2}{\pi}} \left( \frac{m}{k_B T} \right)^{3/2} \exp\left( -\frac{mv^2}{2k_B T} \right) v^2 dv, 
 $$


**Fusion Lawson Criteria**

$$
L = \textnormal{energy output} / \textnormal{energy input}
$$


**Fusion Energy Out**

$$
E_{out} = n_d^2 ⟨σ_{dt}v⟩ Q t_c
$$
