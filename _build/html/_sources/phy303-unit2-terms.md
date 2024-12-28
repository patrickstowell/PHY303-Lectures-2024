## Unit 2 : Equations & Terms

### Equations
To aid with exam revision below is a list of all equations that you should learn for this unit in the course.

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
- $a$ is the "edge" of the nucleus defining the width of the top-hat.
- $d$ is the so-called Skin or Surface Thickness.



**Typical Values For the charge density distribution**
```{math}
:label: chargedist
\begin{equation}
\rho_{\textnormal{charge}}^{0} = \frac{\rho^0_{\textnormal{charge}}}{1+\textnormal{exp}[\frac{r-a}{d}]}
\end{equation}
```

- $a = 1.07 A^{1/3} ~\textnormal{fm}~~\textnormal{(radius)}$ 
- $d = 0.54~\textnormal{fm}~\textnormal{ (skin thickness)}$ 
- $\rho^{0} = 0.06-0.08~e~\textnormal{fm}^{-3}~\textnormal{ (average charge density)}$
- Note: We expect $\rho^{0}$ to be lower for heavy nuclei as $Z$ tends away from $N$.


**Typical Values For the mass density distribution**
```{math}
:label: massdist
\begin{equation}
\rho_{\textnormal{mass}}(r) = \frac{\rho^0_{\textnormal{mass}}}{1+\textnormal{exp}[\frac{r-a}{d}]}
\end{equation}
```

- $a = 1.2 A^{1/3} ~\textnormal{fm}~~\textnormal{(radius)}$ 
- $d = 0.75~\textnormal{fm}~\textnormal{ (skin thickness)}$ 
- $\rho^{0} = 0.17~e~\textnormal{fm}^{-3}~\textnormal{ (average charge density)}$


**Liquid Drop Model Binding Energy Estimate**
```{math}
:label: simpledropcombined_extraterms
\begin{equation}
B(A,Z) = a_{v}A - a_{s}A^{2/3} - a_{c}Z(Z-1)A^{-1/3} - \left[a_a(A-2Z)^{2}A^{-1}\right]_{\textnormal{assym}}- \delta_{\textnormal{pair}}
\end{equation}
```
- $a_{v} = 15.5 \textnormal{MeV}$, 
- $a_{s} = 16.8 \textnormal{MeV}$, 
- $a_{c} = 0.72 \textnormal{MeV}$, 
- $a_{a} = 23.0 \textnormal{MeV}$, 
- $a_{p} = 12.0 \textnormal{MeV}$.

**Liquid Drop Model Binding Energy Estimate per Nucleon**
```{math}
:label: simpledropcombined_totalequationperA
\begin{align}
B(A,Z)/A = a_{v} - a_{s}A^{-1/3} - a_{c} Z(Z-1) A^{-4/3} - a_{a}(A-2Z)^{2}A^{-2} + \delta A^{-1}
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

**Coulomb Final Term**
```{math}
:label: simpledropmodel_coloumbfinaltermquantised
\begin{equation}
B_{C} = -a_{C} \frac{Z(Z-1)}{A^{1/3}}
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

