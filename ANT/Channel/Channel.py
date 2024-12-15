# Baseband Channel
#d=simulate_channel(x,tx_power,switch_graph)  # API defintion 3.5.2

import numpy as np
import matplotlib.pyplot as plt

'''' A channel is constituted of transmitter amplifier, path loss, additive whote gaussian noise and receiver amplifier
Transmitter amplifier - amplifies the transmitted signal
Path Loss -

Receiver amplifier - amplifies received signal. GRX =1

Path loss =

Aim is to achieve a desired SNR
'''
# Calculate PathLoss

distance = 36000000    # Height of GEO satellites above the surface of the earth in m
CarrierFreq = 20000000000   # Carrier frequency of 20 GHz
LightSpeed = 300000000  # Speed of light in m/s
Ga = 40    # Transmitter antenna gain in dBi
Gb = 40       # Receiver antenna gain in dBi
TN= 165       # Noise temperature in K
BW = 800000000    # Bandwidth in Hz
kB = 1.38e-23    # Boltzmann constant in W/Hz K




# Calculate Path Loss in dB
PathLoss = (20 * np.log10 ((4 * np.pi * distance * CarrierFreq )/LightSpeed)) - (Ga + Gb)
PathLoss_linear  =  10 ** (-PathLoss/10)

print(f'Path loss: {PathLoss} dB')
print(f'Linear path loss: {PathLoss_linear}')

# Calculate Noise Power
Noise_power = (kB * TN * BW)   # Noise power for bandwidth is Power spectral density * bandwidth. Power spectral density = (kB * TN )/2
print(f'Noise Power:{Noise_power}')

def transmitter_power():
    trans_power = (Noise_power * (10**2) )/PathLoss_linear  # Calculate transmitter power for SNR = 20 dB at receiver
    print(f'Transmitter Power:{trans_power} ')
    return 10.0
def simulate_channel(x,tx_power,switch_graph):
    amplified_x = x * tx_power
    print(f'Amplified input: {amplified_x}')
    att_sig = amplified_x * np.sqrt (PathLoss_linear)      # Calculate attenuated signal by multiplying with path loss factor
    print(f'Attenuated input after path losses:{att_sig}')
    # Complex_att_sig = att_sig[:,0] + 1j*att_sig[:,1]
    # print(f'Complex attenuated signal:{Complex_att_sig}')
    Noise_std_dev= np.sqrt(Noise_power/2)
    print(f'Standard deviation of noise:{Noise_std_dev}')
    Random_Noise = np.random.randn(len(x))
    print(f'Random generated noise: {Random_Noise}')
    Noise_real= Noise_std_dev * np.random.randn(len(x))
    Noise_imag = Noise_std_dev * np.random.randn(len(x))
    WGN = np.column_stack(Noise_real + 1j * Noise_imag)
    print(WGN)
    y = att_sig + WGN
    SNR=10 * np.log10 (tx_power * PathLoss_linear / Noise_power)
    print (y)

    if switch_graph.upper()==('ON'):
        plt.figure(figsize=(6, 6))
        plt.scatter(np.real(y), np.imag(y), color='r')
        plt.title("Received Signal (with Noise)")
        plt.xlabel("In-phase")
        plt.ylabel("Quadrature-phase")
        plt.grid(True)
        plt.show()

    else:
        pass

    return y,SNR

