(unit10:problems)=
# Unit 10 : Worked Problems

## Unworked Example: Brachytherapy for Lung Cancer

A clinical trial found that $ ^{125}I $ brachytherapy was more effective than conventional radiotherapy for treating inoperable lung cancer. $ ^{125}I $ decays by electron capture with a half-life of 59.4 days, emitting a 35.5 keV X-ray. 

Given that:
- Mean tumor volume = 312.7 cm³
- Mean radiation dose = 141.6 Gy
- Mean density of the human body = 985 g/cm³

Determine:
1. The average mass of $ ^{125}I $ implanted.
2. The activity of $ ^{125}I $ at the time of implantation.

State any assumptions made in the calculations.


## Worked Example : Medical Radioisotopes
A $ ^{99}Mo $ generator for $ ^{99m}Tc $ initially has an activity of 20 GBq and contains no $ ^{99m}Tc $. Technetium is extracted from the generator 24 hours after production, and again 24 hours after that. Assuming that the extraction is 100% efficient (an exaggeration, but not too much of one—the specification says >90%), what are the activities of the two technetium extractions?

The half-life of $ ^{99}Mo $ is 66.0 hours, and that of $ ^{99m}Tc $ is 6.0 hours. The branching ratio of the decay from $ ^{99}Mo $ to $ ^{99m}Tc $ is 86.8% (the remaining 13.2% of the time it decays directly to $ ^{99}Tc $).

---
```{admonition} Solution
:class: note, dropdown

For the $ ^{99}Mo $, we know that:
$$
N_{Mo}(t) = N_{Mo,0} e^{-\lambda_{Mo} t},
$$
where $ \lambda = \ln(2)/t_{1/2} $. The activity is therefore:
$$
A_{Mo}(t) = -\frac{dN_{Mo}}{dt} = \lambda_{Mo} N_{Mo,0} e^{-\lambda_{Mo} t} = \lambda_{Mo} N_{Mo}(t).
$$

For the $ ^{99m}Tc $, we must account for the atoms gained by the decay of $ ^{99}Mo $, and those lost by the decay of $ ^{99m}Tc $. Therefore:
$$
\frac{dN_{Tc}}{dt} = f \lambda_{Mo} N_{Mo} - \lambda_{Tc} N_{Tc},
$$
where $ f = 0.868 $ is the branching ratio to $ ^{99m}Tc $. Rearranging:
$$
\frac{dN_{Tc}}{dt} + \lambda_{Tc} N_{Tc} = f \lambda_{Mo} N_{Mo}.
$$

This is a standard form, which can be solved using an integrating factor $ F(t) $:
$$
F(t) = e^{\lambda_{Tc} t}.
$$

After solving and substituting, the activity of $ ^{99m}Tc $ is given by:
$$
A_{Tc}(t) = \frac{f \lambda_{Tc} A_{Mo,0}}{\lambda_{Tc} - \lambda_{Mo}} \left( e^{-\lambda_{Mo} t} - e^{-\lambda_{Tc} t} \right).
$$

Using the given data:
- $ \lambda_{Tc} = \ln(2) / 6.0 = 0.1155 \, \text{hr}^{-1} $,
- $ \lambda_{Mo} = \ln(2) / 66.0 = 0.0105 \, \text{hr}^{-1} $.

For $ t = 24 \, \text{hr} $:
$$
A_{Tc}(24 \, \text{hr}) = \frac{0.868 \times 0.1155 \times 20}{0.1155 - 0.0105} \left( e^{-0.0105 \times 24} - e^{-0.1155 \times 24} \right) = 14 \, \text{GBq}.
$$

For $ t = 48 \, \text{hr} $, reset the clock at the previous extraction:
$$
A_{Mo} = 20 \times e^{-0.0105 \times 24} = 15.5 \, \text{GBq}.
$$
Replacing $ 20 $ with $ 15.5 $ in the equation gives:
$$
A_{Tc}(48 \, \text{hr}) = 11 \, \text{GBq}.
$$

```


## Problems

1. **Calculate the Q-value for the reaction $ ^{14}N(p, \alpha)^{11}C $ used to produce the PET isotope $ ^{11}C $. Consulting the JANIS database, we see that the threshold for this reaction is approximately 4 MeV proton kinetic energy. Is this what you would expect? Briefly justify your answer.**

2. **Calculate the Q-value for the reaction $ ^{88}Sr(n, \gamma)^{89}Sr $ used to produce the therapeutic isotope $ ^{89}Sr $. Is it possible to produce this isotope using thermal neutron capture? If so, what is the expected photon energy?**

3. **The recommended dose of $ ^{131}I $ for treatment of hyperthyroidism is 550 MBq. If this is administered in the form of Na$ ^{131}I $, what mass of Na$ ^{131}I $ should the patient be given?**
   - *The half-life of $ ^{131}I $ is 8.0 days. The mean atomic mass of sodium is 23.0 u.*

---

## Workd Example : Gamma Cameras

The collimator in a gamma camera typically consists of a lead sheet of thickness $ l $, with holes of diameter $ d $ separated by “septa” of thickness $ t $:

- **a.** What is the resolution of the camera, expressed in terms of $ l $, $ d $, and $ z $, where $ z $ is the distance between the object and the front of the collimator?
- **b.** A particular collimator has $ d = 1.40 \, \text{mm} $, $ t = 0.18 \, \text{mm} $, and $ l = 24.7 \, \text{mm} $. If used to image a tumor at $ z = 40 \, \text{cm} $, calculate its resolution and efficiency.

---

```{admonition} Solution
:class: note, dropdown

The maximum angle accepted by the collimator is:
$$
\theta \approx \frac{d}{l}.
$$

At a distance $ z $, the resolution at the object is:
$$
\Delta x = \theta (l + z) = \frac{d (l + z)}{l}.
$$

For the given dimensions:
$$
\Delta x = 30.9 \, \text{mm}.
$$

Efficiency is given by:
$$
\eta \approx \frac{d^4}{12 l^2 (d + t)^2}.
$$

Substituting:
$$
\eta = 2.1 \times 10^{-4}.
$$

```

---


## Unworked Problem : Cardiac Collimation
Calculate the efficiency and resolution for the "Cardiac High Resolution" collimator ($ d = 2.03 \, \text{mm} $, $ t = 0.15 \, \text{mm} $, $ l = 48 \, \text{mm} $).

## Unworked Problem : Collimator Shielding
For $ ^{99m}Tc $ gamma rays in soft tissue ($ a = 0.15 \, \text{cm}^{-1} $), what fraction of $ \gamma $-rays will be observed for a tumor at $ x = 4 \, \text{cm} $ and a collimator half-angle of $ 0.18 \, \text{radians} $? Assume efficiency $ \eta = 2.1 \times 10^{-4} $.

## Unworked Problem : COllimated Gamma Count Rates
Cardiac perfusion imaging typically uses $ 550-1100 \, \text{MBq} $ of $ ^{99m}Tc $. What is the count rate observed with the "Cardiac High Resolution" collimator? State any assumptions.
