from mmd.molecule import Molecule 
from mmd.postscf import PostSCF
import numpy as np

h2 = """
0 1
H    0.000000000    0.000000000   -0.368652
H    0.000000000    0.000000000    0.368652
"""

# init molecule and build integrals
mol = Molecule(geometry=h2,basis='6-311G**')

# do the SCF
mol.RHF()

# do MP2
PostSCF(mol).MP2()

#print(mol.CAP)

np.savetxt("cap_h2.dat",mol.CAP,'%10.6f',delimiter=" ")

#P_MO = np.real(np.dot(np.transpose(mol.CO),np.dot(mol.P,mol.CO)))

#DEN = np.real(np.dot(np.transpose(mol.CO),np.dot(mol.CAP,mol.CO)))

#print(DEN)

#new = np.real(np.dot(mol.CAP,mol.P))

#trace = np.trace(new)

#print(trace)
