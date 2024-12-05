import os

#os.mkdir('Transmitter')
#os.mkdir("Channel")
#os.mkdir("Receiver")

# Importing functions created in GenerateBits.py
from Transmitter.GenerateBits import generate_bits

# Importing functions created in Channel.py
from Channel import Channel

# Importing functions created in Receiver.py
from Receiver import Receiver

bits = generate_bits(32.32,False)

print(bits)