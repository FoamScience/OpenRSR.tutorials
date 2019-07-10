// -*- C++ -*-
// File generated by PyFoam - sorry for the ugliness

FoamFile
{
 version 2.0;
 format ascii;
 class volScalarField;
 location "0";
 object oil.mu;
}

dimensions [ 1 -1 -1 0 0 0 0 ];

internalField uniform 0.001;

boundaryField
{
  outlet
  {
    type zeroGradient;
  }
  inlet
  {
    type zeroGradient;
  }
  frontAndBack
  {
    type empty;
  }
  topAndBottom
  {
    type zeroGradient;
  }
} 	// ************************************************************************* //

