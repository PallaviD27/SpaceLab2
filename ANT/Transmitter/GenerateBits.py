import numpy as np
import matplotlib.pyplot as plt


# Digital Source's output

# b= generate_bits(n_bits), API definition 3.4.2


def generate_bits(n_bits,switch_graph):
    '''
    Generate a random bit string/vector of integers (0 and 1).

    Parameters:
        n_bits (int): Number of bits to generate. Must be a multiple of 16.
        switch_graph : If ON, a bar graph of the bit values is plotted.

    Returns:
        np.ndarray or None: A NumPy array of random bits (0s and 1s) if n_bits is valid, else None.
    '''
# Checking if input is multiple of 16
    try:
        if n_bits % 16 !=0:
            raise ValueError ("Number of input bits 'n_bits' should be a multiple of 16")
# Generate a random bit stream
        bits_source=np.random.randint(0,2,size=n_bits)

# Print randomly generated bit stream
        print(f'\033[32m\033[1mInput bits:\033[0m\033[0m {bits_source}')

# Graph of input bits to be plotted only if switch_graph= ON
        if switch_graph=='ON':
            plt.figure(figsize=(6, 6))
# Bars to display bit values
            plt.bar(range(len(bits_source)), bits_source,width=0.2, color='blue', edgecolor='black',label='Bit Value')
# Graphical details of plot
            plt.title('Generated Bit Stream',fontweight='bold')
            plt.xlabel('Bit Index',fontweight='bold')
            plt.xlim(-0.1,n_bits)
            plt.xticks(range(0,n_bits+1,1))
            plt.ylabel("Bit Value",fontweight='bold')
            plt.ylim(0,1)
            plt.yticks([0, 1])
            plt.grid(axis='both', linestyle='--', alpha=0.7)
            plt.show()

        else:
            pass

        return bits_source
# Display error if input for number of bits is not a multiple of 16
    except ValueError as error:
        print(f'\033[31mError:\033[0m {error}')
        return None