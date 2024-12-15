import os

#os.mkdir('Transmitter')
#os.mkdir("Channel")
#os.mkdir("Receiver")

# Importing functions created in GenerateBits.py
from Transmitter.GenerateBits import generate_bits
from Transmitter.ChannelCoding import encode_hamming
from Transmitter.ChannelCoding import generate_parity_check_matrix
from Transmitter.Modulation import map2symbols
from Channel.Channel import transmitter_power
from Channel.Channel import simulate_channel
from Transmitter.Filter import filter_tx
from Receiver.Demodulation import detect_symbols
import numpy as np
# Importing functions created in Channel.py
from Channel import Channel

# Importing functions created in Receiver.py
from Receiver import Receiver

# Taking user input for bit string generation
try:
    n_bits = float(input("Enter input bit length: "))  # Read input as a float
    if n_bits.is_integer():  # Check if the number is actually an integer
        n_bits = int(n_bits)  # Convert to int
    else:
        raise ValueError("The number of bits should be an integer")
except ValueError as e:
    print(f"Error: {e}")


# Using already defined bit string to generate string of input bits
bits = generate_bits(n_bits,False)

print(bits)


# Usign already defined function to generate the parity check matrix
parity_check_matrix=generate_parity_check_matrix()


# Generating Code word using the already defined function
Code_word = encode_hamming(bits,parity_check_matrix)

print(f"Code word: {Code_word}")

    # Code_length = int(len(Code_word))

# print(f"Length of the code word:{Code_length} ")


#Input for selection of Modulating Scheme
switch_mode=int(input("Enter a switch mode(0 for 16-QAM and 1 for 16-PSK): "))

switch_graph = input("Enter ON to display graph or OFF otherwise: ")

Modulated_Output = map2symbols(Code_word,switch_mode,switch_graph)

d= Modulated_Output[:,0] + 1j * Modulated_Output[:,1]

print(f'Complex Signal:{d}')

# x=filter_tx(d,8,"ON")

# Channel
tx_power = transmitter_power()
switch_graph_channel = input("Enter ON to display graph of channel output or OFF otherwise: ")
[y,SNR] =  simulate_channel(d,tx_power,switch_graph_channel)

# Receiver Side

c_hat = detect_symbols(d,1,'ON')
print(c_hat)
