# Finite element code for 1D piecewise linear Galerkin
# -(Diff u')'(x) = f(x) with Dirichlet BC

from input_data import input_data
from basis_func import localBasis
from stiff_matrix import stiffBuild
from rhs_equation import forcing
from boundary_cond import imposeBC
from error_evaluate import evalErr

import numpy as np

def run_1D():
    # End points
    a = 0
    b = 1

    # Number of elements
    Nelem = 40

    # Define the 1D mesh and equation BCs and coefficients
    Nodes, NDir, xcoord, elem, DirNod, DirVal, Diff, source, ureal = input_data(a, b, Nelem)

    # Define for each element the two basis functions \phi_i(x) = a_i x + b_i
    BasisCoeffA = localBasis(Nelem, xcoord, elem)

    # Build stiffness matrix (without BCs)
    stiffMat = stiffBuild(Nodes, Nelem, xcoord, elem, BasisCoeffA, Diff)

    #  build right-hand-side vector (withouy Dirichlet boundary conditions)
    rhs = forcing(Nodes, Nelem, xcoord, elem, source)

    # impose boundary conditions
    stiffMat, rhs = imposeBC(NDir, DirNod, DirVal, stiffMat, rhs)

    # solve the linear system
    uh = np.linalg.solve(stiffMat, rhs)

    # evaluate the error
    err = evalErr(Nelem, xcoord, elem, uh, ureal)

    return xcoord, uh, ureal, err