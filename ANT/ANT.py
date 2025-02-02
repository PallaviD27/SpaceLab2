'''This is the main file calling the function from different modules.
Output being displayed in Green and input prompts in Red
Receiver side doesn't work so is to be commented out before running the
transmitter and Channel. Also corresponding import lines are to be commented for Receiver
'''
# Import of functions created in GenerateBits.py
from Transmitter.GenerateBits import generate_bits
from Transmitter.ChannelCoding import encode_hamming
from Transmitter.ChannelCoding import generate_parity_check_matrix
from Transmitter.Modulation import map2symbols
from Channel.Channel import transmitter_power
from Channel.Channel import simulate_channel
from Transmitter.Filter import filter_tx
import matplotlib.pyplot as plt
# Receiver side import - to be commented because not working
from Receiver.Demodulation import detect_symbols
from Receiver.Decode import decode_hamming
from Receiver.Decode import binary_to_decimal
from Receiver.Sink import count_errors

import numpy as np

# Transmitter
'''Generate Bits'''
# User input for bit string generation
try:
    n_bits = float(input("\033[31m\033[1mEnter input bit length:\033[0m\033[0m "))  # Read input as a float
    if n_bits.is_integer():  # Check if the number is actually an integer
        n_bits = int(n_bits)  # Convert to int
    else:
        raise ValueError("The number of bits should be an integer")
except ValueError as e:
    print(f"Error: {e}")

# Use of already defined function to generate string of input bits
bits = generate_bits(n_bits,'ON')

'''Channel Coding'''

# Using already defined function to generate the parity check matrix
parity_check_matrix=generate_parity_check_matrix()

# Generating Code word using the already defined function
Code_word = encode_hamming(bits,parity_check_matrix)

print(f"\033[32m\033[1mCode word:\033[0m\033[0m {Code_word}")

'''Modulation'''

#Input for selection of Modulating Scheme
switch_mode=int(input("\033[31m\033[1mEnter a switch mode(0 for 16-QAM and 1 for 16-PSK):\033[0m\033[0m "))

switch_graph = input("\033[31m\033[1mEnter ON/on to display graph or OFF otherwise:\033[0m\033[0m ")

Modulated_Output = map2symbols(Code_word,switch_mode,switch_graph)

d= Modulated_Output[:,0] + 1j * Modulated_Output[:,1]

print(f'\033[32m\033[1mComplex Signal:\033[0m\033[0m {d}')

'''Filter'''
# Transmitter Filter
# Generate Filtered Signal with d aka Complex Signal as input
usf_filter = 8
Filtered_signal=filter_tx(d,usf_filter,"ON")

# Channel
'''Channel'''
# Generator
tx_power = transmitter_power()
switch_graph_channel = input("\033[31m\033[1mEnter ON/on to display graph of channel output or OFF otherwise:\033[0m\033[0m ")
[y,SNR] =  simulate_channel(Filtered_signal,tx_power,switch_graph_channel)

# Receiver Side
# filter - Not implemented

# demodulation - Need to be commented out because not working correctly
angle = np.angle(p)
print(angle)
c_hat = detect_symbols(d,0,'ON')
print(c_hat)

# decode - Need to be commented out because not working correctly
b_hat=decode_hamming(c_hat,parity_check_matrix,switch_graph)
print(b_hat)
print(f"Code word: {Code_word}")

# sink - Need to be commented out because not working correctly
[BE,BEuc]=count_errors(bits,b_hat,Code_word,c_hat)

plt.show()

