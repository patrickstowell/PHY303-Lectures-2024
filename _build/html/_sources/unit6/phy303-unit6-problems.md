(unit6:problems)=
# Unit 6 : Worked Problems

(unit6:problem:example1)=
#### Example 6.1.1 : Alpha decay separation energy
Calculate the separation energy for the alpha decay of $^{238}$U.

```{admonition} Solution
:class: note, dropdown

For $\rm ^{238}U \rightarrow ^{234}Th + \alpha$, the separation energy is given by:

$$
Q = m(238,92) - m(234,90) - m(4,2),
$$  
where m is the nuclear or atomic mass (interchangeable in this calculation since the mass of the electrons cancels out in the atomic mass).

So 

$$
Q = ( 238.050788 ~\textnormal{u} - 234.04359 ~\textnormal{u} - 4.002603~\textnormal{u} ) \times 931.5~\textnormal{MeV~u}^{-1} = 4.28~\textnormal{MeV}
$$
```

(unit6:problem:example2)=
#### Example 6.1.2 : Nuclear separation distance in alpha decay
Using the separation energy calculated in 6.1.1, calculate the nuclear separation distance of the $\alpha$ and $^{234}$Th daughter nucleus.

```{admonition} Solution
:class: note, dropdown

Nuclear separation $\rm R = r_0 (A_{\alpha}^{1/3}+A_d^{1/3})$ where $A_{\alpha}$ and $\rm A_d$ are the atomic masses of the alpha and daughter nucleus respectively, and $\rm r_0 = 1.2$ is a constant of proportionality. Therefore:

$$ 
R = 1.2(4^{1/3}+234^{1/3}) = 9.30~ \textnormal{fm}
$$
```

(unit6:problem:example3)=
#### Example 6.1.3 : Height of the Coulomb barrier to alpha decay
Calculate the height of the Coulomb barrier to the alpha decay of $\rm ^{238}U$ at the nuclear separation distance R calculated in 6.1.2.

```{admonition} Solution
:class: note, dropdown

The height of the barrier at nuclear separation distance R is calculated as the Coulomb potential of point charges Z$_{\alpha}$e and Z$_d$e, where Z$_\alpha$ and Z$_d$ are the atomic numbers of the alpha particle and daughter nucleus. The height of the barrier is therefore:

$$
\begin{align*}
V(R) &= \frac{2Z_dke^2}{R} \\
     &= \frac{2(90)1.44~\textnormal{MeV~fm}}{9.30~\textnormal{fm}} \\
     &= 27.9~\textnormal{MeV},
\end{align*}
$$ 
where $ke^2=\frac{e^2}{4\pi\epsilon_0}$.
```

(unit6:problem:example4)=
#### Example 6.1.4 : Outer extent of the Coulomb barrier to alpha decay
Calculate the distance at which the Coulomb potential drops to the energy of the $\alpha$ particle and, from this, the width of the Coulomb barrier in the alpha decay of $^{238}$U using your answers from earlier steps.

```{admonition} Solution
:class: note, dropdown

The energy of the alpha particle is $T_e \approx Q = 4.28~\textnormal{MeV}$ (from Example 6.1.1). The distance at which the Coulomb potential R$_Q$ is equal to Q is given by rearranging the equation for the Coulomb potential:

$$
R_Q = \frac{2Z_dke^2}{Q} = \frac{2(90)1.44~\textnormal{MeV~fm}}{4.28~\textnormal{MeV}} = 60.6~\textnormal{fm}
$$

The width of the Coulomb barrier is therefore $w = R_Q - R = 60.6~\textnormal{fm} - 9.30~\textnormal{fm} = 51.3~ \textnormal{fm} $. 
```

(unit6:problem:example5)=
#### Example 6.1.5 : Alpha-Coulomb barrier collision frequency
Now find the frequency at which the $\alpha$ particle collides with the Coulomb barrier in the alpha decay of $^{238}$U using your earlier answers.

```{admonition} Solution
:class: note, dropdown

Since the alpha particle at this energy is non-relativistic, the velocity of the alpha can be calculated from its kinetic energy $T_e \approx Q = 4.28~\textnormal{MeV}$:

$$
\begin{align*}
T_e &= \frac{mv^2}{2} \approx Q\\
\textnormal{Therefore}\\
\frac{v}{c} &= sqrt{\frac{2Q}{m}} \\
            &= sqrt{\frac{2(4.28)}{4.002603~u (931.5 \textnormal{MeV u}^{-1})}} \\
            &= 0.0479~\textnormal{m~s}^{-1}c^{-1}\\
\textnormal{and}\\
v &= 1.44 \times 10^7~\textnormal{m~s}^{-1} 
\end{align*}
$$

The frequency of collisions of an alpha particle with this velocity is given by:

$$
\begin{align*}
f &= \frac{v}{2R} \\
  &= \frac{1.88 \times 10^6~\textnormal{m~s}^{-1}}{2(9.30~\textnormal{fm})(10^{-15}~\textnormal{m~fm}^{-1}} \\
  &= 0.772 \times 10^{21}~\textnormal{s}{-1}
\end{align*}
$$
```

