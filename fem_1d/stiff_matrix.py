import numpy as np

def stiffBuild(Nodes, Nelem, xcoord, elem, BasisCoeffA, Diff):
    # Build stiffness matrix from local elemental contributions
    # stiff_{ij} = \int Diff \phi'_i \phi'_j

    stiffMat = np.zeros((Nodes, Nodes))
    
    for iel in range(0, Nelem):
        area = xcoord[elem[1, iel] - 1] - xcoord[elem[0, iel] - 1]
        for iloc in range(0, 2):
            iglob = elem[iloc, iel]
            for jloc in range(0,2):
                jglob = elem[jloc, iel]
                localMat =  Diff[iel] * BasisCoeffA[iloc, iel] * BasisCoeffA[jloc, iel]
                stiffMat[iglob - 1, jglob - 1] = stiffMat[iglob - 1, jglob - 1] + area * localMat

    return stiffMat