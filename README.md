# Tutorial cases For OpenRSR

These tutorials are documented in this repo's wiki pages.
Mainly, they verify the integrity of developed solvers:

 - `BL-Case.*`: Some 1D Buckley-Leverett scenarios to verify 
   basic functionality of `pSwImpesFoam` and `pSwCoupledFoam` solvers.
 - `SPE10` related cases to compare results obtained with `pSwCoupledFoam`
   against original SPE10 publication and a reference MUFITS simulation (
   available as an example at its webpage).
 - `A reduced realistic reservoir` to test the anisotropic version of the 
   coupled solver.


## Known Problems & workarounds

Parallel running of cases is not yet comfortable:

- OpenFOAM creates a local mesh per processor and solves equations there. Calculations
  in regions with no wells are usually much faster,but BCs are applying blocking MPI calls
  everywhere. 
- Setting Reference Pressure cell in global `system/fvSolution` should be avoided as the
  local cell ID will change.
- Well cell set in `constant/wellProperties` shouldn't use `labelToCell` topoSets
  because those are relying on global cell labeling for now. It's better to use
  something like `cylinderToCell`.
- Cells of a single well should belong to the same processor, especially if conversion 
  of rate-imposed to BHP-operated wells is allowed.

In general, avoid parallelizing the cases until a concrete solution to these issues is
solved.
