(unit10:problems)=
# Unit 10 : Worked Problems


## Worked Problem : Medical Radioisotopes
A $ ^{99}Mo $ generator for $ ^{99m}Tc $ initially has an activity of 20 GBq and contains no $ ^{99m}Tc $. Technetium is extracted from the generator 24 hours after production, and again 24 hours after that. Assuming that the extraction is 100% efficient (an exaggeration, but not too much of one—the specification says >90%), what are the activities of the two technetium extractions?

The half-life of $ ^{99}Mo $ is 66.0 hours, and that of $ ^{99m}Tc $ is 6.0 hours. The branching ratio of the decay from $ ^{99}Mo $ to $ ^{99m}Tc $ is 86.8% (the remaining 13.2% of the time it decays directly to $ ^{99}Tc $).

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


## Worked Problem : Gamma Cameras

The collimator in a gamma camera typically consists of a lead sheet of thickness $ l $, with holes of diameter $ d $ separated by “septa” of thickness $ t $:

- **a.** What is the resolution of the camera, expressed in terms of $ l $, $ d $, and $ z $, where $ z $ is the distance between the object and the front of the collimator?
- **b.** A particular collimator has $ d = 1.40 \, \text{mm} $, $ t = 0.18 \, \text{mm} $, and $ l = 24.7 \, \text{mm} $. If used to image a tumor at $ z = 40 \, \text{cm} $, calculate its resolution and efficiency.

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
