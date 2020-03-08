# Tutorial cases For OpenRSR solvers

These tutorials are here to verify the integrity of developed solvers:

 - `BL-Case.*`: Some 1D Buckley-Leverett scenarios to verify 
   basic functionality of isotropic IMPES and coupled solvers.
 - `SPE10`-related cases to compare results obtained with coupled solvers
   against original SPE10 publication and a reference MUFITS simulation (
   available as an example at the software's webpage).
 - `A reduced realistic reservoir` to test the anisotropic version of the 
   coupled solver [coming soon].

> The ``dev`` branch of this repo is kept always in sync with the dev branch
> of [OpenRSR](https://github.com/FoamScience/OpenRSR) repo. Which means, changes (in case files) needed to be able
> to run the tutorials with the latest library/solvers (from the dev branch)
> will only be applied here on the dev branch.
