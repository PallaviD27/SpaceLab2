import numpy as np
import matplotlib.pyplot as plt

"""Parameters
 c_hat: vector of estimated codebits
 parity_check_matrix: parity check of a [7,4] Hamming code
 switch_graph:switch graphical output on or off

 output:
 b_hat: vector of decoded bits"""


# c_hat = [0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0]
# print('c_hat',c_hat)
if len(c_hat)%7 != 0:
    print("Length of c_hat must be a multiple of 7")

parity_check_mat1 = np.array([[0,1,1,1,1,0,0],
                                 [1,0,1,1,0,1,0],
                                 [1,1,0,1,0,0,1]])
print("parity_check_mat1",parity_check_mat1)
# define function
def decode_hamming(c_hat, parity_check_matrix, switch_graph):
    blocks = []
    # make blocks of bits
    for k in range(0, len(c_hat) // 7):
        start = k * 7
        end = start + 7
        block = list(c_hat[start:end])
        blocks.append(block)
        print('blocks after iteration', blocks)

    b_hat = []
    print ('b_hat',b_hat)
    bits_int = []
    print('bits_int',bits_int)
    for block in blocks:
        # converting the bits into integers and transposing it
        int_list = [int(bit) for bit in block]
        bits_int.append(int_list)
        print('bits_int', bits_int)

    bits_int = np.array(bits_int).T
    print('bits_int', bits_int)

    # Syndrome decoding
    syndrome = np.dot(parity_check_mat1, bits_int) % 2
    print('syndrome',syndrome)

    # converting the binary to decimal
    if np.sum(syndrome) != 0:
        print("Error detected")
    error_code = syndrome.copy()
    print('error_code:',error_code)

    syndrome_flattened=syndrome.flatten()
    print('syndrome_flattened:',syndrome_flattened)
    syndromes = [syndrome_flattened[i:i+3] for i in range(0, len(syndrome_flattened), 3)]
    print('syndromes:',syndromes)

    error_positions=[]
    for syndrome in syndromes:
        # Convert binary to decimal
        error_position = int(''.join(map(str, syndromes)), 2)
        error_positions.append(error_position)
    print('error_positions:',error_positions)