(unit6:problem:example6)=
#### Example 6.1.6 : Alpha tunnelling probability
Now calculate the tunnelling probability of the alpha particle in the decay of $^{238}$U by integrating over the Gamow factor.

```{admonition} Solution
:class: note, dropdown

The tunnelling probability is given by $P = e^{-2G}$, where G is the Gamow factor:

$$
G = \sqrt{\frac{2m}{\hbar^2}}\int_R^{R_Q} \sqrt{V(r) - Q}~dr
$$

Evaluating this integral gives us:

$$
G = \sqrt{\frac{2m}{\hbar^2Q}}2Z_d ke^2[arccos\sqrt{x}-\sqrt{x(1-x)}]
$$
where $x = R/R_Q = Q/V(R)$.

Putting in the numbers, this gives a tunnelling probability of

$$
P = e^{-2G} = 0.352 \times 10^{-38}
$$
```

(unit6:problem:example7)=
#### Example 6.1.7 : Alpha decay constant and half life
Assuming that the preformation probability $P_\alpha$ of the alpha particle is equal to 1, calculate the decay constant, and therefore half-life of $^{238}$U.

```{admonition} Solution
:class: note, dropdown

The decay constant is given by:

$$
\lambda = fP_\alpha P = f P = 2.72 \times 10^{-18}
$$

And so the half-life of $^{238}$U is

$$
\begin{align*}
T_{1/2} &= \frac{ln(2)}{\lambda} \\
        &= 2.55 \times 10^{17}~\textnormal{s} \\
        &= 8.07 \times 10^9~\textnormal{years}
\end{align*}
$$

```

(unit6:problem:example8)=
#### Example 6.1.8 : Differences between calcualated and measured half-life
The measured half-life of $^{238}$U is approximately $4.468 \times 10^9$ years. Comment on the difference between this value and the half-life we have calculated.

```{admonition} Solution
:class: note, dropdown

The half-life calculated assumed a spherical nucleus and does not take into consideration:
1. The non-spherical nature of heavy nuclei.
2. The effects of nuclear angular momentum.

A 4% change in radius can give a factor of 5 difference in half-life, and in fact the measured half-life can be used to infer information about the radius.
```

(unit6:problem:example9)=
#### Example 6.2.1 : Beta decay selection rules
Use the beta decay selection rules to classify the following transitions:

1. $^{76}$Br(1-) to $^{76}$Se(0+)

    ```{admonition} Solution
    $\Delta \pi = -$, so L is odd, since $\Delta \pi = (-1)^L$.
    
    Since $\Delta J = L + S = 1$, and L is odd, L = 1 and S = 0 is the only possible combination. 
    
    This transition is therefore a 1st forbidden Fermi decay.
    ```

2. $^{22}$Na(3+) to $^{22}$Na(0+)

    ```{admonition} Solution
    There is no change in parity and $\Delta \pi = +$, so L is even and can be 0, 2, etc.

    $\Delta J = L + S = 3$, so L = 2 and S = 1.

    This transition is therefore a 2nd forbidden Gamow-Teller decay.
    ````

3. $^{40}$K(4-) to $^{40}$Ca(0+)

    ```{admonition} Solution
    There is a change in parity and $\Delta \pi = -$, so L is odd.

    $\Delta J = L + S = 4$, so L = 3 and S = 1.

    Therefore this is a 3rd forbidden Gamow-Teller decay
    
    ```

(unit6:problem:example10)=
#### Example 6.2.2 : Beta decay endpoint value

Calculate the endpoint value for the decay of $^{81}$Kr by beta minus, beta plus and electron capture, and therefore demonstrate which form of beta decay the isotope undergoes.

```{admonition} Solution

1. Beta minus decay $ ^{81}_{36}Kr \rightarrow ^{81}_{37}Rb + \beta^- + \bar{\nu}_e$:

$$
Q = M_{Kr} - M_{Rb} - m_e = 80.916593~\textnormal{u} - 80.918994~\textnormal{u} - 5.4858 \times 10^{-4}~\textnormal{u} < 0
$$

2. Beta plus decay $ ^{81}_{36}Kr \rightarrow ^{81}_{35}Br + \beta^+ + \nu_e$:

$$
Q = M_{Kr} - M_{Br} - 2m_e = 80.916593~\textnormal{u} - 80.916291~\textnormal{u} - 2(5.4858) \times 10^{-4}~\textnormal{u} < 0
$$

3. Electron capture $ ^{81}_{36}Kr + e^- \rightarrow ^{81}_{35}Br + \nu_e$

$$
Q = M_{Kr} - M_{Br} = 80.916593~\textnormal{u} - 80.916291~\textnormal{u} = 0.281~\textnormal{MeV}
$$

Therefore, electron capture is the only form of beta decay that $^{81}$Kr can undergo.


