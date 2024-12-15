import numpy as np
import matplotlib.pyplot as plt

"""Parameters
 c_hat: vector of estimated codebits
 parity_check_matrix: parity check of a [7,4] Hamming code
 switch_graph:switch graphical output on or off
 
 output:
 b_hat: vector of decoded bits"""
def binary_to_decimal(binary):
    decimal=0
    for bit in binary:
        decimal=decimal*2+int(bit)
    return decimal

def decode_hamming(c_hat,parity_check_matrix,switch_graph):
    blocks=[]
    # make blocks of bits
    for k in range(0,len(c_hat)//7):
        start=k*7
        end=start+7
        block=list(c_hat[start:end])
        blocks.append(block)

    bits_int=[]
    for block in blocks:
        # converting the bits into integers and transposing it
        int_list=[int(bit) for bit in block]
        bits_int.append(int_list)

    bits_int=np.array(bits_int).T

        # Syndrome decoding
        syndrome=np.dot(parity_check_matrix,bits_int)%2

        if np.sum(syndrome)!=0:
            print("Error detected")
            error_code=bits_int
            error=binary_to_decimal(syndrome)
            if (error_code[error-1]==1):
                error_code[error-1]=0
            else:
                error_code[error-1]==1
                b_hat=error_code[:4]


    if (switch_graph==1):
        plt.plot(c_hat,label="Receieved")
        plt.plot(b_hat,label="Corrected")
        plt.legend()
        plt.title("Decoding")
        plt.show()
    return b_hat




















