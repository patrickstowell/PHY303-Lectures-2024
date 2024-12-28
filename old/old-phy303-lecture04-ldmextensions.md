# Lecture 4 : Improving the Liquid Drop Model

The basic LDM model as stated so far is pretty good but still does not fit the full average binding energy curve very well.

A clue to how to fix this comes froom the other important plot shown earlier, the Chart of Known Nuclei. 

On a quick look we find two important features:
- The mosot stable nuclei lie roughly on a line where N=Z, nuclei that deviate from this tend to be less stable, (ii) nucei for which the Z and/or N are an even number tend to be more stable.
- Anything that tends to make nuclei less stable, implying the nucleons are less well bound together, is equivalent to lowering the average B/A value - *we need to account for this*

To do this we introduce two further terms, the **Asymmetry Term** and the **Pairing Term** as follows:

$$
B(A,Z) = a_{V}A - a_{s}A^{2/3} - a_{c}Z^{2}A^{-1/3} - a_a(A-2Z)^{2}A^{-1} - \delta_{\textnormal{pair}}
$$

At this stage we can regard both these new terms as arising empirically by observation from the data. Though you might guess that the physics origin comes from treating the nucleus using Quantum Mechanics.

Not the negative terms - e.g. the more N deviates from the quality with Z, the more negative is the Asymmetry Term and the weaker bound is the nucleus (lower B/A).


## 4.1 Nucleon Pairing

Although we can regard the Asymmetry and Pairing Terms as empirical, just an observation that fits the data, we can explain their form better by starting to introduce some Quantum Mechanics (QM). This will lead us later to an improved model of the Nucleus, the Shell Model.

Both protons and neutrons are Fermions, i.e. they have Assymetric Wave Functionos and spin =1/2. Thus they obey the Pauli Exclusion Principle. So we would expect that only two protons (or two neutrons) can occupy a given energy state, one with Spin-up the other Spin-down.

In fact the coupling of these spins means it is enegetically favourable to have pairs of neutrons or pairs of protons, rather than an odd neutron or proton alone in a given level.

Here each line corresponds to a new energy level that the protons or neutrons can occupy when the states below them are filled.

TODO : Image protons Levels.

From this nbiave view we might expect that the neutrons and protons in a nucleus might best pile into energy levels in pairs as below. This being the most stable configuration. 

Even numbers of protons and even numbers of neutrons would therefore yield the largest positive contribution to the binding energy. This is referred to as an Even-Even conofiguration.

If however, we have a single left over proton, or a single left over neutron, we end up with only one partially filled energy level on the neutron or proton side. This is referred to as an Odd-Even state and as a result the nucleus is less bound and it is a state of intermediate stability.

Finally we can consider states where both an odd proton and an odd neutron is left. These are referred to as Odd-Odd states. Because they are the least stable they are very rare in nature.

So how nucleons pair up is important in the binding energy and dictates the $\delta_{pair}$ term. 

$$
\delta_{\textnormal{pair}} = +a_{p}A^{-1/2} ~~~~\textnormal{for~~~~ N odd and Z odd}\\
\delta_{\textnormal{pair}} = 0 ~~~~\textnormal{for~~~~ N even and Z even} \\
\delta_{\textnormal{pair}} = -a_{p}A^{-1/2} ~~~~\textnormal{for~~~~ N even and Z even}\\
$$

Note the negative term in the binding energy equation that cancels out the negative term in the Even-Even case to produce an increase in binding energy overall (the nucleus is more stable).




## 4.3 Nucleon Assymetry



## 4.4 Total Binding Energy Equation



## 4.5 Worked Example



## 4.6 SEMF and Binding Energy Conclusions