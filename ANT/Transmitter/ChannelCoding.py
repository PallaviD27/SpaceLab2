# Channel Encoder
# c = encode_hamming(b, parity_check_matrix), API definition 3.4.2

import numpy as np


# Parity check matrix generation
'''Start'''
def generate_parity_check_matrix():
    '''
    Generate a fixed parity-check matrix for (7,4) Hamming code
        Parameter:
            np.ndarray: parity check matrix of shape (3,7)
        Returns:
            parity_check_mat1
    '''

    parity_check_mat1 = np.array([[0,1,1,1,1,0,0],
                                 [1,0,1,1,0,1,0],
                                 [1,1,0,1,0,0,1]])
    return parity_check_mat1

# Generate the parity-check matrix and assign it to variable
parity_check_matrix1 = generate_parity_check_matrix()

# Order of parity check matrix
order_parity_check1 = parity_check_matrix1.shape

# Print parity check matrix
print(f'\033[32m\033[1mThe parity check matrix of order {order_parity_check1}:\033[0m\033[0m \n {parity_check_matrix1}')

'''End'''


'''Start'''
def generate_generator_matrix(parity_check_matrix):
    '''
    Generates the generator matrix for (7,4) Hamming code using parity-check matrix
    Parameter:
        parity_check_matrix (np.ndarray): Parity check matrix of shape (3,7)
    Returns:
        np.ndarray: generator_mat, generator matrix of shape (4,7)
    '''
# Extract first four columns of the parity check matrix and compute its transpose
    parity=parity_check_matrix1[:,:4]
    parity_transpose=parity.transpose()

# (4 x 4) Identity matrix to concatenate with the parity check matrix
    I=np.identity(4)

# Construct generator matrix by  stacking 4x4 identity matrix and transpose of last four columns of partity check matrix
    generator_mat=np.hstack((I,parity_transpose))

    return generator_mat

# Generate generator matrix
generator_matrix = generate_generator_matrix(parity_check_matrix1)

# Verify product of one of the matrices and the transpose of the other = 0
verify = (np.dot(parity_check_matrix1, generator_matrix.transpose()))%2
print(f'\033[32m\033[1mOnly for verification of G.HTanspose = 0:\033[0m\033[0m \n {verify}')

# Get Order of the generator and print it
order_generator_matrix= generator_matrix.shape
print(f'\033[32m\033[1mThe generator matrix of the order {order_generator_matrix}:\033[0m\033[0m \n {generator_matrix}')

'''End'''


'''Start'''

def encode_hamming(bits,parity_check_matrix):
    '''
    Generates the codeword based on the input bits and the generator matrix, as per (7,4) Hamming Code

    Parameters:
        bits(np.ndarray): input bit stream
        parity check matrix (np.ndarray): Parity check matrix of shape (3,7)

    Returns:
        Codeword : coded sequence of 7 bits per 4 input bits as per (7,4) Hammming Code
    '''
    sets = len(bits)//4
    print(sets)
    CodeWord=[]
    for i in range (sets):
        seti=bits[i*4:(i+1)*4]
        print(f"\033[32m\033[1mSet {i+1}:\033[0m\033[0m {seti}")
        CodeSeti=(np.dot(seti,generator_matrix)%2).astype(int)
        print(f"\033[32m\033[1mCodeSet {i+1}:\033[0m\033[0m {CodeSeti} ")
        CodeWord.extend(CodeSeti.tolist())
    return CodeWord

'''End'''