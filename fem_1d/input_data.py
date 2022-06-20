import numpy as np

def input_data(a, b, Nelem):
    Nodes = Nelem + 1
    
    # Uniform subdivision assumed
    # Can be substituted with a read from file for a non uniform mesh
    xcoord = np.linspace(a, b, Nodes)

    # array "elem" - element the two nodes in the global numbering defined in x coord 
    # (node 1 is the first element of xcoord)
    # (left and right in this order)
    elem = np.zeros((2, Nelem), dtype=int)
    # Left nodes
    elem[0,0:Nelem] = range(1, Nelem+1)
    # Right nodes
    elem[1,0:Nelem] = range(2, Nelem+2)

    # Define Dirichlet Boundary conditions (Nodes that are applied and Values)
    NDir = 2
    DirNod = np.zeros((NDir, 1), dtype=int)
    DirVal = np.zeros((NDir, 1))
    DirNod[0] = 1
    DirNod[1] = Nodes
    DirVal[0] = 0
    DirVal[1] = 0

    # Define Diffusion Coeffient
    Diff = np.ones((Nelem, 1))
    
    #Diff = np.ones((Nelem, 1))
    #Diff[0:int(Nelem/2)] = 10

    # Define source function
    source = lambda x: source_func(x)
    ureal = lambda x: ureal_func(x)

    return Nodes, NDir, xcoord, elem, DirNod, DirVal, Diff, source, ureal

def source_func(x):
    kconst = 1
    return (kconst * np.pi)**2 * np.sin(kconst * np.pi * x)

def ureal_func(x):
    kconst = 1
    return np.sin(kconst * np.pi * x)
    

