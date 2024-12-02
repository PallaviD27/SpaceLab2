import numpy as np


# Digital Source's output

'''This function generates a bit string/vector of random integers 0 and 1, 
and length equal to n_bits using the numpy. 'n_bits' takes integer input'''

# b= generate_bits(n_bits) # API definition 3.4.2

def generate_bits(n_bits,switch_graph=False):
    try:
        bits_source=np.random.randint(0,2,size=n_bits)

    except TypeError:
        print("Number of input bits 'n_bits' should be an integer")
        return None

    # Graph to be plotted only when switch_graph parameter is true


    return bits_source





