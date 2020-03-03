from mmd.molecule import Molecule 
import numpy as np
from mmd.postscf import PostSCF

water = """
0 1
O    0.000000      -0.075791844    0.000000
H    0.866811829    0.601435779    0.000000
H   -0.866811829    0.601435779    0.000000
"""

# init molecule and build integrals
mol = Molecule(geometry=water,basis='sto-3g')

# do the SCF
mol.RHF()

# do MP2
PostSCF(mol).MP2()

np.set_printoptions(formatter={'float': '{: 0.6f}'.format})

print(mol.CAP)
#cap_mat = np.real(np.dot(np.transpose(mol.CO),np.dot(mol.CAP,mol.CO)))
#H = np.diag(mol.MO)
#H_n = H - 1j*0.001*cap_mat
#np.savetxt("myarray.txt",H, fmt='%10.6f', delimiter=" ")

#EVAL, EVECS = np.linalg.eigh(H_n)

#np.savetxt("cap_eigvals.txt", np.diag(EVAL), fmt='%10.6f', delimiter="  ")
