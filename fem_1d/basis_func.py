import numpy as np

def localBasis(Nelem, xcoord, elem):
    # Calculate for each element the local basis linear functions

    # phi = ax + b
    # for each element "iel"
    # BasisCoefA(0,iel) contatins a for basis function related to local node 1
    # BasisCoefB(0,iel) contains b for basis function related to local node 1
    # BasisCoefA(1,iel) contatins a for basis function related to local node 2
    # BasisCoefB(1,iel) contains b for basis function related to local node 2

    BasisCoeffA = np.zeros((2, Nelem))
    # BasisCoeffB = np.zeros((2, Nelem)) # not needed now because PDE is only derivatives

    for iel in range(0, Nelem): # loop over all elements
        globnod1 = elem[0, iel]
        globnod2 = elem[1, iel]
        BasisCoeffA[0, iel] = -1/(xcoord[globnod2 - 1] - xcoord[globnod1 - 1])
        BasisCoeffA[1, iel] = 1/(xcoord[globnod2 - 1] - xcoord[globnod1 - 1])

    return BasisCoeffA