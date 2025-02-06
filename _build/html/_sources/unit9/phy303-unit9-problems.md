(unit9:problems)=
# Unit 9 : Worked Problems

(unit9:problem:example1)=
## Worked Example : AmBe Sources

**Calculate the energy of the $ \alpha $ particle emitted in the decay of $ ^{241}Am $. Hence calculate the total energy released when that $ \alpha $-particle collides with a stationary nucleus of $ ^{9}Be $. Compare this with the neutron energy spectrum in the notes, and comment.**

---

```{admonition} Solution
:class: note, dropdown


The $ \alpha $-decay is:
$$
^{241}_{95}Am \to ^{237}_{93}Np + ^{4}_{2}He
$$

Here we can actually use the atomic masses, because the electron masses will all cancel out, so we have (from Krane):
$$
Q = 241.056824 - (237.048168 + 4.002603) = 0.006053 \, u = 5.638 \, \text{MeV}.
$$

The beryllium reaction is $ ^{9}Be(\alpha,n)^{12}C $. The Q-value, again using atomic masses, is:
$$
Q = 9.012182 + 4.002603 - (12 + 1.008665) = 0.006120 \, u = 5.701 \, \text{MeV}.
$$

So the total kinetic energy in the final state is:
$$
5.638 + 5.701 = 11.339 \, \text{MeV}.
$$

If we compare this with the AmBe neutron energy spectrum from the notes, we see that the maximum neutron energy is a bit less than the total available (which is reasonable, as we need to allow for momentum conservation), but most emitted neutrons have smaller energies. There are several factors that contribute to this:
- The sharing of the total energy between the carbon nucleus and the neutron depends on the angle at which the neutron is emitted (relative to the original $ \alpha $-direction).
- Alpha particles have a very short range, so many $ \alpha $-particles will presumably have lost some energy by the time they encounter a $ ^{9}Be $ nucleus.
- Similarly, the neutrons may lose energy through scattering before they emerge from the AmBe source.
- The neutron emission may leave the $ ^{9}Be $ nucleus in an excited state rather than the ground state.

```

### Unworked Problem : Neutron Sources

The two common laboratory-scale (as opposed to national facility scale) neutron sources are AmBe (as discussed in the example) and d-t fusion generators. Compare and contrast these two source types.



### Unworked Problem : Reactor Spectra

There are two "reactor neutron" energy spectra shown in the lecture, one (from the IPEN/MB01 research reactor) on slide 7 and one (comparing reactor and spallation neutrons) on slide 8. They do not look the same. Both come from reputable sources, so we can reasonably assume that both are in some sense "right". What do you think causes the difference?


### Unworked Problem : 14 MeV Neutrons

Verify the statement in the notes that the energy of the neutrons emitted in the $ ^{3}H(d,n)^{4}He $ reaction is 14 MeV, stating any assumptions that you make.


## Worked Example : Uranium Fission
**Neutrons from uranium fission are emitted with typical energies of 2 MeV or so. In nuclear reactors, it is desirable to moderate these to thermal energies (0.025 eV), because thermal neutrons are much more efficient at inducing further fissions. If a reactor uses graphite ($ ^{12}C $) as a moderator, estimate how many times a neutron needs to scatter off a graphite nucleus in order to thermalize.**


```{admonition} Solution
:class: note, dropdown


This is elastic scattering, so $ Q = 0 $. We can assume non-relativistic speeds since $ K_n \ll m_n c^2 $ (where $ K_n $ is the initial neutron kinetic energy).

The easiest way to tackle this is to consider the centre-of-mass frame. The speed of the centre-of-mass frame is given by:
$$
V_{CM} = \frac{p_n}{m_n + M} = \frac{m_n v_n}{m_n + M},
$$
where $ M $ is the mass of the carbon nucleus, $ 12 - 6m_e = 11.996709 \, u $, and $ v_n $ is the initial speed of the neutron in the lab frame.

The initial speed of the neutron in the centre-of-mass frame is:
$$
u_n = v_n - V_{CM} = v_n \left( 1 - \frac{m_n}{m_n + M} \right) = v_n \frac{M}{m_n + M}.
$$

Since this is elastic scattering, in the CM frame the speeds do not change—only the direction does. The maximum kinetic energy the neutron could have is the same as its initial energy $ K_n $: this represents a glancing blow with negligible energy transfer. The minimum energy would be when the neutron scatters back along its initial path. In this case, the speed of the neutron in the lab frame is:
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

Therefore, we have, taking logs:
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

## Unworked Problem : Alternative Yield

Repeat the above calculation for (i) $ ^{1}H $, (ii) $ ^{2}H $, and (iii) $ ^{238}U $, and comment on your results.

---

## Unworked Problem : Excited States

In thermal neutron capture by $ ^{55}Mn $, the following $ \gamma $-ray energies (in MeV) are observed: 7.2703, 7.2438, 7.1597, 7.0578, 6.9287. Deduce the energies of the corresponding $ ^{56}Mn $ excited states.

---

## Unworked Problem : He3 Detectors

Helium-3 gas proportional chambers are widely used as thermal neutron detectors. The reaction is $ ^{3}He(n,p)^{3}H $. What is the Q-value of this reaction? Estimate the energy of the produced proton, stating any assumptions that you make.