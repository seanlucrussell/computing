import numpy as np

#quantum state with n qubits represented by
#complex vector of length 2^n of magnitude
#1

#quantum computation represented by unitary
#matrices with unit determinant, which are
#members of SU(n), the special unitary group

#a unitary matrix A is a complex matrix such
#that the conjugate transpose of A times A
#is the identity matrix

#actually I don't think that computations
#require the unitary matrix determinant to
#be 1. It can be whatever
#no the MAGNITUDE of the determinant has to
#be 1. Thats it

class State():

    def __init__(self,n):
        self.state = np.zeros(2**n,dtype='complex')
        self.state[0] = 1

    def measure(self, n):
        probabilites = self.state.conjugate().dot(self.state)
        
        return np.random.choice(np.arange(len(self.state)),p=self.state)
                                

def hadamard_state(n):
    return (2 ** -.5) ** n * np.ones(2**n,dtype='complex')

def identity_transformation(n):
    return np.identity(2**n,dtype='complex')

def verify_state(S):
    return np.isclose(np.linalg.norm(S) ** 2, 1)

def verify_transformation(T):
    return np.isclose(T.conjugate().T.dot(T),np.identity(T.shape[0])).all()


#single qubit things

zero = np.array([1+0j,0+0j])
one = np.array([0+0j,1+0j])

not_transformation = np.array([[0+0j,1+0j],[1+0j,0+0j]])

def single_cubit_transformation(a,b):
    return np.array([a,-b.conjugate(),b,a.conjugate()])
