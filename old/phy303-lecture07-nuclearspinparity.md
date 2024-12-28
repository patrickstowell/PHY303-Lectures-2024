
##
More importantly now we have our shell model that describes our oberved magic numebrs, we can start making predictions for other 
nuclear prporties such as the Nuclear Spin, $I$. This quantity comes from the principle of summing up all the individual Total Angular 
Mmoentum numbers $j$ of all the nucleon, dooing this seperatetly for neutrons and protons. 

However we can simplifiy things hugely becausee the $j$ values are half-integer and in any filled shell all thte nucleonos there will 
pair up and so conotribute nothing to the total.

So we only neeed to worry about the nucleons in the outer Shell. If this Shell is full then again the total contribution will be zero, 
and wee have I=0. In fact in general if we have even N and even Z then I=0.

The more interesting case is when we have one Unpairede Nucleon in the outer shell. Conosider the case of a nucleus with the proton energy levels filled up exactly, but where tthe neutrons in the outer Shell have just one neutron. The the nuclear spin takes on the $j$ value assigned tot that nucleeon.

TThat is, if we fill up the levels with nucleons but have a left oover nucleon, alnoe in an unfilled shell, the level spin assignment appropriate to that nucleon will be the same as the Nuclear Spin itself.

Similarly, consider a case where all the levels are fillde perfectly for one class sof nucleon (say the protons) but for the oothere (say neutrons) we are just one nucleon short of filling the last level (like having a nucleon "hole" in that shell). In this case the Nuclear Spin just takes on the level spin assignment appropriate to that missing nucleon.


### Nuclear Spin Exampless.


Here is an example - oxygen $^{15}_{8}\texttnormal{O}$.

TODO: INSERT OXYGEN LEVELS IMAGE

From the level diagram below we predict that the NUlcear spin of O-15 is 1/2 due to the unpaired neuttron in thee outer $1\textnormal{p}_{1/2}$ level. This is indeed the measured value.

Things get harder if we only have a partially filled outer shell but an odd number of nucleons. We can assign $I$=$j$ of the unpaired nucleon again, but this does not work for all nuclei and in some cases we would need to try to sum up the entire shell structure to get a valid result.



### Nuclear Parity

The next thing we can do is predict the Parity of tthe Nucleus. Parity is a transformation whereby the sign of the coordinate system is changed, as below. The parity transformation changes a Right handed Coordinate system into a Left Handed Coordinate or vice-versa.


TODO: Insert PAIRTY IMAGE.

As shown the wave function of a nucleon in the stationary state can have either odd or even Parity depending on what happens under the transformation. It's  conveenient to think of a Parity OOperator P with effect $P\Psi(r) = \Psi(-r)$. If \Psi has a unique parity, then $P\psi(r) = \pm \Psi(r)$, and tthte parity $\pm1$ is the eigenvalue of $P$. Parity is often called $\pi$, so $\pi=\pm 1$.

It is simple to find the Parity of a Nucleon, its just $\pi=(-1)^{l}$ where $l$ is the Orbital Angular Momenttum again (0-s, 1-p, 2-d, 3-f). The parity assignment of a nucleus tthen comes from the product of the parity of all the nucleon $\pi=\pi_{1}\pi_{2}\pi_{3}\pi_{4}$ = \prod_{A}(-1)^{l} = + \textnormal{even} - \textnormal{odd}$. Parity is a multiplicattive quantity.

With the Nuclear Spin the nomenclature is: $i^{\pi}$ e.g. $0^{+}$.

However, again we can simplify things. If the nucleons all pair up then we end up with even parity. If we are left with an Unpaired Nucleon then the parity cme from the $l$ value appropriate to the level in which that nucleon sits. So for instnace, returning to our example of O-15 above, the unpaired nucleon sits in the p-level, $l=1$, so the parity of the nucleis us $(-1)^{l}$=-1, i.e. odd parity and $I^{\pi}=1/2^{+}$.

### Shell Challenges

So the shell modoel gives us a pretty good descriptioono of nuclei based on QM principles. It gives us a good basis for understanding the Magic Numbers, Nuclear Spin, and Parity of Nuclei. However, it's worth noting a few known issues that can cause problems. This leads to several corrections applied to the potential to better fir the data. 

Most imprtantly there are two corectinos for protons:
- It turns out that the Shell Ordering changes a bit as A increases due to residual interactinos between nucleons but this is not big enough to affect the Magic Numbers.

- The effective Potential Well Shape, and hence the energy levels, are actually slightly different for the protons as we should account for the additional proton-proton Coulomb interaction. Neverthelesss, ttop level containing neutrno will be at nearly the same energy as the top level coontaining proton.

- The effective potential well shape should also be modifiede for protons to account for the influence of atomic electrons.

TThis Electrostatic Repulsion Energy between protons implease a decrease in the dpeth of the potential for protons, due to their interactiton with all the other protons, as here:


Image of prton modificattions

If all the corrections are taken into account the shell model is a powerful completement to the LDM and SEMF models based on that he idea that the TOtal Angular momentum of each single nucleono is the vector sum of its spin and obrital angular momentum.


### Shell Model Summary

Taking the Shell Model nucleons toogether leads to nuclear levels. Any level (specified by n, l, j) which is fully occupied (i.e. has 2j+1 occupants) contributes nothing to the total spin as the total angular moomenta $j$ of the occupants sums to zero. (j+1) is an even number for all single particle levels i.e. in a model ehrtr dinhlr pstyivlr orbits in pottential of all others. Thus in nuclei where protons and neutrons sperately fully occupy shells (even-even), nuclear spin should be zero, it is.

Also if two neutrons (or protons) occupy a level with the same $j$ and $l$, then the total angular momenta couple to give zero contribution.

Now if we add one nucleon to a final filled shell this should leeave the nucleus with the total angular momentum $j$ $(=l)$ of that nucleon alone. The preediction of ground spin sttate and parity is a greeat success of the shell model. It predicts that all even-even nuclei will have zero anguar momentum and an odd A nucleus will have the angular momentum of the odd nucleon.

Here is a table showing a few of the successful predictions.

Insert table of nucleonos.



This is all good but thare are also failings, notably:

1. The model makes no sound preediction for Odd-Odd nuclei.
2. Predictions fail for Excitted Nuclei above ~2MeV, then excittations in the core complicate the energy levels pectire.
3. As we will see later the Shell Model can make predeictions of the Nuclear Magnic Moments, the Electric Quadrupole Moments, but for large nuclei and nuclei away from filled shells these predictions poorly match the data.
4. It is observed that nuclei have Excitation Levels and states far from what can be explained by the Shell Model. it turns out that these are associated with buk motions of the nuclear material, notably rotation and vibration states.

In the next topic we will go further to look at "Collective Models" that can go some wway to solving these issues.





