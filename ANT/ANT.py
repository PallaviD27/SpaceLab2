import os

#os.mkdir('Transmitter')
#os.mkdir("Channel")
#os.mkdir("Receiver")

# Importing functions created in GenerateBits.py
from Transmitter.GenerateBits import generate_bits
from Transmitter.ChannelCoding import encode_hamming
from Transmitter.ChannelCoding import generate_parity_check_matrix

# Importing functions created in Channel.py
from Channel import Channel

# Importing functions created in Receiver.py
from Receiver import Receiver


try:
    n_bits = float(input("Enter input bit length: "))  # Read input as a float
    if n_bits.is_integer():  # Check if the number is actually an integer
        n_bits = int(n_bits)  # Convert to int
    else:
        raise ValueError("The number of bits should be an integer")
except ValueError as e:
    print(f"Error: {e}")

bits = generate_bits(n_bits,False)

print(bits)

parity_check_matrix=generate_parity_check_matrix()

Code_word = encode_hamming(bits,parity_check_matrix)

print(f"Code word: {Code_word}")

Code_length = len(Code_word)

print(f"Length of the code word:{Code_length} ")