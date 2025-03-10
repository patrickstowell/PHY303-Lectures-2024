(unit5:problems)=
# Unit 5 : Worked Problems

(unit5:problem:example1)=
#### Example 5.1 : Nuclear Deformation
If the $\beta$ parameter is estimated to be $\beta=-0.197$ for a deformed nucleus Co-57, estimate the intrinsic quadrupole moment. Is this a prolate or probate nucleus?
```{admonition} Solution
:class: note, dropdown

To estimate the intrinsic quadrupole moment we use the equation from the notes.

$$
Q_{0} = \frac{3}{\sqrt{5\pi}} R_{av}^{2} Z \beta (1+0.16\beta)
$$

To estimate the average nuclear radius first we use $\sqrt{\langle r^{2} \rangle} = 0.94 A^{1/3}$

$$
R_{av}^{2} = (0.94 (57^{1/3}))^{2} = 13.0869~\textnormal{fm}^{2}
$$

Subbing this in to our equation gets us


$$
Q_{0} = \frac{3}{\sqrt{5\pi}} 13.0869 \times 27 \times  (-0.197) (1+0.16(-0.197)) \textnormal{fm}^{2} = -51.029 \textnormal{fm}^{2} = -0.510 \textnormal{b}
$$

The mapping between intrinsic moment $Q_{0}$ and measured electric quadrupole moment ($Q_{EQM}$) is dependent on the angular momentum, but generally we find if one is negative the other is positive and vice-versa. For Co-57 the real measured $Q_{EQM}$ momentum is +0.52 b which agrees with  this.

Since $\beta$ is negative, we are expecting this to be a prolate nucleus.

``` 

(unit5:problem:example2)=
#### Example 5.2 : Excited States of Erbium

The lowest lying excited state of Erbium-164 is $E(2^{+}) = 91.4~\textnormal{keV}$. Where does this state come from? Based on this value estimate the energy levels of the higher $E(4^{+}), E(6^{+}), E(8^{+})$ states.

```{admonition} Solution
:class: note, dropdown

These levels come from rotational states that are only possible when we have a slightly deformed nucleus.

If we know the first state, we can estimate the value of the moment of intertia scaling.

$$
E_{J} = \frac{\hbar^{2}}{2I}J(J+1)~~~~~J=0,2,4,\ldots
$$

$$
E_{2} = \frac{\hbar^{2}}{2I}2(2+1) =   \frac{\hbar^{2}}{2I} \times 6 = 91.4~\textnormal{keV}
$$

$$
\frac{\hbar^{2}}{2I} 15.2~\textnormal{keV}
$$

We can then estimate the higher states using the same scaling

$$
E_{4} = 20 * 15.2 ~\textnormal{keV} = 304 ~\textnormal{keV}
$$

$$
E_{6} = 42 * 15.2 ~\textnormal{keV} = 638 ~\textnormal{keV}
$$

$$
E_{8} = 72 * 15.2 ~\textnormal{keV} = 1094 ~\textnormal{keV}
$$

``` 


(unit5:problem:example3)=
#### Example 5.3 : Gamma Ray Transitions

Determine whether the following transitions are allowed, stating their possible multipoles (E1, M1, etc), and which of them is the most likely.


```{admonition} Solution
:class: note, dropdown

$$
\frac{3}{2}^{+} \rightarrow \frac{5}{2}^{+}, ~~~~
\frac{3}{2}^{+} \rightarrow \frac{5}{2}^{-}, ~~~~
0^{+} \rightarrow 0^{+}, ~~~~
\frac{3}{2}^{-} \rightarrow \frac{1}{2}^{+}, ~~~~
$$

**Transition 1**

$$
\frac{3}{2}^{+} \rightarrow \frac{5}{2}^{+}
$$

To evaluate this first we need to look at the range of nuclear spins. We expect

$$
\left|\frac{3}{2} - \frac{5}{2}\right | \leq L \leq \left|\frac{3}{2} + \frac{5}{2}\right |
$$

So we know $L$ can be $1, 2, 3, 4$. We also know this has no change in parity $\Delta \pi = \textnormal{no}$.

The available transitions are therefore M1, E2, M3, E4. The M1 is the most likely.


**Transition 2**

$$
\frac{3}{2}^{+} \rightarrow \frac{5}{2}^{-}
$$

This is the same as above but now there is a change in parity $\Delta \pi = \textnormal{yes}$.

The available transitions are therefore flipped E1, M2, E3, M4. The E1 is the most likely. This is because an E1 transition is parity changing, whilst an M1 transition is not.

**Transition 3**

$$
0^{+} \rightarrow 0^{+}
$$

Again we need to look at the range of nuclear spins. We expect

$$
|0 - 0| \leq L \leq |0 + 0|
$$

The one exception we have for $L$ is we cannot have $L=0$, as the gamma needs to take away something, so this transition is not allowed at all.


**Transition 4**

$$
\frac{3}{2}^{-} \rightarrow \frac{1}{2}^{+}, ~~~~
$$

Again we need to look at the range of nuclear spins. We expect

$$
\left |\frac{1}{2} - \frac{3}{2}\right | \leq L \leq \left|\frac{3}{2} + \frac{1}{2}\right |
$$

So this time we expect $L$ to be either 1 or 2. 
We are parity changing so this means the available transitions are either E1, M2 in order of decreasing likelihood.

```