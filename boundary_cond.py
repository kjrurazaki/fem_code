import numpy as np

def imposeBC(NDir, DirNod, DirVal, stiffMat, rhs):
    '''
    Impose Dirichlet BCs with the penalty method
    Impose Neumann BCs
    '''
    penalty = 1e+15

    for idir in range(0, NDir):
        iglob = DirNod[idir]
        stiffMat[iglob - 1, iglob - 1] = penalty
        rhs[iglob - 1] = penalty * DirVal[idir]

    # Impose Neumann BCs
    # for ineu in range(0, NNeu):
    #     iglob = NeuNod[ineu]
    #     rhs[iglob - 1] = rhs[iglob - 1] + NeuVal[ineu]
        
    return stiffMat, rhs