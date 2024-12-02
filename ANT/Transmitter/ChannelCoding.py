# Channel Encoder

import numpy as np
from ANT import bits

# Parity check matrix generation
'''This function generates a fixed parity-check matrix for (7,4) Hamming code.'''
def generate_parity_check_matrix():
    parity_check_mat = np.array([[1,0,0,1,1,1,0],
                                 [0,1,0,1,1,0,1],
                                 [0,0,1,1,0,1,1]])
    return parity_check_mat

# Generate the parity-check matrix and assign it to a variable
parity_check_matrix = generate_parity_check_matrix()

# Print the parity check matrix
print(f'Parity check matrix: \n {parity_check_matrix}')



'''This function generator the generator matrix based on the parity-check matrix'''
def generate_generator_matrix(parity_check_matrix):
    parity=parity_check_matrix[:-4]
    generator_mat=np.array(np.identity(4))


    return generator_matrix

generator_matrix = generate_generator_matrix(parity_check_matrix)



# code=encode_hamming(bits,parity_check_matrix)
