# Channel Encode

import numpy as np
from ANT import bits


# Parity check matrix generation
'''Start'''

'''This function generates a fixed parity-check matrix for (7,4) Hamming code.'''
def generate_parity_check_matrix():
    parity_check_mat = np.array([[0,1,1,1,1,0,0],
                                 [1,0,1,1,0,1,0],
                                 [1,1,0,1,0,0,1]])
    return parity_check_mat

# Generate the parity-check matrix and assign it to a variable
# Also check order of the parity check matrix
parity_check_matrix = generate_parity_check_matrix()
order_parity_check = parity_check_matrix.shape

# Print the parity check matrix
print(f'The parity check matrix of order {order_parity_check}: \n {parity_check_matrix}')

'''End'''


'''Start'''

'''This function generates the generator matrix based on the parity-check matrix'''
def generate_generator_matrix(parity_check_matrix):
    parity=parity_check_matrix[:,:4]

    parity_transpose=parity.transpose()

    I=np.identity(4)     # generates Identity to concatenate with the parity check matrix

    generator_mat=np.hstack((I,parity_transpose)) #generator matrix made with stacking 4x4 identity matrix and
                                                   # transpose of last four columns of partity check matrix
    return generator_mat

# Generating the generator matrix
generator_matrix = generate_generator_matrix(parity_check_matrix)

verify = (np.dot(parity_check_matrix, generator_matrix.transpose()))%2

print(f'Only for verification of G.HTanspose = 0: \n {verify}')

order_generator_matrix= generator_matrix.shape
print(f'The generator matrix of the order {order_generator_matrix}: \n {generator_matrix}')

'''End'''


'''Start'''

'''This function generates the codeword based on the input bits and the generator matrix'''

def encode_hamming(bits,parity_check_matrix):










# code=encode_hamming(bits,parity_check_matrix)
