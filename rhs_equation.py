import numpy as np

def forcing(Nodes, Nelem, xcoord, elem, ffunc):
    '''
    Using the trapezoidal rule for evaluating the integral (it is exact on linear functions)
    has a convergence error comptabile with linear P1 FEM
    Trapezoidal is used here exploiting the fact that in one of the nodes the phi is zero!! (only 1 term)
    '''
    rhs = np.zeros((Nodes, 1))

    for iel in range(0, Nelem):
        area = xcoord[elem[1, iel] - 1] - xcoord[elem[0, iel] - 1]
        for iloc in range(0,2):
            iglob = elem[iloc, iel]
            rhs[iglob - 1] = rhs[iglob - 1] + ffunc(xcoord[iglob - 1]) * area/2
    return rhs